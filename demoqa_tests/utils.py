from pathlib import Path

import allure
from allure_commons.types import AttachmentType
from selene.support.shared import browser

import demoqa_tests


def resource(path):
    return str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{path}'))


def add_screenshot(browser=browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser=browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'log', AttachmentType.TEXT, '.log')


def add_html(browser=browser):
    html = browser.driver.page_source
    allure.attach(html, 'html', AttachmentType.HTML, '.html')


def add_video(browser=browser):
    video_url = f'https://selenoid.autotests.cloud/video/{browser.driver.session_id}.mp4'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'test_video_' + browser.driver.session_id, AttachmentType.HTML, '.html')








