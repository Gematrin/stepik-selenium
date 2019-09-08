# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

import math
from selenium import webdriver
from time import sleep


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/math.html')
y = calc(int(driver.find_element_by_css_selector('#input_value').text))
driver.find_element_by_css_selector('#answer').send_keys(y)
driver.find_element_by_css_selector('#robotCheckbox').click()
driver.find_element_by_css_selector('#robotsRule').click()
driver.find_element_by_css_selector('.btn-default').click()
sleep(30)
driver.quit()
