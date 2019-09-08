# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from time import sleep
from os import path

driver = webdriver.Chrome()
try:
    current_dir = path.abspath(path.dirname(__file__))
    file_path = path.join(current_dir, 'file.txt')
    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element_by_name('firstname').send_keys('name')
    driver.find_element_by_name('lastname').send_keys('surname')
    driver.find_element_by_name('email').send_keys('mail@plr.net')
    driver.find_element_by_name('file').send_keys(file_path)
    driver.find_element_by_class_name('btn-primary').click()
    sleep(30)
finally:
    driver.quit()
