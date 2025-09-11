import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='2da92aed']").text == "Игра престолов (сериал 2011-2019)"
    assert driver.find_element(By.CSS_SELECTOR, "div[data-tid='rating']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "div[data-tid='description']").is_displayed()

@allure.title("Поиск фильма по актеру")
@allure.description("Вводим в поисковую строку имя актера, переходим на страницу с актером")
@allure.severity("high")
def test_actors(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Павел Прилучный")
    driver.find_element(By.ID, "suggest-item-person-1681168").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='f22e0093']").text == "Павел Прилучный"
# Проверка что это страница актера
    assert "актер" in driver.title.lower() or "actor" in driver.title.lower()
    assert driver.find_element(By.CSS_SELECTOR, "div[data-tid='filmography']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "img[alt*='Павел Прилучный']").is_displayed()

@allure.title("Поиск фильма по символам")
@allure.description("Вводим в поисковую строку символы и проверяем сообщение об отсутствии результатов")
@allure.severity("normal")
def test_negative(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("!@#$%^&*()")
    assert driver.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

@allure.title("Поиск фильма по цифре")
@allure.description("Вводим в поисковую строку одну цыфру для поиска фильма")
@allure.severity("normal")
def test_search_by_digit(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("9")
    driver.find_element(By.ID, "suggest-item-film-84674").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "9 рота (2005)"
# Проверка что это страница фильма
    assert driver.find_element(By.CSS_SELECTOR, "div[data-tid='rating']").is_displayed()
    assert "2005" in driver.page_source  # Проверка года выпуска

@allure.title("Просмотр Топ-250 фильмов")
@allure.description("Проверка страницы Топ-250 фильмов")
@allure.severity("high")
def test_top250_movies(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.XPATH, "//a[contains(text(), 'Фильмы')]").click()
    #driver.find_element((By.XPATH, "//a[contains(text(), 'Топ-250') or contains(@href, 'top250')]")).click()
    # Клик по Топ-250
    top250_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'top250')]"))
    )
    top250_link.click()

    # Ожидание загрузки страницы Топ-250
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '250')]"))
    )

    # Проверки страницы Топ-250
    assert "250" in driver.title
    assert driver.find_element(By.XPATH, "//h1[contains(text(), '250')]").is_displayed()

    # Проверка что есть список фильмов
    movies_list = driver.find_elements(By.CSS_SELECTOR, ".styles_root__ti07r")
    assert len(movies_list) > 0
