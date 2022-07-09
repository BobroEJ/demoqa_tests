from dataclasses import dataclass


@dataclass
class User:
    genders = ['Male', 'Female', 'Other']
    first_name = 'Evgeny'
    last_name = 'Tverdun'
    email = 'tverdune@ya.ru'
    gender = genders[0]
    mobile_number = 9034334637
    b_year = 1982
    b_month = 5
    b_day = 1
    subjects = 'Computer Science', 'English'
    hobbies = ['Sports', 'Reading', 'Music']
    picture = 'pic.jpg'
    address = 'Home sweet home'
    state = 'NCR'
    city = 'Noida'
