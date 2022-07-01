import pytest
from selene import have
from selene.support.shared import browser
# from selenium.webdriver.common.by import By


def test_practice_form():
    browser.open('automation-practice-form')
    browser.should(have.title('ToolsQA'))

    # browser.element('#firstName').type('Evgeny')
    browser.element('//*[@id="firstName"]').type('Evgeny')

    browser.element('#lastName').type('Tverdun')
    browser.element('#userEmail').type('tverdune@ya.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9034334637')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="4"]').click()
    browser.element('.react-datepicker__year-select [value="1982"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter().type('English').press_enter()
    browser.element('#hobbies-checkbox-1').following_sibling().click()
    browser.element('#hobbies-checkbox-2').following_sibling().click()
    browser.element('#uploadPicture').send_keys('C:\qa-guru\qa-guru-lesson-5-hw\pic.jpg')
    browser.element('#currentAddress').type('Home sweet home')
    browser.element('#state input').type('NCR').press_enter()
    browser.element('#city input').type('Noida').press_enter().press_enter()

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