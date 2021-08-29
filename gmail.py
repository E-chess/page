import smtplib
import os
from email.message import EmailMessage

Gmail_Adress = os.environ['GMAIL_ADRESS']

Gmail_Passwoard = os.environ['GMAIL_PASSWOARD']



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login(Gmail_Adress, Gmail_Passwoard)
    email = EmailMessage()
    email['From'] = Gmail_Adress
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)