from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


from demoqa_tests.controls.datepicker import Datepicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.utils import resource
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput


def test_practice_form():
    # Given
    browser.open('automation-practice-form')
    # When
    browser.element('#firstName').type('Evgeny')
    browser.element('#lastName').type('Tverdun')
    browser.element('#userEmail').type('tverdune@ya.ru')

    male_gender = browser.element('[for="gender-radio-1"]')
    male_gender.click()

    browser.element('#userNumber').type('9034334637')

    Datepicker(browser.element('#dateOfBirthInput'), 1982, 5, 1).set_date_by_clicks()

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add_by_click('Comp', autocomplete='Computer Science')
    subjects.add_by_tab('eng')

    sports_hobby = browser.element('#hobbies-checkbox-1').following_sibling()
    sports_hobby.click()
    reading_hobby = browser.element('#hobbies-checkbox-2').following_sibling()
    reading_hobby.click()

    browser.element('#uploadPicture').send_keys(resource('pic.jpg'))

    browser.element('#currentAddress').type('Home sweet home')

    Dropdown(browser.element('#state')).select_by_click(option='NCR')
    Dropdown(browser.element('#city input')).autocomplete(option='noi')

    browser.element('#submit').perform(command.js.click)

    # Then
    result_table = Table
    result_table(0, 'Evgeny Tverdun').result_assert()
    result_table(1, 'tverdune@ya.ru').result_assert()
    result_table(2, 'Male').result_assert()
    result_table(3, '9034334637').result_assert()
    result_table(4, '01 May,1982').result_assert()
    result_table(5, 'Computer Science, English').result_assert()
    result_table(6, 'Sports, Reading').result_assert()
    result_table(7, 'pic.jpg').result_assert()
    result_table(8, 'Home sweet home').result_assert()
    result_table(9, 'NCR Noida').result_assert()