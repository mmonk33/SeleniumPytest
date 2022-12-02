import logging
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class PicturesPageLocators:
    PIC_FIRST = (By.CSS_SELECTOR, ".serp-item_pos_0")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input__control.mini-suggest__input")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next")
    BUTTON_PREV = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    OPENED_IMAGE = (By.CSS_SELECTOR, '.MMImage-Origin')
    PICTURES_FIRST_ITEM = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")


class PicturesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(driver.window_handles[-1])

    def check_is_image_opened(self) -> None:
        with allure.step("Проверить открыта ли картинка"):
            self.find_element(PicturesPageLocators.OPENED_IMAGE)

    def check_category_name_in_search_field(self) -> None:
        with allure.step("Проверить, что название категории отображается в поле поиска"):
            category = self.find_element(PicturesPageLocators.PICTURES_FIRST_ITEM).get_attribute("data-grid-text")
            assert category == self.find_element(PicturesPageLocators.SEARCH_FIELD).get_attribute("value")

    def get_image_src(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".MMImage-Origin").get_attribute("src")

    def check_current_picture_after_changing(self, picture_before_changing: str):
        try:
            with allure.step("Проверить, что картинка осталась той же"):
                picture_after_changing = self.get_image_src()
                assert picture_after_changing == picture_before_changing
        except AssertionError as Assertion:
            logging.exception("Assertion Failed. Image src is not equal!")
            raise Assertion

    def click_to_next_button(self) -> None:
        with allure.step("Нажать вперед"):
            self.find_element(PicturesPageLocators.BUTTON_NEXT, time=2).click()

    def click_to_previous_button(self) -> None:
        with allure.step("Нажать назад"):
            self.find_element(PicturesPageLocators.BUTTON_PREV, time=2).click()

    def check_picture_change(self, picture_before_changing: str) -> None:
        try:
            with allure.step("Проверить, что картинка сменилась"):
                picture_after_changing = self.get_image_src()
                assert picture_after_changing != picture_before_changing
        except AssertionError as Assertion:
            logging.exception("Assertion Failed. Image src is not equal!")
            raise Assertion

