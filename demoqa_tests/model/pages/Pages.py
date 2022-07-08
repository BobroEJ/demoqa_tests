from selene import command
from selene.support.shared import browser

from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.table import Table
from demoqa_tests.model.controls.tags_input import TagsInput
from demoqa_tests.utils import resource


class Student_registration_form_page:

    def __init__(self, user_data):
        self.user_first_name = user_data.first_name
        self.user_last_name = user_data.last_name
        self.user_email = user_data.email
        self.user_gender = user_data.gender
        self.user_mobile_number = user_data.mobile_number
        self.user_b_year = user_data.b_year
        self.user_b_month = user_data.b_month
        self.user_b_day = user_data.b_day
        self.user_subjects = user_data.subjects
        self.user_hobbies = user_data.hobbies
        self.user_picture = user_data.picture
        self.user_address = user_data.address
        self.user_state = user_data.state
        self.user_city = user_data.city

    @staticmethod
    def open_browser():
        browser.open('automation-practice-form')

    def set_first_name(self):
        browser.element('#firstName').type(self.user_first_name)
        return self

    def set_last_name(self):
        browser.element('#lastName').type(self.user_last_name)
        return self

    def set_email(self):
        browser.element('#userEmail').type(self.user_email)
        return self

    def set_gender(self):
        browser.element(f'[name=gender][value={self.user_gender}]').following_sibling.click()
        return self

    def set_mobile_number(self):
        browser.element('#userNumber').type(self.user_mobile_number)
        return self

    def set_birth_day(self):
        Datepicker(browser.element('#dateOfBirthInput'), self.user_b_year, self.user_b_month, self.user_b_day).set_date_by_clicks()
        return self

    def set_subjects(self):
        for value in self.user_subjects:
            TagsInput(browser.element('#subjectsInput')).add_by_click(value)
        return self

    def set_hobbies(self):
        hobbies_dict = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Reading': '[for=hobbies-checkbox-2]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for value in self.user_hobbies:
            browser.element(hobbies_dict[value]).click()
        return self

    def set_picture(self):
        browser.element('#uploadPicture').send_keys(resource(self.user_picture))
        return self

    def set_address(self):
        browser.element('#currentAddress').type(self.user_address)
        return self

    def set_state(self):
        Dropdown(browser.element('#state input')).autocomplete(option=self.user_state)
        return self

    def set_city(self):
        Dropdown(browser.element('#city input')).autocomplete(option=self.user_city)
        return self

    @staticmethod
    def submit_form():
        browser.element('#submit').perform(command.js.click)

    # def should_have(self, result):
    #     browser.all('.table-responsive tbody tr')[self.row_num].all('td')[1].should(have.exact_text(result))
    #     return self

    @property
    def full_name(self):
        return Table(0)
        # return browser.all('.table-responsive tbody tr')[0].all('td')[1]

    @property
    def email(self):
        return Table(1)

    @property
    def gender(self):
        return Table(2)

    @property
    def mobile_number(self):
        return Table(3)

    @property
    def date_of_birth(self):
        return Table(4)

    @property
    def subjects(self):
        return Table(5)

    @property
    def hobbies(self):
        return Table(6)

    @property
    def picture(self):
        return Table(7)

    @property
    def address(self):
        return Table(8)

    @property
    def state_and_city(self):
        return Table(9)



'''
app.form.subjects.should_have('Chemistry', 'Maths', 'Physics')
'''


