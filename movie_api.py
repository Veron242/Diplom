from base_api import BaseAPI

class MovieAPI(BaseAPI):
    def search_movies(self, query, page=1, limit=10):
        """Поиск фильмов по названию"""
        endpoint = "/v1.4/movie/search"
        params = {
            "page": page,
            "limit": limit,
            "query": query
        }
        return self._get(endpoint, params).json()

    def get_movie_by_id(self, movie_id):
        """Получение фильма по ID"""
        endpoint = f"/v1.4/movie/{movie_id}"
        return self._get(endpoint).json()

    def get_movies_with_rating(self, rating_range="8-10", rating_type="imdb"):
        """Получение фильмов с определенным рейтингом"""
        endpoint = "/v1.4/movie"
        params = {f"rating.{rating_type}": rating_range}
        return self._get(endpoint, params).json()