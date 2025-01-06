import os
from email.message import EmailMessage
import ssl
import smtplib

the_pass = os.getenv("python_password")

if the_pass:
    print("The environment variable was set")
else:
    print("It isn't set")


email_from = "smisosibeko@gmail.com"
email_to = "nwabosibeko17@gmail.com"

email_sub = 'Trying this programm out.'
email_body = """
This application is in it's first stage as I will create a GUI going forth
"""
message = EmailMessage()
