import allure
from calendar import month_name

from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.data import User, Gender, Hobbie
from demoqa_tests.model import app


def test_practice_form():
    # Given
    with allure.step('Открываем страницу'):
        app.registration_page.open()
    with allure.step('Создаём студента'):
        student = User(
            first_name='Evgeny',
            last_name='Tverdun',
            email='tverdune@ya.ru',
            gender=Gender.Male,
            mobile_number='9034334637',
            birthday_year=1982,
            birthday_month=5,
            birthday_day=1,
            subjects=['Computer Science', 'English'],
            hobbies=[Hobbie.Sports, Hobbie.Reading, Hobbie.Music],
            picture='pic.jpg',
            address='Home sweet home',
            state='NCR',
            city='Noida'
        )

    # When
    with allure.step('Вносим данные в форму'):
        (app.registration_page
         .set_first_name(student.first_name)
         .set_last_name(student.last_name)
         .set_email(student.email)
         .set_gender(student.gender)
         .set_mobile_number(student.mobile_number)
         .set_birth_day(student.birthday_day, student.birthday_month, student.birthday_year)
         .set_subjects(student.subjects)
         .set_hobbies(student.hobbies)
         .set_picture(student.picture)
         .set_address(student.address)
         .set_state(student.state)
         .set_city(student.city)
         .submit_form())

    # Then
    with allure.step('Проверяем полное имя'):
        app.registered_user_dialog.full_name.should_have(student.first_name, student.last_name)
    with allure.step('Проверяем email'):
        app.registered_user_dialog.email.should_have(student.email)
    with allure.step('Проверяем пол'):
        app.registered_user_dialog.gender.should_have(student.gender.value)
    with allure.step('Проверяем ноиер телефона'):
        app.registered_user_dialog.mobile_number.should_have(student.mobile_number)
    with allure.step('Проверяем дату рождения'):
        app.registered_user_dialog.date_of_birth.should_have(
            f'{student.birthday_day} {month_name[student.birthday_month]},{student.birthday_year}')
    with allure.step('Проверяем предменты'):
        app.registered_user_dialog.subjects.should_have(student.subjects[0], student.subjects[1])
    with allure.step('Проверяем хобби'):
        app.registered_user_dialog.hobbies.should_have(student.hobbies[0].value, student.hobbies[1].value,
                                                       student.hobbies[2].value)
    with allure.step('Проверяем путь к картинке'):
        app.registered_user_dialog.picture.should_have(student.picture)
    with allure.step('Проверяем адрес'):
        app.registered_user_dialog.address.should_have(student.address)
    with allure.step('Проверяем штат и город'):
        app.registered_user_dialog.state_and_city.should_have(student.state, student.city)

