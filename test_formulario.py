#Raúl Alfredo Veras Martínez
#2023-0646
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import os
import pyautogui  
import time  

# Función para iniciar el navegador
@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path='C:/Users/raula/OneDrive/Desktop/Tarea4/drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

# Función auxiliar para capturar capturas de pantalla completas
def capture_full_screenshot(driver, test_name):
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)  
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_full.png")
    
    # Capturar toda la pantalla
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f"Captura de pantalla completa guardada en: {screenshot_path}")

# Test para llenar el formulario
def test_form_submission(driver: WebDriver):
    test_name = "test_form_submission"
    try:
        # Abrir el formulario
        driver.get("file:///C:/Users/raula/OneDrive/Desktop/Tarea4/index.html")
        wait = WebDriverWait(driver, 10)

        # Llenar el formulario
        wait.until(EC.presence_of_element_located((By.ID, "name_input"))).send_keys("Juan Pérez")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "email_input"))).send_keys("juan@example.com")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "telephone_input"))).send_keys("543654757")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "subject_input"))).send_keys("Me gustaría hacer una pregunta")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "message_input"))).send_keys("Tengo una duda sobre el proyecto.")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "form_button"))).click()
        time.sleep(2)  

        # Verificar la alerta
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "Su mensaje" in alert_text, f"Error: El mensaje de éxito no es el esperado. Obtuvo: {alert_text}"

    except Exception as e:
        pytest.fail(f"Error en la prueba: {str(e)}")
    finally:
        capture_full_screenshot(driver, test_name)

# Test para validar error al ingresar caracteres no numéricos en el teléfono
def test_form_invalid_phone_number(driver: WebDriver):
    test_name = "test_form_invalid_phone_number"
    try:
        driver.get("file:///C:/Users/raula/OneDrive/Desktop/Tarea4/index.html")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located((By.ID, "name_input"))).send_keys("Juan Pérez")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "email_input"))).send_keys("juan@example.com")
        time.sleep(1)  

        # Llenar el formulario con datos no válidos (letras en lugar de números)
        wait.until(EC.presence_of_element_located((By.ID, "telephone_input"))).send_keys("hjbfgkjdfg")
        time.sleep(1)  

        # Esperar a que aparezca la alerta
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

        # Verificar que la alerta tenga el mensaje adecuado
        assert "Este campo solo permite números." in alert_text, \
            f"Error: El mensaje de alerta no es el esperado. Obtuvo: {alert_text}"

    except UnexpectedAlertPresentException as e:
        pytest.fail(f"Error inesperado de alerta: {str(e)}")
    except Exception as e:
        pytest.fail(f"Error en la prueba: {str(e)}")
    finally:
        capture_full_screenshot(driver, test_name)

# Test para verificar si aparece un alert cuando los campos están incompletos
def test_form_incomplete_fields(driver: WebDriver):
    test_name = "test_form_incomplete_fields"
    try:
        driver.get("file:///C:/Users/raula/OneDrive/Desktop/Tarea4/index.html")
        wait = WebDriverWait(driver, 10)

        # Dejar los campos por mitad y enviar el formulario

        wait.until(EC.presence_of_element_located((By.ID, "name_input"))).send_keys("Juan Pérez")
        time.sleep(1)  

        wait.until(EC.presence_of_element_located((By.ID, "email_input"))).send_keys("juan@example.com")
        time.sleep(1) 

        submit_button = wait.until(EC.presence_of_element_located((By.ID, "form_button")))
        time.sleep(1)  

        submit_button.click()
        time.sleep(2) 

        # Verificar el mensaje del alert
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert "Por favor, llene todos los campos antes de enviar el formulario." in alert_text, \
            f"Error: El mensaje de alerta no es el esperado. Obtuvo: {alert_text}"
        alert.accept()

    except Exception as e:
        pytest.fail(f"Error en la prueba: {str(e)}")
    finally:
        capture_full_screenshot(driver, test_name)
