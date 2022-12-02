import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser:")
    parser.addoption('--selenide', action='store', default='n',
                     help="run selenium in docker y/N:")


@pytest.fixture(scope="session")
def browser(request):
    global driver
    selected_browser = request.config.getoption("browser")
    selenide = request.config.getoption("selenide")
    if selenide == 'y':
        if selected_browser == 'chrome':
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "107.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                desired_capabilities=capabilities)
    else:
        if selected_browser == 'chrome':
            driver = webdriver.Chrome()
        elif selected_browser == 'firefox':
            driver = webdriver.Firefox()
    yield driver
    driver.quit()
