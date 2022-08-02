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
