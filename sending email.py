import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tony James'
email['to'] = 'tony135@gmail.com'
email['subject'] = 'Hurray!....that got works'
email.set_content('Its working man !!!!!!!!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('tony1351998@gmail.com','Blacksheep13*')
    smtp.send_message(email)
    print('all good boys')