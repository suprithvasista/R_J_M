import secrets
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(secrets.choice(characters) for i in range(length))
    return otp

def send_otp(email, otp):
    # Email server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'vasistatech19@gmail.com'
    sender_password = 'qtpx qokx sgvi tggk'

    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = 'Your OTP Code'

    body = f'Your OTP code is {otp}'
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, email, text)
        server.quit()
        print(f'OTP sent successfully to {email}')
    except Exception as e:
        print(f'Failed to send OTP: {e}')

# Example usage
def verify_otp(input_otp, actual_otp):
    return input_otp == actual_otp

def feed_back_mail(text):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'vasistatech19@gmail.com'
    sender_password = 'qtpx qokx sgvi tggk'

    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = 'vasistatech19@gmail.com'
    message['Subject'] = 'Feed back'

    body = text
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, 'vasistatech19@gmail.com', text)
        server.quit()
    except Exception as e:
        print(f'Failed to send OTP: {e}')

