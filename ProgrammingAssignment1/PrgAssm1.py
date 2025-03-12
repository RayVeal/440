# Ramon Veal
# Programming assignment 1
# 10/16/23
# cmsc 440

import smtplib
import getpass

def send_email():
    sender_email = input("Enter your email address: ")
    
    password = getpass.getpass("Enter your email password: ")

    recipient_email = input("Enter the recipient's email address: ")

    subject = input("Enter the email subject: ")
    
    body = input("Enter the email body: ")

    # Compose the email message
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to the SMTP server
        # server = smtplib.SMTP('smtp.ethereal.email', 587)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message)

        print("Successfully sent email")
        
    except Exception:    
        print("Error: unable to send email")  
        
    finally:
        # End session
        server.quit()


if __name__ == "__main__":
    send_email()
