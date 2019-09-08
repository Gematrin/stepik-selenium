# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент - картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x(сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

import math
from selenium import webdriver
from time import sleep


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    y = calc(int(driver.find_element_by_id('treasure').get_attribute('valuex')))
    driver.find_element_by_id('answer').send_keys(y)
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_css_selector('.btn-default').click()
    sleep(30)
finally:
    driver.quit()
