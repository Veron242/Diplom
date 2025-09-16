from base_page import BasePage
from selenium.webdriver.common.by import By


class MoviePage(BasePage):
    MOVIE_TITLE = (By.CSS_SELECTOR, "span[data-tid='2da92aed']")
    MOVIE_TITLE_ALT = (By.CSS_SELECTOR, "span[data-tid='75209b22']")
    RANDOM_BUTTON = (By.CLASS_NAME, "randomMovieButton")

    def get_movie_title(self):
        try:
            return self.get_text(*self.MOVIE_TITLE)
        except:
            return self.get_text(*self.MOVIE_TITLE_ALT)

    def is_random_button_displayed(self):
        return self.is_displayed(*self.RANDOM_BUTTON)

    def get_current_url(self):
        return self.driver.current_url