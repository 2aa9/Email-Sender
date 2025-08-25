
### `send_email.py`
```python
import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    sender = "your_email@example.com"
    password = "your_password"  # Consider using app password for Gmail

    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("✅ Email sent!")

if __name__ == "__main__":
    to = input("Recipient: ")
    subject = input("Subject: ")
    body = input("Message: ")
    send_email(to, subject, body)
