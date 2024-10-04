from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from properties import (NETGEAR_AUTH_URL,
                        BLOCK_IP_ADDRESSES)

def block(block_state=True):
    access = "block" if block_state else "allow"

    allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, access))
    )
    allow_button.click()

    # Prompt for alert, accept
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

options = Options()
options.add_experimental_option("detach", True)

# Open portal using driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(NETGEAR_AUTH_URL)
driver.maximize_window()

# Find devices and block
for address in BLOCK_IP_ADDRESSES:
    xpath = f"//tr[@name='row_rules' and .//span[@name='rule_ip' and text()='{address}']]//input[@name='checkbox']"

    try:
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        checkbox.click()

    except TimeoutException:
        print(f"Could not find the checkbox for IP or may not exist.")

block(block_state=False)
    