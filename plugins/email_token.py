import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp = 'mail.gowishway.com'
def send_token_via_email(recipient_email):
    try:
        sender_email, sender_password = ('admin@gowishway.com','4=_w}SQ],_#y')
        # Generate a random token
        token = ''.join(random.choices('0123456789128934832100567', k=6))
        # Set up the email message content
        message = f"Your token is: {token}"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Token Verification"
        msg.attach(MIMEText(message, 'plain'))
        # Connect to the email server and send the email message
        server = smtplib.SMTP(smtp, 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        return True
    except Exception as e :
        return False 

# Example usage
def check_email_status(recipient_email):
    print('Sending...')
    if send_token_via_email(recipient_email):
        return "Email delivery successfully."
    else:
        return "Email delivery failed."


