from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin")

login_email = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
login_email.send_keys("hola0@gmail.com")
login_password = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
login_password.send_keys("Pruebas123")
login_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "auth-form__button")))
login_button.click()

# Buscar las tarjetas y desplazarla a la vista
element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "places__list")))
#argument [0] es el element
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.quit()