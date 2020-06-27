import smtplib
content ='hai this is saikiran reddy'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('saikiranreddygangidi@gmail.com','saikiran0074')
mail.sendmail('saikiranreddygangidi@gmail.com','saikiranreddygangidi@gmail.com',content)
mail.close()
print('sent')
