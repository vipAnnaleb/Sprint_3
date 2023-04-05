from conftest import (webdriver_wait,
                      SITE_URL,
                      TEST_LOGIN,
                      TEST_PASSWORD)

from locators import (Home,
                      Login,
                      ForgotPassword)


class TestLogin:
    def test_login_from_homepage_login_btn(self, driver):
        driver.get(SITE_URL)
        driver.find_element(*Home.ENTRY_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        driver.find_element(*Login.EMAIL_FIELD).send_keys(TEST_LOGIN)
        driver.find_element(*Login.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Login.SIGN_IN_BTN).click()
        webdriver_wait(driver, Home.PROFILE_BTN)
        check = driver.find_element(*Home.PROFILE_BTN).text
        assert check == 'Личный Кабинет'

    def test_login_from_profile_btn(self, driver):
        driver.get(SITE_URL)
        driver.find_element(*Home.PROFILE_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        driver.find_element(*Login.EMAIL_FIELD).send_keys(TEST_LOGIN)
        driver.find_element(*Login.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Login.SIGN_IN_BTN).click()
        webdriver_wait(driver, Home.PROFILE_BTN)
        check = driver.find_element(*Home.PROFILE_BTN).text
        assert check == 'Личный Кабинет'

    def test_login_from_register_page_login_btn(self, driver):
        driver.get(SITE_URL + 'register')
        driver.find_element(*Home.PROFILE_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        driver.find_element(*Login.EMAIL_FIELD).send_keys(TEST_LOGIN)
        driver.find_element(*Login.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Login.SIGN_IN_BTN).click()
        webdriver_wait(driver, Home.PROFILE_BTN)
        check = driver.find_element(*Home.PROFILE_BTN).text
        assert check == 'Личный Кабинет'

    def test_login_from_forgot_passport_page(self, driver):
        driver.get(SITE_URL + 'forgot-password')
        driver.find_element(*ForgotPassword.SIGN_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        driver.find_element(*Login.EMAIL_FIELD).send_keys(TEST_LOGIN)
        driver.find_element(*Login.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Login.SIGN_IN_BTN).click()
        webdriver_wait(driver, Home.PROFILE_BTN)
        check = driver.find_element(*Home.PROFILE_BTN).text
        assert check == 'Личный Кабинет'










