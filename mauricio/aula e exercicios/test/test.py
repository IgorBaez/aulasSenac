from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # mantém o navegador aberto

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
'   '
driver.get("https://www.google.com")
time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium tutorial")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
