# Seatwork 1
from pyscript import display, document


fullname = 'Anthony Kendrick Dino'  # string
age = ag3_s = 15  # integer
height = 172.72  # float
countries_ = ['Canada', 'Singapore', 'Japan', 'Dubai', 'Israel']  # list
student_info = {  # Dictionary
    'car_brand': 'Toyota',
    'shoe_size': 10,
    'best_friends': ['Jacob Minguillo', 'Raphael De Vera', 'Logan Anaque', 'Marcus De Jesus']
}
fruits = {'Mango', 'Apple', 'Strawberry', 'banana', 'tomato',}  # set
Days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')  # tuple



display(f'hello. My name is {fullname}, I am {ag3_s} years old.', target='result')
document.getElementById('result').innerHTML = f'hello. My name is <i>{fullname}</i>, I am {ag3_s} years old. I am {height} cm tall. Some countries I want to visit are {countries_}. Here is some information about me: {student_info}. My favorite fruits are {fruits}. The days of the week are {Days_of_the_week}.'