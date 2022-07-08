from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser

from demoqa_tests.Pages import Student_registration_form_page
from demoqa_tests.controls.datepicker import Datepicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.data import User
from demoqa_tests.utils import resource
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput


def test_practice_form():
    # Pre
    form = Student_registration_form_page(User)
    form.open_browser()
    # When
    form.set_first_name()
    form.set_last_name()
    form.set_email()
    form.set_gender()
    form.set_mobile_number()
    form.set_birth_day()
    form.set_subjects()
    form.set_hobbies()
    form.set_picture()
    form.set_address()
    form.set_state()
    form.set_city()
    form.submit_form()
    # Then
    result_table = Table
    result_table(0).should_have('Evgeny Tverdun')
    result_table(1).should_have('tverdune@ya.ru')
    result_table(2).should_have('Male')
    result_table(3).should_have('9034334637')
    result_table(4).should_have('01 May,1982')
    result_table(5).should_have('Computer Science, English')
    result_table(6).should_have('Sports, Reading, Music')
    result_table(7).should_have('pic.jpg')
    result_table(8).should_have('Home sweet home')
    result_table(9).should_have('NCR Noida')
