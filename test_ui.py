import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(50)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Входим на страницу фильма, выбираем фильм")
@allure.severity("high")
def test_search(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Игра престолов")
    driver.find_element(By.ID, "suggest-item-tvSeries-464963").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='2da92aed']").text == "Игра престолов"
    assert "464963" in driver.current_url

@allure.title("Поиск фильма по актеру")
@allure.description("Вводим в поисковую строку имя актера, переходим на страницу с актером")
@allure.severity("high")
def test_actors(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Павел Прилучный")
    driver.find_element(By.ID, "suggest-item-person-1681168").click()
    assert driver.find_element(By.TAG_NAME, "h1").text == "Павел Прилучный"
# Проверка что это страница актера
    assert "1681168" in driver.current_url

@allure.title("Поиск фильма по символам")
@allure.description("Вводим в поисковую строку символы и проверяем сообщение об отсутствии результатов")
@allure.severity("normal")
def test_negative(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("!@#$%^&*()")
    assert driver.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

@allure.title("Поиск фильма по цифре")
@allure.description("Вводим в поисковую строку одну цифру для поиска фильма")
@allure.severity("normal")
def test_search_by_digit(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("9")
    driver.find_element(By.ID, "suggest-item-film-84674").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "9 рота (2005)"
# Проверка что это страница фильма
    assert "84674" in driver.current_url

@allure.title("Рандомный фильм")
@allure.description("Выбор случайного фильма через кнопку Случайный фильм")
@allure.severity("normal")
def test_random_movie(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.XPATH, "//button[@data-tid='f49ca51f']").click()
    assert driver.find_element(By.CLASS_NAME, "randomMovieButton").is_displayed()
    assert "chance" in driver.current_url

