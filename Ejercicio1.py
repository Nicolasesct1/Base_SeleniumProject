from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys("hola0@gmail.com")
# Buscar el campo Contraseña y rellenarlo
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "password")))
driver.find_element(By.ID, "password").send_keys("Pruebas123")
# Buscar el botón Iniciar sesión y hacer clic en él
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "auth-form__button")))
driver.find_element(By.CLASS_NAME, "auth-form__button").click()
# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
# Comprobar que la URL actual es 'https://around-v1.nm.tripleten-services.com/'
assert driver.current_url == "https://around-v1.nm.tripleten-services.com/"
#Desplazar el elemento a la vista
footer = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "footer")))
driver.execute_script("arguments[0].scrollIntoView();", footer)
# Comprobar que el pie de página contiene el string 'Around' (el completo es @2020 Around)
assert 'Around' in footer.text

# Usar el objeto de espera para obtener el botón de cierre de sesión y verificar que su texto sea 'Cerrar sesión'
logout = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__logout"))).text
assert logout == 'Cerrar sesión'





driver.quit()