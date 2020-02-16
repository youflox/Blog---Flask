from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), length(min=2, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember me :')
    submit = SubmitField('Login')

