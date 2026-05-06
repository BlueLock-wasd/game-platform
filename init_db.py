from app import app, db
from models import Game, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Удаляем все старые таблицы
    db.drop_all()
    print("✅ Старые таблицы удалены")

    # Создаем только нужные таблицы
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

    # Создаем админа
    admin = User(
        username='admin',
        email='admin@game.ru',
        password_hash=generate_password_hash('admin123'),
        role='admin',
        avatar_url='default.jpg'
    )
    db.session.add(admin)
    print("✅ Создан администратор: admin / admin123")

    db.session.commit()
    print("🎉 База данных успешно создана!")