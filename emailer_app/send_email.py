import os
from email.message import EmailMessage
import ssl
import smtplib

the_pass = os.getenv("python_password")



email_from = "smisosibeko@gmail.com"
email_to = "nwabosibeko17@gmail.com"

email_sub = 'Trying this programm out.'
email_body = """
This application is in it's first stage as I will create a GUI going forth
"""
message = EmailMessage()

message['From'] = email_from
message['To'] = email_to
message['Subject'] = email_sub
message.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as sm:
    sm.login(email_from, the_pass)
    sm.sendmail(email_from, email_to, message.as_string())