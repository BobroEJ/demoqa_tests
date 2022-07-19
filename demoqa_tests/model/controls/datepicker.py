from calendar import month_name

from selene import command
from selene.core.entity import Element
from selene.support.shared import browser


class Datepicker:

    def __init__(self, element: Element, year, month, day):
        self.element = element
        self.year = year
        self.month = month
        self.day = str(day) if day > 9 else f'0{day}'
    '''
    set_date_straight не работает, так и не смог разобраться, почему.
    '''
    def set_date_straight(self):
        self.element.perform(command.js.set_value('05 01 1982')).press_enter()

    def set_date_by_clicks(self):
        self.element.click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select [value="{self.year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select [value="{self.month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{self.day}').click()
