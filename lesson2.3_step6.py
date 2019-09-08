# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    driver.find_element_by_class_name('trollface').click()
    driver.switch_to.window(driver.window_handles[1])
    y = calc(int(driver.find_element_by_id('input_value').text))
    driver.find_element_by_id('answer').send_keys(str(y))
    driver.find_element_by_class_name('btn-primary').click()
    sleep(30)
finally:
    driver.quit()
