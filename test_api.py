import requests
import allure

key = ""

@allure.title("Поиск фильма по названию")
@allure.description("Ввод названия фильма")
@allure.severity("critical")
def test_by_name():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
        }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query={Один дома}",
                            headers=HEADERS)
    assert response.status_code == 200

@allure.title("Поиск фильма по ID")
@allure.description("Ввод ID")
@allure.severity("critical")
def test_by_movie_id():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/8124", headers=HEADERS)
    assert response.status_code == 200

@allure.title("Получить список фильмов с рейтингом выше 8")
@allure.description("Фильтрация фильмов по рейтингу выше 8")
@allure.severity("critical")
def test_movies_with_high_rating():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie?rating.imdb=8-10", headers = HEADERS)
    assert response.status_code == 200

@allure.title("Получить список возможных жанров")
@allure.description("Вывод возможных жанров")
@allure.severity("normal")
def test_possible_genres():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
    }
    response = requests.get("https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=genres.name", headers = HEADERS)
    assert response.status_code == 200

@allure.title("Поиск по ID актера")
@allure.description("Поиск по вводу ID актера")
@allure.severity("normal")
def test_search_movies_by_actor_id():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/person/1681168", headers = HEADERS)
    assert response.status_code == 200