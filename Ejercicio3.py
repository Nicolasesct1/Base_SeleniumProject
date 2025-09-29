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
#Recuerda que xpath es el unico que encuentra por texto
title_before = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[@class='card__title' and text()='Colosseum']")))
add_new_pub_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "profile__add-button")))
add_new_pub_button.click()
# Generar número aleatorio de 3 dígitos
random_digits = random.randint(100, 999)
# Crear el nuevo título
new_title = "Tokio" + str(random_digits)
new_popup_title = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "place-name")))
new_popup_title.send_keys(new_title)
new_popup_link = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "place-link")))
new_popup_link.send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")
popup_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//form[@name='new-card']/button[text()='Save']")))
popup_button.click()
delete_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']")))
#Usar la variable new_title en {} ya que es dinamico
new_title_pub = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, f"//h2[@class='card__title' and text()='{new_title}']")))
time.sleep(10)
assert new_title_pub.text == new_title
cards_before= len(driver.find_elements(By.CSS_SELECTOR, "li.places__item.card"))
print(cards_before)
delete_button.click()
time.sleep(10)
# Lambda es una funcion temporal para contar las cartas anteriores -1 en este caso (asi comprueba la eliminacion)
WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "li.places__item.card")) == cards_before - 1)
time.sleep(10)
cards_after= len(driver.find_elements(By.CSS_SELECTOR, "li.places__item.card"))
print(cards_after)
assert cards_after == cards_before - 1


driver.quit()