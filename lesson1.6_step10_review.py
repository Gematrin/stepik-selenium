import time
from selenium import webdriver

website = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(website)


input1 = browser.find_element_by_css_selector('.form-control.first[required]')
input1.send_keys("Vladyslav")
input2 = browser.find_element_by_css_selector('.form-control.second[required]')
input2.send_keys("Bilenko")
input3 = browser.find_element_by_css_selector('.form-control.third[required]')
input3.send_keys("vlad@gmail.com")

button = browser.find_element_by_css_selector('button.btn')
button.click()
time.sleep(2)

welcome_text = browser.find_element_by_tag_name('h1')
record_welcome_text = welcome_text.text

assert "Поздравляем! Вы успешно зарегистировались!" == record_welcome_text
time.sleep(2)

browser.quit()
