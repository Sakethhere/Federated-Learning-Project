import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders

FROM_EMAIL = "saketha1299@gmail.com"
FROM_EMAIL_PASSWORD = "mchsowbjxjfqgnvw"

def send_email(recipient_email, ss,subject, message):
    with open(ss, 'rb') as f:
        img_data = f.read()
    
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    image = MIMEImage(img_data, name='ss.jpg')
    msg.attach(image)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)
            server.sendmail(FROM_EMAIL, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")


# sender_email = 'your_email@gmail.com'
# sender_password = 'your_password'
# recipient_email = 'recipient_email@example.com'
# subject = 'Test Email'
# message = 'This is a test email.'
# send_email('warrior.prince652002@gmail.com', subject, message)


