from selene import command, have
from selene.core.entity import SeleneElement
from selene.support.shared import browser


class Dropdown:

    def __init__(self, element: SeleneElement):
        self.element = element

    def select_by_click(self, option: str):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()

    def autocomplete(self, option: str):
        self.element.type(option).press_tab()

