from flask import Flask, render_template, redirect, request

from . import settings
from .forms import FeedbackForm


app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
app.config['RECAPTCHA_PUBLIC_KEY'] = settings.RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = settings.RECAPTCHA_PRIVATE_KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Serve the bug request form as well as send the input to
    Asana via our gmail address.

    :param request:
    :return:
    """
    form = FeedbackForm()
    if request.method == 'POST' and form.validate():
        return redirect('/thank-you')
    return render_template('index.html', form=form)


@app.route('/thank-you')
def thank_you():
    """
    Simple page that displays a thank you message

    :param request:
    :return:
    """
    return 'Thank you!'