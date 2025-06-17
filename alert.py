import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SETTINGS

def send_email_alert(product_name,price,link):
    subject = f"!!PRICE DROP!! : {product_name}"
    body = f"{product_name}\n Price: {price}\n Link: {link}"
    
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SETTINGS["sender"]
    msg["To"] = EMAIL_SETTINGS["receiver"]
    msg["Subject"] = subject
    msg.attach(MIMEText(body,"plain"))
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SETTINGS["sender"], EMAIL_SETTINGS["app_password"])
            server.sendmail(EMAIL_SETTINGS["sender"],EMAIL_SETTINGS["receiver"], msg.as_string())
            print(" Email alert sent for",product_name)
    except Exception as e:
        print("Email alert failed" , e)