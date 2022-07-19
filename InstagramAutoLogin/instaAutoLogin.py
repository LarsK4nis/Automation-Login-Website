from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import requests 
import time

request = requests.get('https://instagram.com') # WEB PAGE TARGET Ex: https://instagram.com
configuration = yaml.full_load(open('dmInfo.yml')) # USER INFORMATION ACCOUNT.YML
usuario = configuration ['data_user']['user']
passwd = configuration ['data_user']['password']

driver = webdriver.Chrome() # DRIVER BROWSER CHOSEN 
driver.maximize_window()
time.sleep(2)
css1 = "body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm" # CSS selector used for "Accept Only Necesary Cookies"
css2 = "#loginForm > div > div:nth-child(3) > button > div"  # CSS selector used for "Login button" in Login Web

def login(url,username, username1, password, password1): 
   driver.get(url)
   driver.find_element(By.CSS_SELECTOR, css1).click()
   time.sleep(2)
   driver.find_element(By.NAME, username).send_keys(username1)
   driver.find_element(By.NAME, password).send_keys(password1)
   time.sleep(1)
   driver.find_element(By.CSS_SELECTOR, css2).click()


if(request.status_code == 200): # WEB PAGE TARGET COMPROBATION
   login ("https://instagram.com", "username", usuario, "password", passwd)
   