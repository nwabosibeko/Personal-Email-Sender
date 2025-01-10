import os
from email.message import EmailMessage
import ssl
import smtplib


#Greeting  into the application...



the_pass = os.getenv("python_password") #the password to my account login (stored in my OS)

email_from = "smisosibeko@gmail.com" #immutable email used

message = EmailMessage() #building the email programmatically, with the subject, body, recepient and attachments.


def userInput():

    email_to = input("Enter the email of the recepient: ")
    email_sub = input("Subject: ")
    email_body = input("Body: ")

    return email_to, email_sub, email_body

def construct_send_email(recepient, subject, bod):

    message['From'] = email_from
    message['To'] = recepient
    message['Subject'] = subject
    message.set_content(bod)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as sm:
        sm.login(email_from, the_pass)
        sm.sendmail(email_from, recepient, message.as_string())


if __name__ == "__main__":
    to, sub, body = userInput()
    construct_send_email(to, sub, body)