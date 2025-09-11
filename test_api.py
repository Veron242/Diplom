import requests
import allure
import pytest

key = ""

@allure.title("Поиск фильма по названию")
@allure.description("Ввод названия фильма 'Один дома'")
@allure.severity("critical")
def test_by_name():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
        }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=Один дома",
                            headers=HEADERS)
    assert response.status_code == 200
    response_body = response.json()
# Проверка структуры ответа
    assert "docs" in response_body
    assert len(response_body["docs"]) > 0
# Проверка конкретных значений из тела ответа
    first_movie = response_body["docs"][0]
    assert first_movie["name"] == "Один дома"  # Проверка названия
    assert first_movie["year"] == 1990  # Проверка года выпуска

@allure.title("Поиск фильма по ID")
@allure.description("Ввод ID фильма 8124 ('Один дома')")
@allure.severity("critical")
def test_by_movie_id():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/8124", headers=HEADERS)
    assert response.status_code == 200
    assert response_body
    response_body = response.json()

# Проверка конкретных значений
    assert response_body["name"] == "Один дома"
    assert response_body["rating"]["kp"] >= 8.0  # Проверка рейтинга Кинопоиска

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
    response_body = response.json()

# Проверка что фильмы имеют высокий рейтинг
    assert len(response_body["docs"]) > 0
    for movie in response_body["docs"]:
        assert movie["rating"]["kp"] >= 8.0  # Проверка рейтинга для каждого фильма


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
    response_body = response.json()

# Проверка наличия ожидаемых жанров
    genres = [genre["name"] for genre in response_body]
    assert "комедия" in genres  # Проверка наличия жанра
    assert "драма" in genres    # Проверка наличия жанра

@allure.title("Поиск по ID актера")
@allure.description("Поиск по вводу ID актера Павел Прилучный")
@allure.severity("normal")
def test_search_movies_by_actor_id():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": key
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/person/1681168", headers = HEADERS)
    assert response.status_code == 200
    response_body = response.json()

# Проверка данных актера
    assert response_body["name"] == "Павел Прилучный"