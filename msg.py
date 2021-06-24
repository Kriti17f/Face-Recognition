############################################################## Email ##############################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(name, pic):    
    sender = '<sender_email_add>'
    reciever = 'reciever_email_add'
    password = '<sender_password>'  

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    msg['From'] = sender
    msg['To'] = reciever
    msg['Subject'] = "Subject of the Mail"

    body = '''
    Hi,
    This is face of {} 
    '''
    # attach the body with the msg instance
    msg.attach(MIMEText(body.format(name), 'plain'))

    # open the file to be sent 
    filename = pic
    attachment = open(pic, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    # Send the message via our own SMTP server.
    message = msg.as_string()
    try:
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, reciever, message)
        s.quit()
        print("##############################")
        print("Successfully sent email!:)")
        print("##############################")

    except Exception:
        print("Error: unable to send email")
        s.quit()
        
########################################################### Whatsapp ###############################################################     
#pip install pywhatkit
import pywhatkit
from datetime import datetime

now = datetime.now()

def send_watsapp_msg(name):
    try:
        # sending message to reciever
        # using pywhatkit
        pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "Hi,{}\nWe have Successfully Completed Our Task".format(name), int(now.strftime("%H")), int(now.strftime("%M"))+2, 10)
        print("##############################")
        print("Successfully Sent!:)")
        print("##############################")

    except:
        print("An Unexpected Error!")
        

        
########################################################### AWS Instance ############################################################      
import os

def aws():
    try:
        os.system("terraform init")
        os.system("terraform apply -auto-approve")
        print("##############################")
        print("Successfully launched!:)")
        print("##############################")
    except:
        print("An Unexpected Error!")