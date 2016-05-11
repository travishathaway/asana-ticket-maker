import smtplib
from email.mime.text import MIMEText

from . import settings


def send_mail(subject, body, to_email=settings.ASANA_PROJECT_EMAIL):
    """
    Send an email with subject and body to the requested recipient

    :param to_email: String, recipient of the email
    :param subject: String, subject of the email
    :param body: String, body of the email (plain text)
    """
    # Set up connection to the server
    server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    server.starttls()
    server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)

    # Create the Message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = settings.SMTP_USER
    msg['To'] = to_email

    # Send Email
    server.send_message(msg, settings.SMTP_USER, settings.ASANA_PROJECT_EMAIL)

    # Close connection
    server.quit()
