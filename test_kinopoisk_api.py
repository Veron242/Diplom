import allure
from movie_api import MovieAPI
from metadata_api import MetadataAPI

movie_api = MovieAPI(api_key="CH5EBJX-8BR4F9T-NAEDG5V-YVWHHTA")
metadata_api = MetadataAPI(api_key="CH5EBJX-8BR4F9T-NAEDG5V-YVWHHTA")


@allure.title("Поиск фильма по названию")
@allure.description("Ввод названия фильма 'Один дома'")
@allure.severity("critical")
def test_by_name():
    response_body = movie_api.search_movies("Один дома")

    # Проверка структуры ответа
    assert "docs" in response_body
    assert len(response_body["docs"]) > 0

    # Проверка конкретных значений
    first_movie = response_body["docs"][0]
    assert first_movie["name"] == "Один дома"
    assert first_movie["year"] == 1990


@allure.title("Поиск фильма по ID")
@allure.description("Ввод ID фильма 8124 (Один дома)")
@allure.severity("critical")
def test_by_movie_id():
    response_body = movie_api.get_movie_by_id(8124)

    # Проверка конкретных значений
    assert response_body["name"] == "Один дома"
    assert response_body["rating"]["kp"] >= 8.0


@allure.title("Получить список фильмов с рейтингом выше 8")
@allure.description("Фильтрация фильмов по рейтингу выше 8")
@allure.severity("critical")
def test_movies_with_high_rating():
    response_body = movie_api.get_movies_with_rating("8-10", "imdb")

    # Проверка что фильмы имеют высокий рейтинг
    assert response_body["docs"][0]["rating"]["imdb"] >= 8.0


@allure.title("Получить список возможных жанров")
@allure.description("Вывод возможных жанров")
@allure.severity("normal")
def test_possible_genres():
    response_body = metadata_api.get_possible_genres()

    # Проверка наличия ожидаемых жанров
    genres = [genre["name"] for genre in response_body]
    assert "комедия" in genres
    assert "драма" in genres


@allure.title("Поиск по ID актера")
@allure.description("Поиск по вводу ID актера Павел Прилучный")
@allure.severity("normal")
def test_search_movies_by_actor_id():
    response_body = metadata_api.get_person_by_id(1681168)

    # Проверка данных актера
    assert response_body["name"] == "Павел Прилучный"
