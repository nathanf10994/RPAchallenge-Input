import pandas as pd 
import time 
import os
 
from selenium import webdriver 
from selenium.webdriver.common.by import By 

url = 'https://www.rpachallenge.com/'

chrome = webdriver.Chrome() 
chrome.get(url)

time.sleep(5)
chrome.find_element (By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a').click()

time.sleep(2)
file_name = 'C:\\Users\\nataf\\Downloads\\challenge.xlsx'
dataframe = pd.read_excel(file_name)

chrome.find_element (By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click() 

for index, row in dataframe.iterrows(): 
    
    time.sleep(1) 
    
    input_first_name= chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]')
    input_last_name = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]')
    input_company_name = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]') 
    input_role_in_company = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]') 
    input_address = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]') 
    input_email = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]') 
    input_phone_number = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]') 
    
    input_first_name.send_keys(row['First Name']) 
    input_last_name.send_keys(row['Last Name ']) 
    input_company_name.send_keys(row['Company Name']) 
    input_role_in_company.send_keys(row['Role in Company']) 
    input_address.send_keys(row['Address']) 
    input_email.send_keys(row['Email']) 
    input_phone_number.send_keys(row['Phone Number']) 
    
    chrome.find_element (By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click() 

status = chrome.find_element(By.CLASS_NAME, 'message2')
txt = status.text

with open('status.txt','w', encoding='utf-8') as file:
    file.write(txt)

os.remove(file_name)

file_address = 'status.txt'
os.system(f'start {file_address}')