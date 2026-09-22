from app import app, db
from models import Game, User
from werkzeug.security import generate_password_hash
from config import Config

with app.app_context():
    # Удаляем все старые таблицы
    db.drop_all()
    print("✅ Старые таблицы удалены")

    # Создаём новые
    db.create_all()
    print("✅ Новые таблицы созданы")

    # Добавляем игры
    games = [
        Game(name='sudoku', display_name='Судоку'),
        Game(name='dino', display_name='Динозаврик'),
        Game(name='tetris', display_name='Тетрис')
    ]
    for game in games:
        db.session.add(game)
        print(f"✅ Добавлена игра: {game.display_name}")

    # Создаём админа
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