import os
from email.message import EmailMessage
import ssl
import smtplib

the_pass = os.getenv("python_password")

if the_pass:
    print("The environment variable was set")
else:
    print("It isn't set")


