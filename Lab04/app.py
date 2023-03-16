from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.nycu.edu.tw/")
driver.maximize_window()
myLink = driver.find_element(By.PARTIAL_LINK_TEXT, '新聞')
myLink.click()
elems = driver.find_elements(By.XPATH,"//a[@href]")
href = driver.find_element(By.CLASS_NAME,"su-post")
href = href.find_element(By.CSS_SELECTOR,".su-post > a")
href.click()
text = driver.find_element(By.TAG_NAME, 'h1')
print(text.get_attribute("innerHTML"))
texts = driver.find_elements(By.TAG_NAME, 'p')
for  text in texts:
    print(text.get_attribute("innerHTML"))
driver.switch_to.new_window('tab')
driver.get("https://www.google.com")
google = driver.find_element(By.NAME, 'q')
google.send_keys("311551126")
google.submit()
google = driver.find_elements(By.CLASS_NAME, 'DKV0Md')[1]
print(google.text)
driver.close()


