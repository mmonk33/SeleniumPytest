import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import logging


class SearchLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, ".arrow__input.mini-suggest__input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".arrow__button")
    PICTURES_LINK = (By.CSS_SELECTOR, ".desktop-services__icon_images")
    SEARCH_FRAME = (By.CSS_SELECTOR, ".dzen-search-arrow-common__frame")
    SUGGEST = (By.CSS_SELECTOR, 'ul.mini-suggest__popup-content')


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.is_iframe_available(SearchLocators.SEARCH_FRAME)

    def enter_word(self, word: str) -> None:
        with allure.step(f"Ввести в поиск {word}"):
            _search = self.find_element(SearchLocators.SEARCH_FIELD)
            _search.click()
            _search.send_keys(word)

    def click_on_the_search_button(self) -> None:
        return self.find_element(SearchLocators.SEARCH_BUTTON, time=2).click()

    def press_enter(self) -> None:
        with allure.step("Нажать ENTER"):
            self.find_element(SearchLocators.SEARCH_FIELD, time=2).send_keys(Keys.ENTER)

    def check_suggestion_visible(self) -> None:
        with allure.step("Проверить, что появилась таблица с подсказками (suggest)"):
            try:
                _suggest = self.find_element(SearchLocators.SUGGEST)
                WebDriverWait(self.driver, 10).until(EC.visibility_of(_suggest))
                assert _suggest.is_displayed()
            except AssertionError as err:
                logging.exception("Assertion Failed. Suggestion is not visible")
                raise err

    def check_search_field_is_present(self):
        with allure.step("Проверить наличия поля поиска"):
            _search_field = self.find_element(SearchLocators.SEARCH_FIELD)
            assert _search_field.is_displayed()

    def check_pictures_link_is_visible(self):
        with allure.step("Проверить, что ссылка «Картинки» присутствует на странице"):
            _picture_link = self.find_element(SearchLocators.PICTURES_LINK)
            assert _picture_link.is_displayed()
