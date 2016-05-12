from flask_wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, validators
from wtforms.fields.html5 import EmailField


class FeedbackForm(Form):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    title = StringField('Brief Description', [validators.DataRequired(), ])
    description = TextAreaField('Full Description')
    recaptcha = RecaptchaField()
    def get_email_data(self):
        """
        Formats a submitted form entry to include the email and description
        as the email body and the title field as the subject.
        :return: Tuple, (Subject, Body)
        """
        msg_body = 'Reported by: {}\n'.format(self.email.data)
        msg_body += self.description.data
        return self.title.data, msg_body
