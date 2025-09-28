from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin")

login_email = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
login_email.send_keys("hola0@gmail.com")
login_password = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
login_password.send_keys("Pruebas123")
login_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "auth-form__button")))
login_button.click()
profile_image = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "profile__image")))
profile_image.click()
img_url = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(((By.ID, "owner-avatar"))))
img_url.send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png")
popup_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//form[@name='edit-avatar']/button[text()='Save']")))
popup_button.click()
new_img= WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), 'style', "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"))

time.sleep(1)

driver.quit()