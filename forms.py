from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from config import Config
from models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[
            DataRequired(),
            Length(min=Config.USERNAME_MIN_LENGTH, max=Config.USERNAME_MAX_LENGTH)
        ]
    )
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Пароль',
        validators=[DataRequired(), Length(min=Config.PASSWORD_MIN_LENGTH)]
    )
    confirm = PasswordField(
        'Подтвердите пароль',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError(Config.MSG_USERNAME_TAKEN)

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(Config.MSG_EMAIL_TAKEN)


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Старый пароль', validators=[DataRequired()])
    new_password = PasswordField(
        'Новый пароль',
        validators=[DataRequired(), Length(min=Config.PASSWORD_MIN_LENGTH)]
    )
    confirm = PasswordField(
        'Подтвердите пароль',
        validators=[DataRequired(), EqualTo('new_password')]
    )
    submit = SubmitField('Сменить пароль')


class NoteForm(FlaskForm):
    content = TextAreaField(
        'Комментарий',
        validators=[DataRequired(), Length(max=Config.NOTE_MAX_LENGTH)]
    )
    submit = SubmitField('Оставить комментарий')