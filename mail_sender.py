import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

userEmail = input('Enter your email to send the mails: ')
userPassword = input('Enter your email password: ')
def createPasswordTxt(passFileName):
    with open(passFileName, 'w') as file:
        file.write(userPassword)
passFileName = "mail_sender/password.txt"
createPasswordTxt(passFileName)


loggedIn = False
try:
    with open(passFileName, 'r') as f:
        password = f.read()
    server.login(userEmail, password)
    print('Logged in successfully...')
    loggedIn = True

except smtplib.SMTPAuthenticationError:
    print('Log in failed, check the email and password!')
    server.quit()

def sendingEmailProccess():
    subject = input('Enter the Subject title: ')
    userMessage = input('Enter your message: ')
    def createMessageTxt(msgFileName):
        with open(msgFileName, 'w') as f:
            f.write(userMessage)
    msgFileName = 'mail_sender/message.txt'
    createMessageTxt(msgFileName)
    with open(msgFileName, 'r') as f:
        message = f.read()

    emailAmount = int(input('Enter the amount of emails you want to send: '))
    emailArray = []

    for i in range(emailAmount):
        emailTargets = input('Enter email ' + str(i + 1) + ' : ')
        emailArray.append(emailTargets)

    msg = MIMEMultipart()
    msg['From'] = userEmail
    recipient = emailArray
    msg['To'] = ', '.join(recipient)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server.sendmail(msg['From'], recipient, text)

    print('The email(s) are sent successfully...')
if loggedIn:
    sendingEmailProccess()

    userChoice = input('Press F to quit, or A to continue...')
    if (userChoice.lower() == 'f'):
        server.quit()
    elif (userChoice.lower() == 'a'):
        sendingEmailProccess()

