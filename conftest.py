import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

    
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                 help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):            
    options = webdriver.ChromeOptions()
    # выключаем служебные сообщения Хрома
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # берем язык из командной строки
    user_language = request.config.getoption("language")
    # включаем поддержку языков в Хроме
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # включаем поддержку языков в ff
    options_ff = Options()
    options_ff.set_preference("intl.accept_languages", user_language)
    # из командной строки получаем, какой браузер используется
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")        
        browser = webdriver.Chrome(options=options)        
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_ff)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    