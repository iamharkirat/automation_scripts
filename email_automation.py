import pandas as pd
import smtplib
import imghdr
from email.message import EmailMessage

e=pd.read_excel(r'C:\Users\Z\Desktop\Python\Coursera\Scripts\Email.xlsx')
emails=e['Emails'].values

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('iamharkirat@gmail.com', 'BT2178309')
# server.send_message(msg)
with open(r'C:\Users\Z\Desktop\Python\Coursera\Scripts\sSvyJR0-lancia-wallpapers.jpg', 'rb') as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name

for email in emails:
    msg=EmailMessage()
    msg['Subject']='This is the Subject Line'
    msg['From']='iamharkirat@gmail.com'
    msg['To']=email
    msg.set_content('This is the Msg. PFA below an image.')

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    server.send_message(msg)
    print(email + ": Done")
