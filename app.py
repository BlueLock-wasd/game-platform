from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta
from functools import wraps
import os
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from config import Config
from models import db, User, Game, GameSession, LoginStreak, Note
from forms import LoginForm, RegisterForm, ChangePasswordForm, NoteForm



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = Config.MSG_LOGIN_REQUIRED


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != Config.ROLE_ADMIN:
            flash(Config.MSG_ACCESS_DENIED, 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)

    return decorated_function


@app.context_processor
def inject_globals():
    return {
        'Config': Config,
        'current_year': date.today().year
    }


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


def update_streak(user):
    today = date.today()
    streak = LoginStreak.query.filter_by(user_id=user.id).first()

    if not streak:
        streak = LoginStreak(user_id=user.id)
        db.session.add(streak)

    if streak.current_streak is None:
        streak.current_streak = 0
    if streak.max_streak is None:
        streak.max_streak = 0

    if user.last_login_date != today:
        if user.last_login_date == today - timedelta(days=1):
            streak.current_streak += 1
        else:
            streak.current_streak = 1

        if streak.current_streak > streak.max_streak:
            streak.max_streak = streak.current_streak

        streak.last_update = today
        user.last_login_date = today
        db.session.commit()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_IMAGE_EXTENSIONS


@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            update_streak(user)
            flash(Config.MSG_LOGIN_SUCCESS, 'success')
            return redirect(url_for('profile', username=user.username))
        flash(Config.MSG_LOGIN_FAILED, 'danger')

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()

        streak = LoginStreak(user_id=user.id)
        db.session.add(streak)
        db.session.commit()

        flash(Config.MSG_REGISTER_SUCCESS, 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/admin')
@admin_required
def admin_panel():
    users = User.query.all()
    admins_count = User.query.filter_by(role=Config.ROLE_ADMIN).count()
    total_games = GameSession.query.count()
    total_notes = Note.query.count()
    active_today = User.query.filter_by(last_login_date=date.today()).count()
    
    return render_template('admin/dashboard.html',
                           users=users,
                           admins_count=admins_count,
                           total_games=total_games,
                           total_notes=total_notes,
                           active_today = active_today)


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = NoteForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        note = Note(
            user_id=user.id,
            author_id=current_user.id,
            content=form.content.data
        )
        db.session.add(note)
        db.session.commit()
        flash(Config.MSG_NOTE_ADDED, 'success')
        return redirect(url_for('profile', username=username))

    # Статистика по играм
    stats = {}
    for game in Game.query.all():
        sessions = GameSession.query.filter_by(user_id=user.id, game_id=game.id).all()
        if sessions:
            total = len(sessions)
            scores = [s.score for s in sessions]
            max_score = max(scores)
            avg_score = sum(scores) // total
            last_played = sessions[-1].played_at.strftime(Config.DATE_DISPLAY_FORMAT)

            stats[game.name] = {
                'total': total,
                'max': max_score,
                'avg': avg_score,
                'last': last_played,
                'scores': sorted(scores, reverse=True)[:Config.TOP_LIMIT]
            }

    # Серия заходов
    streak = LoginStreak.query.filter_by(user_id=user.id).first()
    # Комментарии для этого пользователя
    notes = Note.query.filter_by(user_id=user.id).order_by(Note.created_at.desc()).all()

    return render_template('profile.html',
                           user=user,
                           stats=stats,
                           streak=streak,
                           notes=notes,
                           form=form)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if check_password_hash(current_user.password_hash, form.old_password.data):
            current_user.password_hash = generate_password_hash(form.new_password.data)
            db.session.commit()
            flash(Config.MSG_PASSWORD_CHANGED, 'success')
            return redirect(url_for('profile', username=current_user.username))
        flash(Config.MSG_PASSWORD_WRONG, 'danger')

    games = Game.query.all()
    return render_template('settings.html', form=form, games=games)


@app.route('/notes')
@login_required
def notes_list():
    notes = current_user.notes_for_me.order_by(Note.created_at.desc()).all()  # ← изменено
    return render_template('notes.html', notes=notes)


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/games')
@login_required
def games():
    games = Game.query.all()
    return render_template('games.html', games=games)


@app.route('/game/<game_name>')
@login_required
def play_game(game_name):
    game = Game.query.filter_by(name=game_name).first_or_404()
    return render_template(f'games/{game_name}.html', game=game)


@app.route('/api/save_score', methods=['POST'])
@login_required
def save_score():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': Config.MSG_NO_DATA}), 400
        game_name = data.get('game')
        if not game_name:
            return jsonify({'success': False, 'message': Config.MSG_GAME_NOT_SPECIFIED}), 400

        game = Game.query.filter_by(name=game_name).first()
        if not game:
            return jsonify({
                'success': False,
                'message': Config.MSG_GAME_NOT_FOUND.format(game=game_name)
            }), 404

        session = GameSession(
            user_id=current_user.id,
            game_id=game.id,
            score=data.get('score', 0)
        )
        db.session.add(session)
        db.session.commit()
        return jsonify({'success': True, 'message': Config.MSG_SCORE_SAVED})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'success': False, 'message': Config.MSG_DB_ERROR}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False,
                        'message': Config.MSG_UNKNOWN_ERROR.format(error=str(e))
        }), 500


