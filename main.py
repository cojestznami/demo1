import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://www.google.pl")
driver.maximize_window()
driver.find_element(By.ID, "W0wltc").click()
driver.find_element(By.NAME, "q").send_keys("wakacje", Keys.ENTER)
driver.find_element(By.XPATH, "//a[contains(@href,'www.wakacje.pl')]").click()
driver.find_element(By.XPATH, "//button[text()='AKCEPTUJĘ I PRZECHODZĘ DO SERWISU']").click()
driver.find_element(By.XPATH, "//input[@value='Dowolnie']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Wpisz kierunek lub hotel']").send_keys("Bieszczady", Keys.ENTER)
driver.find_element(By.XPATH, "//div[1]/div/div[1]/ul/li[2]/label").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/footer/button").click()
time.sleep(90)
# if __name__ == '__main__':
