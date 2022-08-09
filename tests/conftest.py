import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

import sys
import os

conf_path = os.getcwd()
sys.path.append(conf_path)
sys.path.append(conf_path + '\demoqa_tests')

from demoqa_tests import utils


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com/'
    browser.config.hold_browser_open = False

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options)
    browser.config.driver = driver

    yield

    utils.add_screenshot(browser)
    utils.add_logs(browser)
    utils.add_html(browser)
    utils.add_video(browser)
