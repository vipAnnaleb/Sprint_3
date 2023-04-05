from faker import Faker

from conftest import (webdriver_wait,
                      SITE_URL,
                      NAME,
                      INCORRECT_PASSWORD)

from locators import (Registration,
                      Login)

faker = Faker()


class TestRegistration:
    def test_register_new_user(self, driver):
        driver.get(SITE_URL + 'register')
        email = faker.email()
        print(email)
        driver.find_elements(*Registration.USERNAME_FIELD)[0].send_keys(NAME)
        driver.find_elements(*Registration.USERNAME_FIELD)[1].send_keys(email)
        password = faker.password()
        print(password)
        driver.find_element(*Registration.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Registration.CHECK_IN_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        current_url = driver.current_url
        assert current_url == SITE_URL + 'login'

    def test_register_new_user_with_bad_password(self, driver):
        driver.get(SITE_URL + 'register')
        email = faker.email()
        print(email)
        driver.find_elements(*Registration.USERNAME_FIELD)[0].send_keys(NAME)
        driver.find_elements(*Registration.USERNAME_FIELD)[1].send_keys(email)
        driver.find_element(*Registration.PASSWORD_FIELD).send_keys(INCORRECT_PASSWORD)
        driver.find_element(*Registration.CHECK_IN_BTN).click()
        check = driver.find_element(*Registration.INCORRECT_PASSWORD).text
        assert 'Некорректный пароль' == check
