import smtplib
import os
from email.mime.text import MIMEText

def main(args):
    email = args.get('email')
    status = args.get('status')

    if not email or not status:
        return {"body": "Error: 'email' and 'status' parameters are required.", "statusCode": 400}

    # MailSender SMTP credentials
    SMTP_SERVER = "smtp.mailersend.net" 
    SMTP_PORT = 587  
    SMTP_USERNAME = os.environ.get("SMTP_USERNAME")  
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")  

    # Email content
    subject = "Order Status Update"
    body = f"Thank you for ordering with us!\n\nYour order status is: {status}.\n\nBon apetite!"
    msg = MIMEText(body)
    msg["From"] = SMTP_USERNAME
    msg["To"] = email
    msg["Subject"] = subject

    try:
      # Connect to the SMTP server
      with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Authenticate
            server.sendmail(SMTP_USERNAME, email, msg.as_string())  # Send the email
      return {"body": "Email sent successfully.", "statusCode": 200}
    except Exception as e:
      return {"body": f"Error: {str(e)}", "statusCode": 500}

