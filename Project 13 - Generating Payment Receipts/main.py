from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def store_products():
    print('=====> WELCOME TO MY-SCHOOL <=====')

    default_courses = [
        {
            'Course' : 'Full Stack Web Application Development',
            'Duration' : '6 Months',
            'Access' : 'Life Time',
            'Price' : 2999
        },

        {
            'Course' : 'Django Tutorials for Beginners',
            'Duration' : '2 Months',
            'Access' : 'Life Time',
            'Price' : 'Free'    
        },

        {
            'Course' : 'AI & Machine Learning Batch Live',
            'Duration' : '1 Year',
            'Access' : 'Life Time',
            'Price' : 10000
        },

        {
            'Course' : 'Data Science Complete Course',
            'Duration' : '6 Months',
            'Access' : 'Life Time',
            'Price' : 8000
        }
    ]

    for i, data in enumerate(default_courses, start=0):
        print(f'--> Course : {i}')
        print(f'Course Name : {data['Course']}\nDuration : {data['Duration']}\nAccess : {data['Access']}\nPrice : {data['Price']}')
        print('---------------------------------------------------------')


    templete = [
        ['Date', 'Name', 'Duration', 'Access', 'Price']
        
    ]

    course_index = -1

    parchasing = True

    while(parchasing):
        buy_course = int(input("Which Course Do you wan to Buy (0, 1, 2....) : "))
        if(buy_course > len(default_courses)):
            print("Course Index Not Exist to Buy !!")
        else:
            course = default_courses[buy_course]
            current_date = datetime.now()
            formated_time = current_date.strftime('%d/%m/%Y')
            buy_date = [
                {
                    'date': formated_time,
                }
            ]
            date = buy_date[0]
                
            templete.append([
                date['date'],
                course['Course'],
                course['Duration'],
                course['Access'],
                course['Price']
            ])

            for row in templete:
                print(row)
        exit = input("Do you want to exit (0 - exit) : ")
        if(exit == 'exit' or exit == '0'):
            parchasing = False
        



store_products()