import datetime as dt
import time
import smtplib

def send_email():
    email_user = 'venkat6879ta@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, '8142147997ven@@@@')

    #EMAIL
    message = 'Hello Baby i miss you a lot!'
    server.sendmail(email_user, email_user, message)
    server.quit()

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')

first_email_time = dt.datetime(2020,3,14,3,0,0) # set your sending time in UTC
interval = dt.timedelta(minutes=2*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval