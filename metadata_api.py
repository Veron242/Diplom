from base_api import BaseAPI


class MetadataAPI(BaseAPI):
    def get_possible_genres(self):
        """Получение списка возможных жанров"""
        endpoint = "/v1/movie/possible-values-by-field"
        params = {"field": "genres.name"}
        return self._get(endpoint, params).json()

    def get_person_by_id(self, person_id):
        """Получение информации о персоне по ID"""
        endpoint = f"/v1.4/person/{person_id}"
        return self._get(endpoint).json()
