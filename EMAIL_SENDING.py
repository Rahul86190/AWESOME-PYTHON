""" password must be generated from google settings . Go to your google settings (Manage Your google account) . Go to security option
 make sure your TWO STEP VERIFICATION is done .Then go through 'App password' and create a password for MAIL,  give name as you think.
copy that password and paste where password written """

import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('Sender_Email_address','password')      # put your mail at the place of 'Sender_Email_address' and receiver mail address at 'Receiver_Email_address;
server.sendmail('Sender_Email_address','Receiver_Email_address',    
                """SUBJECT:MAIL THROUGH PYTHON\n     
                Namaste SIR,\n
                NAME:RAHUL SAINI  \n
                BRANCH:My Branch is -> ARTIFICIAL INTELLIGENCE AND DATA SCIENCE\n
                COLLEGE:Arya College of Engineering\n
                COLLEGE CITY:JAIPIR RAJASTHAN""")   # details Edit according to you 
