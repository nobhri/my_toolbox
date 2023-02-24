import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
load_dotenv()# read .env file and set environment variables

os.environ['WDM_LOCAL'] = '1'# Download webdriver to project root.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# start browser and acces web form
TARGET_URL = os.getenv("TARGET_URL")# read environment variables. I made google form for test
driver.get(TARGET_URL)
title = driver.title
assert title == "test form"
sleep(5)

# input text field
nickname_xpath = r'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.implicitly_wait(0.5)
text_box = driver.find_element(by=By.XPATH , value=nickname_xpath)
text_box.send_keys("Fuzzgoro")
sleep(5)

# input radio
radio_01_xpath = r'//*[@id="i9"]/div[3]/div'
radio_01 = driver.find_element(by=By.XPATH , value=radio_01_xpath)
radio_01.click()
sleep(5)


# input checkbox
checkbox_01_xpath = r'//*[@id="i35"]/div[2]'
checkbox_01 = driver.find_element(by=By.XPATH , value=checkbox_01_xpath)
checkbox_01.click()
sleep(5)

# input pulldown
pulldown_open_xpath = r'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]'
pulldown_open = driver.find_element(by=By.XPATH , value=pulldown_open_xpath)
pulldown_open.click()
sleep(3)
pulldown_ans_yes_xpath = r'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span'
pulldown_ans_yes = driver.find_element(by=By.XPATH , value=pulldown_ans_yes_xpath)
pulldown_ans_yes.click()
sleep(3)

# click submit button
submit_button_xpath= r'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
submit_button = driver.find_element(by=By.XPATH , value=submit_button_xpath)
submit_button.click()
sleep(5)


driver.quit()

print("Succeeded!")