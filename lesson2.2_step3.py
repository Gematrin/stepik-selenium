# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/selects2.html')
    sum2 = int(driver.find_element_by_id('num1').text) + int(driver.find_element_by_id('num2').text)
    Select(driver.find_element_by_id('dropdown')).select_by_value(str(sum2))
    driver.find_element_by_class_name('btn-default').click()
    sleep(30)
finally:
    driver.quit()
