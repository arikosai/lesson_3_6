from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_button_add_to_basket(browser):
    browser.get(link)

    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "There is no button"
    

