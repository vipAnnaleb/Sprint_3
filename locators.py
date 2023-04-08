from selenium.webdriver.common.by import By


class Home:
    ENTRY_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт
    PROFILE_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")  # ссылка на профиль
    CONSTRACTOR_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")  # заголовок Соберите бургер
    # блок с ингредиентами, чтобы проверить, активен ли он
    INGREDIENT_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/span")
    BREAD_TAB = (By.XPATH, "//span[text()='Булки']")  # раздел Булки
    BREAD_TITLE = (By.XPATH, "//h2[text()='Булки']")  # заголовок Булки
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")  # раздел Соусы
    SAUCE_TITLE = (By.XPATH, "//h2[text()='Соусы']")  # заголовок Соусы
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")  # раздел Начинки
    FILLING_FIELD = (By.XPATH, "//h2[text()='Начинки']")  # заголовок Начинки


class Login:
    ENTRY_TITLE = (By.XPATH, "//h2[text()='Вход']")  # заголовок Вход
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # поле ввода мэйла
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # поля ввода пароля
    SIGN_IN_BTN = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти


class ForgotPassword:
    SIGN_BTN = (By.CSS_SELECTOR, "a[href='/login']")  # кнопка Войти


class Registration:
    USERNAME_FIELD = (By.XPATH, "//input[@name='name']")  # поле ввода логина и имя пользователя
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # поля ввода пароля
    CHECK_IN_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")  # конпка Зарегистрироваться
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")  # поле для проверки неправильного пароля
    SIGN_IN_LINK = (By.XPATH, "//a[text()='Войти']")  # ссылка Войти


class Profile:
    SIGN_IN_BTN = (By.CLASS_NAME, "Account_text__fZAIn text text_type_main-default")
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")  # кнопка для перехода в Конструктор
    LOGOUT_BTN = (By.CLASS_NAME, "Account_button__14Yp3 text text_type_main-medium text_color_inactive")  # кнопка для выхода из аккаунта





