# 🎮 GamePlatform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-3.9-FF6384?logo=chartdotjs&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2ea44f)

**Игровая веб-платформа на Flask с тремя классическими играми, системой авторизации, рейтингов, административной панелью и социальными функциями.**

[Возможности](#-возможности) · [Стек](#-стек-технологий) · [Скриншоты](#-скриншоты) · [Установка](#-быстрый-старт) · [API](#-api-эндпоинты)

</div>

---

## 📖 О проекте

**GamePlatform** — учебный fullstack-проект, демонстрирующий навыки разработки веб-приложений на **Flask** с полноценной backend-логикой, базой данных **MySQL**, аутентификацией, разграничением прав и интерактивными играми на **JavaScript Canvas**.

Проект создан для портфолио и демонстрирует:

- 🏗 Проектирование реляционной БД (5 таблиц, связи 1:N и 1:1)
- 🔐 Аутентификацию и авторизацию с хешированием паролей
- 🎮 Интерактивные игры на чистом JavaScript + Canvas API
- 📊 Визуализацию данных через Chart.js
- 🎨 Адаптивный интерфейс на Bootstrap 5
- 🔒 Защиту от CSRF, XSS, SQL-инъекций

---

## ✨ Возможности

<table>
<tr>
<td width="50%" valign="top">

### 🔐 Аутентификация
- Регистрация и вход
- Хеширование паролей (`Werkzeug`)
- CSRF-защита всех форм
- Смена пароля
- Загрузка аватаров
- Удаление аккаунта

</td>
<td width="50%" valign="top">

### 👑 Роли и права
- **Пользователь** — игры, профиль, комментарии
- **Администратор** — управление пользователями, графики
- Декоратор `@admin_required`
- Защита последнего админа

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 Статистика
- Личная статистика по каждой игре
- Количество партий, рекорд, средний счёт
- Последние 5 результатов
- Серия заходов (**streak**)
- Глобальный **ТОП-5 рекордов**

</td>
<td width="50%" valign="top">

### 🛠 Админ-панель
- Сводная статистика
- Поиск и фильтрация пользователей
- Смена роли в один клик
- Удаление пользователей
- Графики: топ игроков + распределение игр

</td>
</tr>
</table>

---

## 🎮 Игры

<table>
<tr>
<th width="15%">Игра</th>
<th width="35%">Описание</th>
<th width="25%">Управление</th>
<th width="25%">Особенности</th>
</tr>
<tr>
<td align="center">
<strong>🧩 Судоку</strong>
</td>
<td>Классическая головоломка с числами. Доступны размеры <strong>4×4</strong> и <strong>6×6</strong>.</td>
<td>Ввод цифр с клавиатуры</td>
<td>Подсветка правильных/неправильных клеток, показ решения</td>
</tr>
<tr>
<td align="center">
<strong>🦖 Динозаврик</strong>
</td>
<td>Бесконечный раннер, вдохновлённый игрой из Chrome.</td>
<td><kbd>Space</kbd> — прыжок</td>
<td>Скорость растёт с очками, случайные препятствия</td>
</tr>
<tr>
<td align="center">
<strong>🟦 Тетрис</strong>
</td>
<td>Классическая головоломка с 7 фигурами.</td>
<td><kbd>←</kbd> <kbd>→</kbd> <kbd>↓</kbd> <kbd>↑</kbd></td>
<td>Уровни каждые 500 очков, пауза</td>
</tr>
</table>

---

## 🛠 Стек технологий

<div align="center">

|   **Backend**    | **Database** | **Frontend** |
|:----------------:|:------------:|:------------:|
|   Python 3.10+   | MySQL 8.0 | HTML5 |
|   Flask 2.3.3    | SQLAlchemy ORM | CSS3 |
|   Flask-Login    | PyMySQL | Bootstrap 5.3 |
|    Flask-WTF     | | Bootstrap Icons |
| Flask-SQLAlchemy | | JavaScript ES6+ |
|  python-dotenv   | | Chart.js |
|     Werkzeug     | | ChartDataLabels |

</div>

---

## 📸 Скриншоты

<div align="center">

### 🏠 Главная страница

<img src="screenshots/main_reg_auth.png" width="80%" alt="Главная до авторизации"/>

<img src="screenshots/main.png" width="80%" alt="Главная"/>

### 🔐 Регистрация

<img src="screenshots/register.png" width="60%" alt="Регистрация"/>

### 🎮 Список игр и рекорды

<img src="screenshots/main_games.png" width="80%" alt="Игры"/>

### 👤 Профиль пользователя

<img src="screenshots/profile.png" width="80%" alt="Профиль"/>

### 🕹 Игровой процесс

<table>
<tr>
<td><img src="screenshots/tetris_game.png" alt="Тетрис"/></td>
<td><img src="screenshots/sudo_game.png" alt="Судоку"/></td>
</tr>
<tr>
<td colspan="2" align="center"><img src="screenshots/dino_game.png" alt="Динозаврик"/></td>
</tr>
</table>

### 🛡 Админ-панель

<img src="screenshots/admin_panel.png" width="80%" alt="Админ-панель"/>

### ⚙️ Настройки и документация

<table>
<tr>
<td><img src="screenshots/settings.png" alt="Настройки"/></td>
<td><img src="screenshots/docs.png" alt="Документация"/></td>
</tr>
</table>

</div>

---

## 🚀 Быстрый старт

### 📋 Требования

| Компонент | Версия |
|-----------|--------|
| Python | 3.10+ |
| MySQL | 8.0+ (или MariaDB 10.5+) |
| pip + venv | — |

### 1️⃣ Клонировать репозиторий

```bash
git clone https://github.com/BlueLock-wasd/game-platform.git
cd game-platform
```

### 2️⃣ Создать виртуальное окружение

```bash
python -m venv venv
```

**Активация:**

<table>
<tr>
<th>ОС</th>
<th>Команда</th>
</tr>
<tr>
<td>🐧 Linux / 🍎 macOS</td>
<td><code>source venv/bin/activate</code></td>
</tr>
<tr>
<td>🪟 Windows (cmd)</td>
<td><code>venv\Scripts\activate</code></td>
</tr>
<tr>
<td>🪟 Windows (PowerShell)</td>
<td><code>.\venv\Scripts\Activate.ps1</code></td>
</tr>
</table>

### 3️⃣ Установить зависимости

```bash
pip install -r requirements.txt
```

### 4️⃣ Создать базу данных MySQL

```sql
CREATE DATABASE game_platform
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

### 5️⃣ Создать `.env` в корне проекта

```bash
cp .env.example .env
```

Затем отредактируйте `.env` — см. раздел [Переменные окружения](#-переменные-окружения).

**Сгенерировать `SECRET_KEY`:**

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 6️⃣ Инициализировать базу данных

<table>
<tr>
<th>ОС</th>
<th>Команда</th>
</tr>
<tr>
<td>🐧 Linux / 🍎 macOS</td>
<td><code>CONFIRM_DROP=yes python init_db.py</code></td>
</tr>
<tr>
<td>🪟 Windows (cmd)</td>
<td><code>set CONFIRM_DROP=yes && python init_db.py</code></td>
</tr>
<tr>
<td>🪟 Windows (PowerShell)</td>
<td><code>$env:CONFIRM_DROP="yes"; python init_db.py</code></td>
</tr>
</table>

> ⚠️ **Внимание!**
> `init_db.py` **удаляет все существующие таблицы** и создаёт их заново.
> **Не запускайте на продакшене.**

**Скрипт создаст:**

- 📁 Таблицы: `users`, `login_streaks`, `games`, `game_sessions`, `notes`
- 🎮 3 игры: Судоку, Динозаврик, Тетрис
- 👑 Админа из `ADMIN_USERNAME` / `ADMIN_PASSWORD`

### 7️⃣ Запустить приложение

```bash
python app.py
```

Откройте 👉 **http://127.0.0.1:5000**

---

## 🔐 Переменные окружения

Создайте `.env` в корне проекта на основе `.env.example`:

```env
# ===== Основное =====
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/game_platform
FLASK_DEBUG=True

# ===== Админ по умолчанию =====
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@game.ru
ADMIN_PASSWORD=admin123
```

| Переменная | Обязательна | Описание |
|:-----------|:-----------:|:---------|
| `SECRET_KEY` | ✅ | Ключ для подписи сессий и CSRF. Генерируйте через `secrets.token_hex(32)`. |
| `DATABASE_URL` | ✅ | URL подключения к БД. Формат: `mysql+pymysql://user:pass@host:port/db`. |
| `FLASK_DEBUG` | ❌ | `True` / `False`. Для прода — `False`. |
| `ADMIN_USERNAME` | ❌ | Логин админа. По умолчанию `admin`. |
| `ADMIN_EMAIL` | ❌ | Email админа. По умолчанию `admin@game.ru`. |
| `ADMIN_PASSWORD` | ❌ | Пароль админа. **Обязательно смените в проде!** |

### 🔒 Безопасность `.env`

- ❌ **Никогда** не коммитьте `.env` в Git
- ✅ Убедитесь, что `.env` добавлен в `.gitignore`
- ✅ Для команды создайте `.env.example` без реальных секретов

---

## 📁 Структура проекта

```
game-platform/
│
├── 📄 app.py                  # точка входа, маршруты, бизнес-логика
├── 📄 config.py               # конфигурация (читает .env)
├── 📄 models.py               # модели SQLAlchemy
├── 📄 forms.py                # Flask-WTF формы
├── 📄 init_db.py              # инициализация БД и создание админа
├── 📄 requirements.txt        # зависимости
├── 📄 .env                    # секреты (не коммитится)
├── 📄 .env.example            # шаблон .env
├── 📄 .gitignore
├── 📄 README.md
│
├── 📁 templates/
│   ├── base.html              # базовый шаблон (навбар, футер, flash)
│   ├── index.html             # главная страница
│   ├── login.html
│   ├── register.html
│   ├── profile.html           # профиль + статистика + комментарии
│   ├── settings.html          # смена пароля, аватара, удаление аккаунта
│   ├── games.html             # список игр + таблица рекордов
│   ├── docs.html              # документация проекта
│   ├── notes.html             # комментарии к профилю
│   │
│   ├── 📁 admin/
│   │   ├── dashboard.html     # админ-панель со статистикой и графиками
│   │   └── users.html         # управление пользователями
│   │
│   ├── 📁 games/
│   │   ├── sudoku.html        # игра Судоку
│   │   ├── dino.html          # игра Динозаврик
│   │   └── tetris.html        # игра Тетрис
│   │
│   └── 📁 errors/
│       ├── 403.html
│       ├── 404.html
│       └── 500.html
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── style.css          # кастомные стили
│   │
│   ├── 📁 images/
│   │   ├── logo.png           # логотип
│   │   ├── sudoku.png         # иконка Судоку
│   │   ├── phon_dino.png      # иконка Динозаврика
│   │   ├── tetris.png         # иконка Тетриса
│   │   └── dino.png           # спрайт персонажа
│   │
│   └── 📁 uploads/
│       ├── default.jpg        # дефолтный аватар
│       └── user_*.jpg         # загруженные аватары (не коммитятся)
│
└── 📁 screenshots/            # скриншоты для README
```

---

## 🌐 API эндпоинты

| Метод | URL | Доступ | Описание |
|:-----:|:----|:------:|:---------|
| `POST` | `/api/save_score` | 🔐 Авторизованные | Сохранить результат игры |
| `DELETE` | `/api/delete_note/<id>` | 🔐 Автор / 👑 Админ | Удалить комментарий |
| `DELETE` | `/api/delete_account` | 🔐 Авторизованные | Удалить аккаунт (кроме последнего админа) |
| `GET` | `/api/top_players` | 👑 Админ | Топ-5 игроков (JSON) |
| `GET` | `/api/game_stats` | 👑 Админ | Статистика по играм (JSON) |
| `GET` | `/api/top_scores` | 🌐 Все | Топ-5 рекордов (JSON) |

---

## 🔒 Безопасность

<table>
<tr>
<td width="50%" valign="top">

### ✅ Реализовано

- 🛡 **Хеширование паролей** — `werkzeug.security.generate_password_hash`
- 🛡 **CSRF-защита** — `flask_wtf.FlaskForm`
- 🛡 **SQL-инъекции** — SQLAlchemy ORM (параметризованные запросы)
- 🛡 **XSS-защита** — `escapeHtml`, `encodeURIComponent` в JS
- 🛡 **Права доступа** — `@login_required`, `@admin_required`
- 🛡 **Защита последнего админа** — нельзя удалить
- 🛡 **Санитизация имён** — `secure_filename`
- 🛡 **Расширения файлов** — whitelist

</td>
<td width="50%" valign="top">

### ⚠️ Для продакшена

- 🔑 Сменить `SECRET_KEY` и `ADMIN_PASSWORD`
- 🚫 Установить `FLASK_DEBUG=False`
- 🗄 Использовать **PostgreSQL** или отдельного MySQL-пользователя (не `root`)
- 🔐 Настроить **HTTPS** (Let's Encrypt)
- 🚦 Добавить **rate limiting** (`Flask-Limiter`)
- 📝 Настроить **логирование** (вместо `console.log`)
- 🚀 Использовать **gunicorn + nginx** вместо `flask run`

</td>
</tr>
</table>

---

## 🧪 Тестовые данные

После `init_db.py` создаётся администратор:

| Параметр | Значение |
|:---------|:---------|
| 🔑 Логин | Значение `ADMIN_USERNAME` из `.env` (по умолчанию `admin`) |
| 🔒 Пароль | Значение `ADMIN_PASSWORD` из `.env` (по умолчанию `admin123`) |

> ⚠️ **Обязательно смените пароль** через `/settings` после первого входа!

---

## 📄 Лицензия

<div align="center">

**MIT License** — см. [LICENSE](LICENSE)

Разработал ❤️ **Захар** ([@BlueLock-wasd](https://github.com/BlueLock-wasd))

⭐ Если проект был интересен — поставьте звезду!

</div>