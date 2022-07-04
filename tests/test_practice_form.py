import os

import pytest
from selene import have
from selene.support.shared import browser
from pathlib import Path
import demoqa_tests


def resource(path):
    return str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{path}'))


def test_practice_form():
    # Pre
    browser.open('automation-practice-form')
    #When
    browser.element('#firstName').type('Evgeny')
    browser.element('#lastName').type('Tverdun')
    browser.element('#userEmail').type('tverdune@ya.ru')

    male_gender = browser.element('[for="gender-radio-1"]')
    male_gender.click()

    browser.element('#userNumber').type('9034334637')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="4"]').click()
    browser.element('.react-datepicker__year-select [value="1982"]').click()
    browser.element('.react-datepicker__day--001').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter().type('English').press_enter()

    sports_hobby = browser.element('#hobbies-checkbox-1').following_sibling()
    sports_hobby.click()
    reading_hobby = browser.element('#hobbies-checkbox-2').following_sibling()
    reading_hobby.click()

    browser.element('#uploadPicture').send_keys(
        resource('pic.jpg')
    )

    browser.element('#currentAddress').type('Home sweet home')

    browser.element('#state').element('input').type('NCR').press_enter()
    browser.element('#city').element('input').type('Noida').press_enter().press_enter()
    #Then
    browser.element('//td[.="Student Name"]').following_sibling.should(have.exact_text('Evgeny Tverdun'))
    browser.element('//td[.="Student Email"]').following_sibling.should(have.exact_text('tverdune@ya.ru'))
    browser.element('//td[.="Gender"]').following_sibling.should(have.exact_text('Male'))
    browser.element('//td[.="Mobile"]').following_sibling.should(have.exact_text('9034334637'))
    browser.element('//td[.="Date of Birth"]').following_sibling.should(have.exact_text('01 May,1982'))
    browser.element('//td[.="Subjects"]').following_sibling.should(have.exact_text('Computer Science, English'))
    browser.element('//td[.="Hobbies"]').following_sibling.should(have.exact_text('Sports, Reading'))
    browser.element('//td[.="Picture"]').following_sibling.should(have.exact_text('pic.jpg'))
    browser.element('//td[.="Address"]').following_sibling.should(have.exact_text('Home sweet home'))
    browser.element('//td[.="State and City"]').following_sibling.should(have.exact_text('NCR Noida'))