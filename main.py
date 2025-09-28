from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome() #Crea un objeto con configuracion por default
#chrome_options = webdriver.ChromeOptions() # Crea un objeto para la configuración
#chrome_options.add_argument('--headless') # Ejecuta el navegador desde la terminal sin una interfaz gráfica
#chrome_options.add_argument('--window-size=1500,780') # Ajusta el tamaño de la ventana por pixeles "y" x "z" pixeles
#driver = webdriver.Chrome(options=chrome_options) # Crea un controlador y pasa la configuración de los ajustes establecidos
#driver.maximize_window()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(1) #poner siempre despues el time sleep antes del link para poder buscar objetos
#current_url = driver.current_url #obtener la url actual en el que estoy
#assert current_url == 'https://www.google.com/' #comprueba la totalidad de la url
#assert '/signin' in current_url #comprueba solo una parte de la url como si fuera solo google
button_login = driver.find_element(By.CSS_SELECTOR, ".auth-form__button") #Buscar el titulo
print("Login from tittle:", button_login.text) #imprimir el texto
button_login.click() #hacer clic en el boton con el titulo inciar sesion
time.sleep(1) #cada vez que esperas un cambio en la automatizacion (ventana) es bueno poner un time sleep, no un cambio en consola

email = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Correo electrónico']") #Busca el placeholder como atributo
assert email.get_attribute("placeholder") == "Correo electrónico"
password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Contraseña']")
assert password.get_attribute("placeholder") == "Contraseña"

email.send_keys("Hola") #escribe en el campo email
time.sleep(1)
email.clear() #borra el campo email
time.sleep(1)
email.send_keys("Chao")
time.sleep(1)

driver.quit() #cierra la pagina