# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
import math
from time import sleep


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/execute_script.html')
    y = calc(int(driver.find_element_by_id('input_value').text))
    field = driver.find_element_by_id('answer')
    driver.execute_script('arguments[0].scrollIntoView(true);', field)
    field.send_keys(str(y))
    robot_checkbox = driver.find_element_by_id('robotCheckbox')
    driver.execute_script('arguments[0].scrollIntoView(true);', robot_checkbox)
    robot_checkbox.click()
    robot_radio = driver.find_element_by_id('robotsRule')
    driver.execute_script('arguments[0].scrollIntoView(true);', robot_radio)
    robot_radio.click()
    submit_button = driver.find_element_by_class_name('btn-primary')
    driver.execute_script('arguments[0].scrollIntoView(true);', submit_button)
    submit_button.click()
    sleep(30)
finally:
    driver.quit()
