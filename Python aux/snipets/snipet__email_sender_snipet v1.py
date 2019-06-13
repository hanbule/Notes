import imaplib
import smtplib
from email.mime.text import MIMEText
from getpass         import getpass
from email.header    import Header
from smtplib         import SMTP_SSL
import email
#from gmail import Gmail
"""
execute in terminal to start local smtp server:
    python -m smtpd -n -c DebuggingServer localhost:1025
and conseqently:
    smtpObj = smtplib.SMTP('localhost', 1025)
"""


# for this to work, need to give permission for unauthorized applications access in gmail account settings
def email_notify_2(subject,message):
    sender = 'from_me@gmail.com'
    login_email, password = '...@mail.com', ''   #getpass('password')
    receivers = [login_email]

    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8') #subject
    msg['From'] = sender
    msg['To'] = ",".join(str(r) for r in receivers)


    s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    s.set_debuglevel(1)
    try:
        s.login(login_email, password)
        s.sendmail(login_email, receivers, msg.as_string())
    finally:
        s.quit()


def email_notify(subject,message):

    smtpObj = smtplib.SMTP('localhost')

    sender = '...@mail.com'
    receivers = ['...@mail.com']

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(str(r) for r in receivers)

    try:
        smtpObj.send_message(msg)
        print("Email sent successfully.")
    except smtplib.SMTPException:
        print("Unable to send email.")

    smtpObj.quit()

    return None


def exception_notify(error):

    error_message = 'Message: ' + " ".join( str(error).splitlines())
    error_doc = 'Doc: ' + str(error.__doc__)
    error_class = 'Class: ' + str(error.__class__)
    error_module = 'Module: ' + str(error.__module__)
    email_notify("ERROR: %s" % error_message, "%s\n%s\n%s\n%s" % (error_message, error_doc, error_class, error_module))

    return None

# try:
#     email_notify("SUCCESS: slicedw_scorecard creation finished","slicedw_scorecard table has been successfully created.")
# except Exception as e:
#     exception_notify(e)
#     sys.exit()







if __name__ == '__main__':
    email_notify_2('Test for selenium','Test for selenium')
    

