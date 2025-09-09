import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Входим на страницу фильма, выбираем фильм")
@allure.severity("high")
def test_search(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Игра")
    driver.find_element(By.ID, "suggest-item-tvSeries-464963").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='f8463833']").text == "Игра престолов (2011)"

@allure.title("Поиск фильма по актеру")
@allure.description("Вводим в поисковую строку имя актера, переходим на стрницу с актером для выбора фильмов с ним")
@allure.severity("high")
def test_actors(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Павел Прилучный")
    driver.find_element(By.ID, "suggest-item-person-1681168").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='f22e0093']").text == "Павел Прилучный"

@allure.title("Поиск фильма по символам")
@allure.description("Вводим в поисковую строку символы и проверяем сообщение об отсутствии результатов")
@allure.severity("normal")
def test_negative(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("!@#$%^&*()")
    assert driver.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

@allure.title("Просмотр Топ-250 фильмов")
@allure.description("Переходим на страницу фильмов с высоким рейтингом")
@allure.severity("high")
def test_top250_movies(driver):
        driver.get("https://www.kinopoisk.ru/lists/top250/")
        driver.find_element()
        assert driver.find_element()


#@allure.title("Чтение отзывов о фильме")
#@allure.description("Переходим на страницу фильма с отзывами")
#@allure.severity("normal")
#def test_movie_reviews(driver):