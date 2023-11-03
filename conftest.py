import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    '''
    Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
    '''
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru or es")
    
@pytest.fixture(scope="session")
def browser(request):
    lang = request.config.getoption("language")    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    match lang:
        case "ru":
            print("\nstart russian language for test..")
        case "es":
            print("\nstart spanish language for test..")
        case 'en':
            print("\nstart english language for test..")
        case _:
            print(f"\nstart {lang} language for test..") 
            # raise pytest.UsageError("--language should be en, ru or es")
    yield browser
    print("\nquit browser..")
    browser.quit()