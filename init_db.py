from app import app, db
from models import Game, User
from werkzeug.security import generate_password_hash
from config import Config
import os, sys

with app.app_context():
    if os.environ.get('CONFIRM_DROP') != 'yes':
        print("⚠️  Установите CONFIRM_DROP=yes для подтверждения")
        sys.exit(1)

    db.drop_all()
    print("✅ Старые таблицы удалены")

    db.create_all()
    print("✅ Новые таблицы созданы")

    games = [
        Game(name='sudoku', display_name='Судоку', icon='images/sudoku.png'),
        Game(name='dino', display_name='Динозаврик', icon='images/phon_dino.png'),
        Game(name='tetris', display_name='Тетрис', icon='images/tetris.png'),
    ]
    for game in games:
        db.session.add(game)
        print(f"✅ Добавлена игра: {game.display_name}")

    admin = User(
        username=Config.ADMIN_USERNAME,
        email=Config.ADMIN_EMAIL,
        password_hash=generate_password_hash(Config.ADMIN_PASSWORD),
        role=Config.ROLE_ADMIN,
        avatar_url=Config.DEFAULT_AVATAR
    )
    db.session.add(admin)
    print(f"✅ Создан администратор: {Config.ADMIN_USERNAME}")

    db.session.commit()
    print("🎉 База данных успешно создана!")

