import smtplib
from email.message import EmailMessage


def send_email_alert(changes):

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    recipient_email = "receiver@gmail.com"

    message = EmailMessage()

    message["Subject"] = "File Integrity Alert"
    message["From"] = sender_email
    message["To"] = recipient_email

    body = []

    for file in changes["modified"]:
        body.append(f"Modified: {file}")

    for file in changes["new"]:
        body.append(f"New File: {file}")

    for file in changes["deleted"]:
        body.append(f"Deleted: {file}")

    message.set_content("\n".join(body))

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender_email,
            sender_password
        )

        smtp.send_message(message)
