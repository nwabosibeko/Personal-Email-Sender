import os
import ssl
import json
import smtplib
from pyfiglet import Figlet
from email.message import EmailMessage



the_pass = os.getenv("python_password") #the password to my account login (stored in my OS)

email_from = "smisosibeko@gmail.com" #immutable email used

message = EmailMessage() #building the email programmatically, with the subject, body, recepient and attachments.
def user_login():
    RED = '\033[31m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    fig = Figlet(font='slant')
    heading = fig.renderText("Nwabo's")
    heading2 = fig.renderText("Emailer")
    print(f"{RED}{heading}{RESET} {BLUE}{heading2}{RESET}")

    my_data = dict()

    if os.path.isfile("emailer_app/accounts.json"):
        print("Yes it does exist")
        with open("accounts.json", "r") as lsm:
            credentials = input("Welcome Mr ")


        
    else:
        print("No it does not, please register")
        my_data["name"] = input("Please enter your name: ")
        my_data["surname"] = input("PLease enter your surname: ")

        with open("accounts.json", "w") as f:
            json.dump(my_data, f)

    my_data = dict()
    print(my_data)

def generate_password(firstName, lastName):
    return ""

def userInput():
    user_login()
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