from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://kimetsu-no-yaiba-jut.su/seasons-1-episode-17")

skip_button = driver.find_element(By.CLASS_NAME, "fp-skip-screen fp-skip-screen__empty")
next_button = driver.find_element(By.CLASS_NAME, "btn w-full flex items-center justify-center gap-2")

print(skip_button)