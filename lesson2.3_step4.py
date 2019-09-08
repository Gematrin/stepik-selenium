# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/alert_accept.html')
    driver.find_element_by_tag_name('button').click()
    driver.switch_to.alert.accept()
    y = calc(int(driver.find_element_by_id('input_value').text))
    driver.find_element_by_id('answer').send_keys(str(y))
    driver.find_element_by_class_name('btn-primary').click()
    sleep(30)
finally:
    driver.quit()
