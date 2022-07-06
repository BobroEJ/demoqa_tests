from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


from demoqa_tests.controls.datepicker import Datepicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.resource import resource
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput


def test_practice_form():
    # Pre
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

    Table(0, 'Evgeny Tverdun')
    Table(1, 'tverdune@ya.ru')
    Table(2, 'Male')
    Table(3, '9034334637')
    Table(4, '01 May,1982')
    Table(5, 'Computer Science, English')
    Table(6, 'Sports, Reading')
    Table(7, 'pic.jpg')
    Table(8, 'Home sweet home')
    Table(9, 'NCR Noida')