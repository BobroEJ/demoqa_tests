from selene import command
from selene.support.shared import browser

from demoqa_tests.controls.datepicker import Datepicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.utils import resource


class Student_registration_form_page:

    def __init__(self, user_data):
        self.first_name = user_data.first_name
        self.last_name = user_data.last_name
        self.email = user_data.email
        self.gender = user_data.gender
        self.mobile_number = user_data.mobile_number
        self.b_year = user_data.b_year
        self.b_month = user_data.b_month
        self.b_day = user_data.b_day
        self.subjects = user_data.subjects
        self.hobbies = user_data.hobbies
        self.picture = user_data.picture
        self.address = user_data.address
        self.state = user_data.state
        self.city = user_data.city

    @staticmethod
    def open_browser():
        browser.open('automation-practice-form')

    def set_first_name(self):
        browser.element('#firstName').type(self.first_name)

    def set_last_name(self):
        browser.element('#lastName').type(self.last_name)

    def set_email(self):
        browser.element('#userEmail').type(self.email)

    def set_gender(self):
        browser.element(f'[name=gender][value={self.gender}]').following_sibling.click()

    def set_mobile_number(self):
        browser.element('#userNumber').type(self.mobile_number)

    def set_birth_day(self):
        Datepicker(browser.element('#dateOfBirthInput'), self.b_year, self.b_month, self.b_day).set_date_by_clicks()

    def set_subjects(self):
        for value in self.subjects:
            TagsInput(browser.element('#subjectsInput')).add_by_click(value)

    def set_hobbies(self):
        hobbies_dict = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Reading': '[for=hobbies-checkbox-2]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for value in self.hobbies:
            browser.element(hobbies_dict[value]).click()

    def set_picture(self):
        browser.element('#uploadPicture').send_keys(resource(self.picture))

    def set_address(self):
        browser.element('#currentAddress').type(self.address)

    def set_state(self):
        Dropdown(browser.element('#state input')).autocomplete(option=self.state)

    def set_city(self):
        Dropdown(browser.element('#city input')).autocomplete(option=self.city)

    @staticmethod
    def submit_form():
        browser.element('#submit').perform(command.js.click)





'''
app.form.subjects.should_have('Chemistry', 'Maths', 'Physics')
'''


