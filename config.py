import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # ===== Основное =====
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('1', 'true', 'yes')
    TOP_LIMIT = 5

    # ===== Роли =====
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'

    # ===== Время =====
    DATE_DISPLAY_FORMAT = '%d.%m.%Y'

    # ===== Пути =====
    UPLOAD_SUBFOLDER = 'uploads'
    AVATAR_URL_PREFIX = 'uploads'   # если аватар хранится как 'uploads/xxx.png'

    # ===== Расширения =====
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    ALLOWED_IMAGE_SUFFIXES = tuple(f'.{ext}' for ext in ALLOWED_IMAGE_EXTENSIONS)

    # ===== Тексты сообщений =====
    MSG_ACCESS_DENIED = 'Доступ запрещен'
    MSG_LOGIN_SUCCESS = 'Вы успешно вошли!'
    MSG_LOGIN_FAILED = 'Неверное имя или пароль'
    MSG_LOGIN_REQUIRED = 'Пожалуйста, войдите для доступа к этой странице'
    MSG_REGISTER_SUCCESS = 'Регистрация успешна! Теперь войдите'
    MSG_NOTE_ADDED = 'Комментарий добавлен'
    MSG_PASSWORD_CHANGED = 'Пароль успешно изменен'
    MSG_PASSWORD_WRONG = 'Неверный старый пароль'
    MSG_ROLE_CHANGED = 'Роль пользователя {username} изменена'
    MSG_USER_DELETED = 'Пользователь {username} удален'
    MSG_FILE_NOT_SELECTED = 'Файл не выбран'
    MSG_AVATAR_UPDATED = 'Аватар обновлен'
    MSG_INVALID_FORMAT = 'Недопустимый формат файла'
    MSG_LOGOUT = 'Вы вышли из системы'
    MSG_NEVER = 'Никогда'
    MSG_NO_RIGHTS = 'Нет прав'
    MSG_NO_DATA = 'Нет данных'
    MSG_GAME_NOT_SPECIFIED = 'Не указана игра'
    MSG_GAME_NOT_FOUND = 'Игра "{game}" не найдена'
    MSG_DB_ERROR = 'Ошибка базы данных'
    MSG_SCORE_SAVED = 'Результат сохранён!'
    MSG_LAST_ADMIN = 'Нельзя удалить последнего администратора'

