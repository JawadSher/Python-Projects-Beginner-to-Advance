
def addStudents(stnd_name, students_list):
    students_list.add(stnd_name)
    if stnd_name in students_list:
        print("Student Add Temprory")

def allStudents(students_list):
    print("----> Total Temprory Saved Students <----")
    for stnd_num, student in enumerate(students_list, 1):
        print(f"{stnd_num} - {students_list}")

def addSubjects(subjt_name, subjects):
    subjects.add(subjt_name)
    if subjt_name in subjects:
        print("Subject Added Temprory")

def allSubjects(subjects):
    print("----> Total Temprory Saved Subjects <----")
    for subj_num, subject in enumerate(subjects, 1):
        print(f"{subj_num} - {subject}")

def currentData():
    pass

def AddDataRegister():
    pass

def readRegister():
    pass

def editRegister(stnd_name):
    pass

def main():
    print("======> Welcome to Attendence Management System <======")
    print()
    
    students = set()
    subjects = set()
    is_running = True

    while(is_running):
        print()
        print("1 - Add Students Temprory")
        print("2 - Add Subjects Temprory")
        print("3 - Show Total Temprory Students")
        print("4 - Show Total Temprory Subjects")
        print("5 - Add All Students & Subjects to Register Permenantly")
        print("6 - Read Class Attendence Register")
        print("7 - Edit Attendence Register")
        print("8 - Exit")
        print()

        user_selection = int(input("Enter a Number : "))
        
        match user_selection:
            case 1:
                student_name = input("Enter a Student Name : ")
                addStudents(student_name, students)
            case 2:
                subject_name = input("Enter a Subject Name : ")
                addSubjects(subject_name, subjects)
            case 3:
                allStudents(students)
            case 4:
                allSubjects(subjects)
            case 5:
                AddDataRegister()
            case 6:
                readRegister()
            case 7:
                editRegister()
            case 8:
                is_running = False
            case _:
                print("Invalid Input")

if __name__ == "__main__":
    main()