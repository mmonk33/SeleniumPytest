from Pages.BasePage import BasePage
from Pages.MainPage import SearchLocators, SearchPage
from Pages.PicturesPage import PicturesPage, PicturesPageLocators
from Pages.ResultPage import Results


def test_yandex_search(browser):
    base = BasePage(browser)
    base.go_to_site('yandex.ru')
    search_page = SearchPage(browser)
    search_page.check_search_field_is_present()
    search_page.enter_word("Тензор")
    search_page.check_suggestion_visible()
    search_page.press_enter()
    results = Results(browser)
    results.check_first_element_link()
    results.check_opened_link()


def test_yandex_search_picture(browser):
    base = BasePage(browser)
    base.go_to_site('yandex.ru')
    main_page = SearchPage(browser)
    main_page.click_to(SearchLocators.SEARCH_FIELD)
    main_page.check_pictures_link_is_visible()
    main_page.click_to(SearchLocators.PICTURES_LINK)
    pictures_page = PicturesPage(browser)
    pictures_page.check_url('https://yandex.ru/images/')
    pictures_page.click_to(PicturesPageLocators.PICTURES_FIRST_ITEM)
    pictures_page.check_category_name_in_search_field()
    pictures_page.click_to(PicturesPageLocators.PIC_FIRST)
    first_picture = pictures_page.get_image_src()
    pictures_page.click_to_next_button()
    pictures_page.check_picture_change(first_picture)
    pictures_page.click_to_previous_button()
    pictures_page.check_current_picture_after_changing(first_picture)
