import smtplib
import os
from email.message import EmailMessage

HOST = 'smtp-mail.outlook.com'
PORT = 587
SENDER = os.environ.get('USER_EMAIL')
RECIPIENT = os.environ.get('USER_RECIPIENT')
PASSWORD = os.environ.get('USER_PASS')


class Email:
    def __init__(self, host, port, sender, recipient, password):
        self.host = host
        self.port = port
        self.sender = sender
        self.recipient = recipient
        self.password = password
        self.subject = input('Enter subject of the email: ').title()
        self.text = input('Type the content of your text: ')



    def send(self):
        msg = EmailMessage()
        msg.set_content(self.text)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.recipient
        with smtplib.SMTP(self.host, self.port) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()
            smtp_server.login(self.sender, self.password)
            smtp_server.send_message(msg)
            smtp_server.quit()
        print('Email message sent.')


email = Email(HOST, PORT, SENDER, RECIPIENT, PASSWORD)
email.send()