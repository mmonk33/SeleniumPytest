import allure
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultLocators:
    FIRST_ITEM = (By.CSS_SELECTOR, 'li.serp-item.serp-item_card[data-cid="0"] .organic__url')
    FIRST_ITEM_LINK = (By.CSS_SELECTOR, 'li.serp-item.serp-item_card[data-cid="0"] a[href].Link_theme_outer b')


class Results(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_tab()

    def check_first_element_link(self) -> None:
        with allure.step("Проверить 1 ссылка ведет на сайт tensor.ru"):
            first_element_link = self.find_element(SearchResultLocators.FIRST_ITEM_LINK).text
            assert 'tensor.ru' == first_element_link

    def check_opened_link(self) -> None:
        with allure.step("Проверить 1 ссылка ведет на сайт tensor.ru"):
            self.click_to(SearchResultLocators.FIRST_ITEM)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            url = self.driver.current_url.replace('https:', '').replace('/', '')
            assert 'tensor.ru' == url
