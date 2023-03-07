from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd


website = 'https://www.adamchoi.co.uk/overs/detailed'

s = Service('/home/royfocker/Chrome_Driver/chromedriver')
driver = webdriver.Chrome(service= s)
#driver.maximize_window()
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

#Busqueda en listas desplegables.
dropdown = Select(driver.find_element(By.ID, 'country')) # busquedas en listas desplegables
dropdown.select_by_visible_text('Spain')

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []


for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text) #//tr/td[3]
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    #home = match.find_element(By.XPATH, './td[2]').text
    #home_team.append(home)
    #print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text) 

df = pd.DataFrame({'date':date, 'home_team':home_team, 'score':score, 'away_team':away_team})
df.to_csv('football.csv', index=False)
print(df)

#time.sleep(5) 