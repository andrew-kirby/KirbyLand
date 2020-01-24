
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from DictReader import DictReader

class AlertEmailer:

    def __init__(self):
        self.senderEmail = None
        self.senderEmailPassword = None

    def loadCredentials(self):
        dictReader = DictReader()
        creds = dictReader.readDict('../emailcredentials')
        self.senderEmail = creds['email']
        self.senderEmailPassword = creds['password']


    def emailAlert(self, member, items):
        print('Sending an email alert...')

        # Set sender and recipient
        fromaddr = self.senderEmail
        toaddr = member['email']

        # Parse the items to get message content
        body = "Hello, " + member['name'] + ", we have detected food items you are looking for!\n" \
                + "\n" \
                + " ----- \n"

        for item in items:
            body = body + item.getAlertText() + "\n"

        body = body + " ----- \n"

        print(body)

        """
        # Compose message headers
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "MSU DINING ALERT"

        # Attach message body
        msg.attach(MIMEText(body, 'plain'))

        # Convert the object to a string to send via the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.senderEmail, self.senderEmailPassword)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        """