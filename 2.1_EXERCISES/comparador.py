#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

url = 'https://www.amazon.es/'
browser.get(url)

timeout = 10

try:
    myElem = browser.find_element(By.ID, 'sp-cc-accept').click()
except:
    print("Timeout")

busqueda = browser.find_element(By.ID, 'twotabsearchtextbox')
busqueda.send_keys('Logitech G915')
busqueda.send_keys(Keys.ENTER)

time.sleep(2)
results = browser.find_elements(By.CLASS_NAME, 'sg-col-inner')

print("")
print("-----Consultar 'Logitech G915' en Amazon -------")
print("")

for result in results:
	if "result" not in result.text:
		try:
			result_name = result.find_element(By.CLASS_NAME, 'a-text-normal')
			if ('Logitech G915 LIGHTSPEED' in result_name.text):
			    precio = result.find_element(By.CLASS_NAME, 'a-price-whole')	
			    if ('199' in precio.text): 
			        print("")
			        print("Es recomana comprar el següent producte:")
			        print("")
			        print(result_name.text)
			        print("")
			        print("Amb el seguent preu: " + precio.text + " €")
		except:
			pass
	#if ('Logitech G915' in result_name):
print("")		
browser.close()
browser.quit()		




# https://unipython.com/navegando-con-selenium/
# https://stackoverflow.com/questions/1629053/typing-the-enter-return-key-in-selenium
