from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome()

driver.get("https://docs.python.org/3/tutorial/index.html")

# sel = driver.find_element(By.ID,"language_select")
# select = Select(sel)
# select.select_by_index(8)

text = driver.find_element(By.TAG_NAME, 'h1')
s = text.get_attribute("innerHTML")
index = s.find("<a")
s = s[:index]

print(s)
print()
# p = driver.find_element(By.TAG_NAME, 'p')
# print(p.get_attribute("innerHTML"))

href = driver.find_element(By.ID,"the-python-tutorial")
href = href.find_element(By.CSS_SELECTOR,"#the-python-tutorial > p")
print(href.get_attribute("innerHTML"))

# google = driver.find_element(By.NAME, 'q')
# google.send_keys("class")
# google.submit()