import smtplib
import sys
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
user = "saikiranreddygangidi@gmail.com"
pwd = "saikiran0074"
driver = webdriver.Chrome()
driver.get("http://www.facebook.com")

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.save_screenshot(r'C:\Users\Anirudh\Desktop\new1.png')
loc =r'C:\Users\Anirudh\Desktop\Book1.xlsx'
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
fromaddr = "saikiranreddygangidi@gmail.com"
toaddr = str(sheet.cell_value(1, 2))
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "facebook profile"
  
# string to store the body of the mail 
body = "facebook profile"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "new1.png"
attachment = open(r"C:\Users\Anirudh\Desktop\new1.png", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "saikiran0074") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr,toaddr , text) 
  
# terminating the session 
s.quit() 


print('sent')

