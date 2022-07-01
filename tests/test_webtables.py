from selene import have
from selene.support.shared import browser


def test_webtables():
    browser.open('webtables')

    #add 4th string
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Evgeny')
    browser.element('#lastName').type('Tverdun')
    browser.element('#userEmail').type('tverdune@ya.ru')
    browser.element('#age').type('40')
    browser.element('#salary').type('15000')
    browser.element('#department').type('IT')
    browser.element('#submit').click()
    #edit 2nd string
    browser.element('#edit-record-2').click()
    browser.element('#firstName').set_value('Bonnie')
    browser.element('#lastName').set_value('Wotson')
    browser.element('#userEmail').set_value('bw@ms.ru')
    browser.element('#age').set_value('33')
    browser.element('#salary').set_value('22000')
    browser.element('#department').set_value('Transport')
    browser.element('#submit').click()
    #delete 3rd string
    browser.element('#delete-record-3').click()

    l = [
        ['Cierra', 'Vega', '39', 'cierra@example.com', '10000', 'Insurance'],
        ['Bonnie', 'Wotson', '33', 'bw@ms.ru', '22000', 'Transport'],
        ['Evgeny', 'Tverdun', '40', 'tverdune@ya.ru', '15000', 'IT']
        ]

    browser.element('//*[@role="rowgroup"]').element('.//*[@role="gridcell"]').should(have.exact_text('Cierra'))
    browser.element('//*[@role="rowgroup"]').element('.//*[@role="gridcell"][2]').should(have.exact_text('Vega'))
    browser.element('//*[@role="rowgroup"]').element('.//*[@role="gridcell"][3]').should(have.exact_text('39'))
    browser.element('//*[@role="rowgroup"]').element('.//*[@role="gridcell"][4]').should(have.exact_text('cierra@example.com'))
    browser.element('//*[@role="rowgroup"]').element('.//*[@role="gridcell"][5]').should(have.exact_text('10000'))
    browser.element('//*[@role="rowgroup"]').element('.//*[@role="gridcell"][6]').should(have.exact_text('Insurance'))
    browser.element('//*[@role="rowgroup"][2]').element('.//*[@role="gridcell"]').should(have.exact_text('Bonnie'))
    browser.element('//*[@role="rowgroup"][2]').element('.//*[@role="gridcell"][2]').should(have.exact_text('Wotson'))
    browser.element('//*[@role="rowgroup"][2]').element('.//*[@role="gridcell"][3]').should(have.exact_text('33'))
    browser.element('//*[@role="rowgroup"][2]').element('.//*[@role="gridcell"][4]').should(have.exact_text('bw@ms.ru'))
    browser.element('//*[@role="rowgroup"][2]').element('.//*[@role="gridcell"][5]').should(have.exact_text('22000'))
    browser.element('//*[@role="rowgroup"][2]').element('.//*[@role="gridcell"][6]').should(have.exact_text('Transport'))
    browser.element('//*[@role="rowgroup"][3]').element('.//*[@role="gridcell"]').should(have.exact_text('Evgeny'))
    browser.element('//*[@role="rowgroup"][3]').element('.//*[@role="gridcell"][2]').should(have.exact_text('Tverdun'))
    browser.element('//*[@role="rowgroup"][3]').element('.//*[@role="gridcell"][3]').should(have.exact_text('40'))
    browser.element('//*[@role="rowgroup"][3]').element('.//*[@role="gridcell"][4]').should(have.exact_text('tverdune@ya.ru'))
    browser.element('//*[@role="rowgroup"][3]').element('.//*[@role="gridcell"][5]').should(have.exact_text('15000'))
    browser.element('//*[@role="rowgroup"][3]').element('.//*[@role="gridcell"][6]').should(have.exact_text('IT'))