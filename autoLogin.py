from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import requests 
import time

request = requests.get('WEBPAGE__CHOSEN') # WEB PAGE TARGET Ex: https://instagram.com
configuration = yaml.full_load(open('YOUR_INFORMATION.yml')) # USER INFORMATION ACCOUNT .YML
usuario = configuration ['data_user']['user']
passwd = configuration ['data_user']['password']

driver = webdriver.Chrome() # DRIVER BROWSER CHOSEN 

def login(url,username, username1, password, password1): 
   driver.get(url) # LOAD WEB PAGE ON THE DRIVER 
   driver.find_element(By.NAME, username).send_keys(username1) #LOCATE USER FIELD AND "WRITE" YOUR YML USERNAME INFO
   driver.find_element(By.NAME, password).send_keys(password1) #LOCATE PASSWORD FIELD AND "WRITE" YOUR YML PASSWORD INFO
   driver.find_element(By.LINK_TEXT,'BUTTON_NAME').click() # IF THE BUTTON IS NOT LOCATED BY LINK_TEXT TRY OTHERS METHODS LISTED IN DOCUMENTATION (By Module Info)


if(request.status_code == 200): # WEB PAGE TARGET COMPROBATION
   login ("WEBPAGE__CHOSEN", "username", usuario, "password", passwd)
   time.sleep(3)
