import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("http://64.227.170.125:8080/icleaf/")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("icadmin")
driver.find_element(By.ID,"password").send_keys("admin@icleaf")
driver.find_element(By.CLASS_NAME,"login_btn").click()
shadow_host_element = driver.find_element(By.XPATH,"//div[@id='root']")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host_element)

print("Loggedin successfully")