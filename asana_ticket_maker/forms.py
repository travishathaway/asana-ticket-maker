from flask_wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, validators


class FeedbackForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=120)])
    title = StringField('Brief Description', [validators.Length(min=3)])
    description = TextAreaField('Full Description')
    recaptcha = RecaptchaField()
