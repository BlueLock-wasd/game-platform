from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, date
from config import Config

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(Config.USERNAME_MAX_LENGTH), unique=True, nullable=False)
    email = db.Column(db.String(Config.EMAIL_MAX_LENGTH), unique=True, nullable=False)
    password_hash = db.Column(db.String(Config.PASSWORD_HASH_MAX_LENGTH), nullable=False)
    role = db.Column(
        db.Enum(Config.ROLE_USER, Config.ROLE_ADMIN),
        default=Config.ROLE_USER
    )
    avatar_url = db.Column(db.String(255), default=Config.DEFAULT_AVATAR)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login_date = db.Column(db.Date, default=date.today)

    # Связи
    streak = db.relationship('LoginStreak', backref='user', uselist=False,
                             cascade='all, delete-orphan')
    game_sessions = db.relationship('GameSession', backref='user', lazy='dynamic',
                                    cascade='all, delete-orphan')

    # Заметки, которые написал user
    notes = db.relationship('Note', backref='author', foreign_keys='Note.author_id',
                            lazy='dynamic', cascade='all, delete-orphan')


class LoginStreak(db.Model):
    __tablename__ = 'login_streaks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    current_streak = db.Column(db.Integer, default=0)
    max_streak = db.Column(db.Integer, default=0)
    last_update = db.Column(db.Date, default=date.today)


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(100), nullable=False)

    sessions = db.relationship('GameSession', backref='game', lazy='dynamic')


class GameSession(db.Model):
    __tablename__ = 'game_sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    score = db.Column(db.Integer, default=0)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)     # кому
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)   # кто написал
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Связи
    recipient = db.relationship('User', foreign_keys=[user_id], backref='notes_for_me') 