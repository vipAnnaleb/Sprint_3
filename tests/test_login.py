from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    def test_login_button(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').click()
        WebDriverWait(driver, 3)
        driver.quit()





