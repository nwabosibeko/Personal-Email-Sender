import os
from email.message import EmailMessage
import ssl
import smtplib


#Greeting  into the application...



the_pass = os.getenv("python_password") #the password to my account login (stored in my OS)


email_from = "smisosibeko@gmail.com"


email_to = input("Enter the email of the recepient: ")
email_sub = input("Subject: ")
email_body = input("Body: ")

message = EmailMessage()

message['From'] = email_from
message['To'] = email_to
message['Subject'] = email_sub
message.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as sm:
    sm.login(email_from, the_pass)
    sm.sendmail(email_from, email_to, message.as_string())