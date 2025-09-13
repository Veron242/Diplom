import pytest
import allure
from selenium import webdriver
from kinopoisk_main_page import KinopoiskMainPage
from movie_page import MoviePage
from actor_page import ActorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(50)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return KinopoiskMainPage(driver).open()


@pytest.fixture
def movie_page(driver):
    return MoviePage(driver)


@pytest.fixture
def actor_page(driver):
    return ActorPage(driver)


@allure.title("Поиск фильма по названию")
@allure.description("Входим на страницу фильма, выбираем фильм")
@allure.severity("high")
def test_search(main_page, movie_page):
    (main_page
     .search("Игра престолов")
     .select_suggestion("tvSeries", "464963"))

    assert movie_page.get_movie_title() == "Игра престолов"
    assert "464963" in movie_page.get_current_url()


@allure.title("Поиск фильма по актеру")
@allure.description("Вводим в поисковую строку имя актера, переходим на страницу с актером")
@allure.severity("high")
def test_actors(main_page, actor_page):
    (main_page
     .search("Павел Прилучный")
     .select_suggestion("person", "1681168"))

    assert actor_page.get_actor_name() == "Павел Прилучный"
    assert "1681168" in actor_page.get_current_url()


@allure.title("Поиск фильма по символам")
@allure.description("Вводим в поисковую строку символы и проверяем сообщение об отсутствии результатов")
@allure.severity("normal")
def test_negative(main_page):
    main_page.search("!@#$%")

    assert main_page.get_empty_suggest_text() == "По вашему запросу ничего не найдено"


@allure.title("Поиск фильма по цифре")
@allure.description("Вводим в поисковую строку одну цифру для поиска фильма")
@allure.severity("normal")
def test_search_by_digit(main_page, movie_page):
    (main_page
     .search("9")
     .select_suggestion("film", "84674"))

    assert movie_page.get_movie_title() == "9 рота (2005)"
    assert "84674" in movie_page.get_current_url()


@allure.title("Рандомный фильм")
@allure.description("Выбор случайного фильма через кнопку Случайный фильм")
@allure.severity("normal")
def test_random_movie(main_page, movie_page):
    main_page.click_random_movie()

    assert movie_page.is_random_button_displayed()
    assert "chance" in movie_page.get_current_url()
