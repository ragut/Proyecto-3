import os
import smtplib
from email.mime.text import MIMEText

def prompt(prompt):
    return raw_input(prompt).strip()

class MailController():

    def sendMail(self, to_email, name):
        ms = """
        Hello, """+name+"""

        Your video is already Available on the company's site.
        Thank you for your participation!"""

        msg = MIMEText(ms)

        msg['to'] = to_email
        msg['from'] = 'raulguti90@gmail.com'
        msg['subject'] = 'Your video have been processed'

        smtp_server = os.environ["smtp_host"]
        smtp_username = os.environ["smtp_user"]
        smtp_password = os.environ["smtp_password"]
        smtp_port = os.environ["smtp_port"]
        smtp_do_tls = True

        server = smtplib.SMTP(
            host=smtp_server,
            port=smtp_port,
            timeout=10
        )
        server.set_debuglevel(10)
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['from'], [to_email], msg.as_string())
        server.quit()


