from selene import command
from selene.support.shared import browser

from demoqa_tests.data import Gender, Hobbie
from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.table_row import TableRow
from demoqa_tests.model.controls.tags_input import TagsInput
from demoqa_tests.utils import resource


class StudentRegistrationPage:

    def open(self):
        browser.open('automation-practice-form')

    def set_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def set_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def set_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def set_gender(self, gender: Gender):
        browser.element(f'[name=gender][value={gender.value}]').following_sibling.click()
        return self

    def set_mobile_number(self, mobile_number):
        browser.element('#userNumber').type(mobile_number)
        return self

    def set_birth_day(self, birth_day, birth_month, birth_year):
        Datepicker(browser.element('#dateOfBirthInput'), birth_year, birth_month, birth_day)\
            .set_date_by_clicks()
        return self

    def set_subjects(self, subjects: list[str]):
        for value in subjects:
            TagsInput(browser.element('#subjectsInput')).add_by_click(value)
        return self

    def set_hobbies(self, hobbies: list[Hobbie]):
        hobbies_dict = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Reading': '[for=hobbies-checkbox-2]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for hobbie in hobbies:
            browser.element(hobbies_dict[hobbie.value]).click()
        return self

    def set_picture(self, picture):
        browser.element('#uploadPicture').send_keys(resource(picture))
        return self

    def set_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def set_state(self, state):
        Dropdown(browser.element('#state input')).autocomplete(option=state)
        return self

    def set_city(self, city):
        Dropdown(browser.element('#city input')).autocomplete(option=city)
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)


