from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Hobbie(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    birthday_year: int
    birthday_month: int
    birthday_day: int
    subjects: list[str]
    hobbies: list[Hobbie]
    picture: str
    address: str
    state: str
    city: str

    '''
    genders = ['Male', 'Female', 'Other']
    first_name = 'Evgeny'
    last_name = 'Tverdun'
    email = 'tverdune@ya.ru'
    gender = genders[0]
    mobile_number = '9034334637'
    b_year = 1982
    b_month = 5
    b_day = 1
    subjects = 'Computer Science', 'English'
    hobbies = 'Sports', 'Reading', 'Music'
    picture = 'pic.jpg'
    address = 'Home sweet home'
    state = 'NCR'
    city = 'Noida'
    '''