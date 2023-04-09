# -*- coding: utf-8 -*-

from wtforms import Form, StringField, validators
from wtforms.validators import InputRequired


class LoginForm(Form):
    username = StringField('Username:', validators=[InputRequired(), validators.Length(min=1, max=30)])
    password = StringField('Password:', validators=[InputRequired(), validators.Length(min=1, max=30)])
    email = StringField('Email:', validators=[validators.optional(), validators.Length(min=0, max=50)])
