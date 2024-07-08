from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import win10toast

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

    totalFee = 0
    discount = 3000
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

            if course['Price'] != 'Free':
                totalFee += course['Price']
            

            for row in templete:
                print(row)

        exit = input("\nDo you want to exit (0 - exit - No) : ")
        if(exit == 'exit' or exit == '0'):
            parchasing = False
    
    
    templete.append([
        ("Discount"),
        (""),
        (""),
        (""),
        (discount),
    ])
    templete.append([
        ("Total"),
        (""),
        (""),
        (""),
        (totalFee-discount),
    ])

    pdf = SimpleDocTemplate('Receipt.pdf', pagesize = A4)
    toaster = win10toast.ToastNotifier()
    t_title = "Courses Reciept Ready!"
    message = "Courses has been parchased from My-School"
    toaster.show_toast(t_title, message)
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1
    title = Paragraph('My-School Courses', title_style)
    style = TableStyle(
        [
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
            ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 4, 0 ), colors.gray ), 
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
            ("BACKGROUND", (0, -2), (-1, -1), colors.lightblue), 
        ]
    )
    table = Table(templete, style=style)
    pdf.build([title, table])

if __name__ == '__main__':
    store_products()