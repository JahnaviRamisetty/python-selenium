from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import Chromedriver
from webdrivermanager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(Chromedriver().install()))
driver.get("https://www.google.com")