@app.route('/admin/users')
@admin_required
def admin_users():
    users = User.query.all()
    total_games = GameSession.query.count()
    active_today = User.query.filter_by(last_login_date=date.today()).count()
    return render_template('admin/users.html', users=users, total_games=total_games, active_today=active_today)


@app.route('/admin/toggle/<int:user_id>')
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    if user.id != current_user.id:
        user.role = (Config.ROLE_USER if user.role == Config.ROLE_ADMIN
                     else Config.ROLE_ADMIN)
        db.session.commit()
        flash(Config.MSG_ROLE_CHANGED.format(username=user.username), 'success')
    return redirect(url_for('admin_users'))


@app.route('/admin/delete/<int:user_id>')
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.id != current_user.id:
        db.session.delete(user)
        db.session.commit()
        flash(Config.MSG_USER_DELETED.format(username=user.username), 'success')
    return redirect(url_for('admin_users'))


@app.route('/api/top_players')
@admin_required
def top_players():
    users = User.query.all()
    top = sorted(users, key=lambda u: u.game_sessions.count(), reverse=True)[:Config.TOP_LIMIT]
    return jsonify({
        'names': [u.username for u in top],
        'counts': [u.game_sessions.count() for u in top]
    })


@app.route('/api/game_stats')
@admin_required
def game_stats():
    games = Game.query.all()
    return jsonify([
        {
            'name': g.name,
            'display_name': g.display_name,
            'count': GameSession.query.filter_by(game_id=g.id).count()
        }
        for g in games
    ])


@app.route('/api/delete_note/<int:note_id>', methods=['DELETE'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)

    if note.author_id == current_user.id or current_user.role == Config.ROLE_ADMIN:
        db.session.delete(note)
        db.session.commit()
        return jsonify({'success': True})

    return jsonify({'success': False, 'message': Config.MSG_NO_RIGHTS}), 403


@app.route('/upload_avatar', methods=['POST'])
@login_required
def upload_avatar():
    if 'avatar' not in request.files:
        flash(Config.MSG_FILE_NOT_SELECTED, 'danger')
        return redirect(url_for('settings'))

    file = request.files['avatar']

    if file.filename == '':
        flash(Config.MSG_FILE_NOT_SELECTED, 'danger')
        return redirect(url_for('settings'))

    if file and allowed_file(file.filename):
        filename = secure_filename(f"user_{current_user.id}_{file.filename}")

        upload_folder = os.path.join(app.static_folder, Config.UPLOAD_SUBFOLDER)
        os.makedirs(upload_folder, exist_ok=True)

        file.save(os.path.join(upload_folder, filename))

        current_user.avatar_url = f'{Config.AVATAR_URL_PREFIX}/{filename}'
        db.session.commit()

        flash(Config.MSG_AVATAR_UPDATED, 'success')
    else:
        flash(Config.MSG_INVALID_FORMAT, 'danger')

    return redirect(url_for('settings'))


@app.route('/api/top_scores')
def top_scores():
    top = db.session.query(
        User.username,
        GameSession.score,
        Game.display_name
    ).join(GameSession, User.id == GameSession.user_id
           ).join(Game, GameSession.game_id == Game.id
                  ).order_by(GameSession.score.desc()
                             ).limit(Config.TOP_LIMIT).all()

    return jsonify([{
        'username': u[0],
        'score': u[1],
        'game_name': u[2]
    } for u in top])    


@app.route('/api/delete_account', methods=['DELETE'])
@login_required
def delete_account():
    if current_user.role == Config.ROLE_ADMIN:
        admins_count = User.query.filter_by(role=Config.ROLE_ADMIN).count()
        if admins_count <= 1:
            return jsonify({'success': False, 'message': Config.MSG_LAST_ADMIN}), 403

    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return jsonify({'success': True})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(Config.MSG_LOGOUT, 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=Config.DEBUG)