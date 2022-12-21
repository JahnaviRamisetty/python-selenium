from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="C:\edgedriver_win64\msedgedriver.exe")

time.sleep(3)
driver.get("https://www.java.com/en/")

time.sleep(3)
driver.minimize_window()
print(driver.title)
time.sleep(3)

driver.close()
