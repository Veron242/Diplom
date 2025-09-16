from base_page import BasePage
from selenium.webdriver.common.by import By


class ActorPage(BasePage):
    ACTOR_NAME = (By.TAG_NAME, "h1")

    def get_actor_name(self):
        return self.get_text(*self.ACTOR_NAME)

    def get_current_url(self):
        return self.driver.current_url
