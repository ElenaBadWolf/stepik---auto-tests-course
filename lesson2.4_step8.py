from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


try:

    browser= webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.execute_script("window.scrollBy(0, 100);")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()
    browser.execute_script("window.scrollBy(0, 400);")



    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()

finally:
    time.sleep(15)
    browser.quit()
