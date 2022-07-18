from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import requests 
import time

request = requests.get('WEBPAGE__CHOSEN') # WEB PAGE TARGET
configuration = yaml.full_load(open('YOUR_INFORMATION.yml')) # USER INFORMATION ACCOUNT .YML
usuario = configuration ['data_user']['user']
passwd = configuration ['data_user']['password']

driver = webdriver.Chrome() # BROWSER CHOSEN 
css1 = ".login .content .form-actions .btn-success" # CSS selector used for button 

def login(url,usernameOrEmailAddress, username, password, password1): 
   driver.get(url)
   driver.find_element(By.NAME, usernameOrEmailAddress).send_keys(username)
   driver.find_element(By.NAME, password).send_keys(password1)
   driver.find_element(By.CSS_SELECTOR, css1).click()


if(request.status_code == 200):
   login ("http://90.174.128.109:8080/SymphonyWeb/Account/Login", "usernameOrEmailAddress", usuario, "password", passwd)
   time.sleep(3)
   driver.find_element(By.LINK_TEXT,'Usuario').click() # LOOK FOR ELEMENT USER AND CLICK ON IT
   objetivoFichar = driver.find_element(By.LINK_TEXT,'Fichar').click() # DESPLEGAMOS DROP-MENU, LOCALIZAMOS FICHAR Y CLICKAMOS
   time.sleep(3)
   fichajeEstrella = driver.find_element(By.LINK_TEXT,'FICHAR').click() # CLICKAMOS EN FICHAR Y SE ACTUALIZA ESTADO PAR/IMPAR
   print ("He llegao 2")
   
