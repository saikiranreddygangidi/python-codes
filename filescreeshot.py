'''import subprocess, os

if os.name == 'nt': # For Windows
 os.startfile('C:/Users/Anirudh/Desktop/new1.png')'''
from selenium import webdriver
import time
from PIL import Image
driver = webdriver.Chrome()
driver.get('C:/Users/Anirudh/Desktop/DL1.pdf')
time.sleep(5)
driver.save_screenshot('C:/Users/Anirudh/Desktop/new1.png')
driver.quit()

