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

# driver.find_element(By.XPATH, "//div[1]/section/div[2]/a[1]/div[2]").click()
# print(driver.find_element(By.XPATH, "//div[2]/div/div/div/h4").text)
elem = driver.find_element(By.TAG_NAME, "body")
counter = 0
while counter < 10:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    counter += 1

list1 = driver.find_elements(By.XPATH, "//div[4]/div[1]/section/div[2]/a")
list_url = [link.get_attribute("href") for link in list1]
print(list_url)
print(list1)
print(len(list_url))
time.sleep(80)
# if __name__ == '__main__':
