from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import datetime
import time

def user_birth():
    c_time = datetime.datetime.now()
    c_year = c_time.year

    input_check = True
    while(input_check):
        date_of_birth_str = input('Enter your Date of Birth', type=DATE)
        date_of_birth = datetime.datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
        if(date_of_birth.year > c_year):
            popup('Invalid Date of Birth', 'Please enter a valid Date of Birth before the current year.')
        else:
            input_check = False
    return date_of_birth

def current_date():
    return datetime.datetime.now().date()

def calculate_age(birth, date_now):
    age_years = date_now.year - birth.year
    age_months = date_now.month - birth.month
    age_days = date_now.day - birth.day

    if age_days < 0:
        age_months -= 1
        age_days += (date_now - datetime.timedelta(days=date_now.day)).day

    if age_months < 0:
        age_years -= 1
        age_months += 12

    total_days = (date_now - birth).days
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    total_seconds = total_minutes * 60

    return {
        'years': age_years,
        'months': age_months,
        'days': age_days,
        'total_days': total_days,
        'total_hours': total_hours,
        'total_minutes': total_minutes,
        'total_seconds': total_seconds
    }

def info_table(d_o_birth, c_date, age):
    
    put_progressbar('bar', auto_close=True)
    for i in range(1, 11):
        set_progressbar('bar', i / 10)
        time.sleep(0.5)

    put_table(
        [
            ['Date Of Birth', 'Current Date', 'Total Age', 'Total Days', 'Total Months', 'Total Hours', 'Total Minutes', 'Total Seconds'],
            [
                f'{d_o_birth}', f'{c_date}', f'{age["years"]} years, {age["months"]} months, {age["days"]} days', f'{age["total_days"]}', f'{age["years"] * 12 + age["months"]}', f'{age["total_hours"]} hr', f'{age["total_minutes"]} min', f'{age["total_seconds"]} sec'
            ]
        ]
    )

    put_image("https://img.freepik.com/free-vector/person-different-ages_23-2148392903.jpg?w=1380&t=st=1719664200~exp=1719664800~hmac=4dfd945bc7289410e4547d325baeaae89fc93cb58c77efbdddaa4df669a00d13")

def main():
    put_html("<h1 align='center'>WELCOME TO LIFE SPAN CALCULATOR</h1>")
    d_o_birth = user_birth()
    c_date = current_date()
    age = calculate_age(d_o_birth, c_date)
    info_table(d_o_birth, c_date, age)

if __name__ == '__main__':
    start_server(main, port=8080, auto_open_webbrowser=True)
