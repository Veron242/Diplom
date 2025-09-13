from base_page import BasePage
from selenium.webdriver.common.by import By


class KinopoiskMainPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.NAME, "kp_query")
    SUGGESTION_ITEM = (By.ID, "suggest-item-{type}-{id}")
    RANDOM_MOVIE_BUTTON = (By.XPATH, "//button[@data-tid='f49ca51f']")
    EMPTY_SUGGEST = (By.XPATH, "//*[contains(@class, 'emptySuggest')]")

    def open(self):
        self.driver.get("https://www.kinopoisk.ru/")
        return self

    def search(self, query):
        self.send_keys(*self.SEARCH_INPUT, query)
        return self

    def select_suggestion(self, item_type, item_id):
        locator = (By.ID, f"suggest-item-{item_type}-{item_id}")
        self.click(*locator)
        return self

    def click_random_movie(self):
        self.click(*self.RANDOM_MOVIE_BUTTON)
        return self

    def get_empty_suggest_text(self):
        return self.get_text(*self.EMPTY_SUGGEST)
