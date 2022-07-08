from demoqa_tests.model import app


def test_practice_form():
    # Pre

    app.form.open_browser()
    # When
    app.form.set_first_name()\
        .set_last_name()\
        .set_email()\
        .set_gender()\
        .set_mobile_number()\
        .set_birth_day()\
        .set_subjects()\
        .set_hobbies()\
        .set_picture()\
        .set_address()\
        .set_state()\
        .set_city()\
        .submit_form()
    # Then
    app.form.full_name.should_have('Evgeny Tverdun')
    app.form.email.should_have('tverdune@ya.ru')
    app.form.gender.should_have('Male')
    app.form.mobile_number.should_have('9034334637')
    app.form.date_of_birth.should_have('01 May,1982')
    app.form.subjects.should_have('Computer Science, English')
    app.form.hobbies.should_have('Sports, Reading, Music')
    app.form.picture.should_have('pic.jpg')
    app.form.address.should_have('Home sweet home')
    app.form.state_and_city.should_have('NCR Noida')
