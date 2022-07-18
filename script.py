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
css1 = ".login .content .form-actions .btn-success" # CSS selector used for button in Login Fonction

def login(url,username, username1, password, password1): 
   driver.get(url)
   driver.find_element(By.NAME, username).send_keys(username1)
   driver.find_element(By.NAME, password).send_keys(password1)
   driver.find_element(By.LINK_TEXT,'Entrar').click()


if(request.status_code == 200): # WEB PAGE TARGET COMPROBATION
   login ("WEBPAGE__CHOSEN", "usernameOrEmailAddress", usuario, "password", passwd)
   time.sleep(3)

   #driver.find_element(By.LINK_TEXT,'Usuario').click() # LOOK FOR ELEMENT USER AND CLICK ON IT
   #objetivoFichar = driver.find_element(By.LINK_TEXT,'Fichar').click() # DESPLEGAMOS DROP-MENU, LOCALIZAMOS FICHAR Y CLICKAMOS
   #time.sleep(3)
   #fichajeEstrella = driver.find_element(By.LINK_TEXT,'FICHAR').click() # CLICKAMOS EN FICHAR Y SE ACTUALIZA ESTADO PAR/IMPAR
   
