import smtplib, ssl
import os
from email.mime.message import MIMEMessage


def send_email(sender, message, subject, send_method="TLS"):
    receiver = "mkappdevtester@gmail.com"
    host = "smtp.gmail.com"
    gmail_user = "mkappdevtester@gmail.com"
    gmail_pwd = str(os.getenv("python_email_pwd")).replace(" ", "")
    send_method = "TLS".upper() # TLS | SSL

    message = f"""\
Subject: {subject}

From: {sender}
Topic: {subject}

{message}
"""

    if send_method == "TLS":
        port = 587

        svr = smtplib.SMTP(host, port)
        svr.starttls()
        svr.login(gmail_user, gmail_pwd)
        svr.sendmail(gmail_user, gmail_user, message.encode("utf8"))

    if send_method == "SSL":
        port = 465
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(gmail_user, gmail_pwd)
            server.sendmail(gmail_user, receiver, message.encode("utf8"))



if __name__ == "__main__":
    # For testing the function directly

    local_msg = """\
This message was sent via the function call, plus injected message.

Bye
From the tester.
"""
    send_email(sender="mkappdevtester@gmail.com", message=local_msg, subject="This is a test")

    print("Email sent from send_email.py (locally called).")