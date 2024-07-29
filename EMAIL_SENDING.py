# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Define the sender and receiver email addresses
# sender_email = "rabni6392@gmail.com"
# receiver_email = "rahulsaini132005@gmail.com"
# password = "7014nisha86190rahul"

# # Create the email subject and body
# subject = "Test Email from Python"
# body = "This is a test email sent from Python!"

# # Create the email message
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject

# # Attach the body to the email
# msg.attach(MIMEText(body, 'plain'))

# # Set up the SMTP server
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()  # Enable TLS encryption
# server.login(sender_email, password)  # Log in to the email account

# # Send the email
# text = msg.as_string()
# server.sendmail(sender_email, receiver_email, text)

# # Disconnect from the SMTP server
# server.quit()

# print("Email sent successfully!")


import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('rahulsaini132005@gmail.com','halw icyd ffdo zogo')
server.sendmail('rahulsaini132005@gmail.com','nishakumarisuman21@gmail.com',
                """SUBJECT:MAIL THROUGH PYTHON\n
                Namaste sir,\n
                NAME:RAHUL SAINI \n
                BRANCH:AI AND DS\n
                COLLEGE:ARYA COLLEGE OF ENGINEERING\n
                COLLEGE CITY:JAIPUR,RAJASTHAN""")