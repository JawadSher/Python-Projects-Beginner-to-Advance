import os
import json

def addStudent(stnd_name, roll_num, students_dict):
    if roll_num in students_dict:
        print(f"Roll number {roll_num} already exists for student {students_dict[roll_num]}.")
    else:
        students_dict[roll_num] = stnd_name
        with open("Temprory.txt", "w") as file:
            json.dump(students_dict, file)
        file.close()
        print("Student Added Temprorily")

def allStudents(students_dict):
    print("----> Total Temprory Saved Students <----")
    for rollnum, student in students_dict.items():
        print(f"{rollnum} - {student}")

def addSubjects(subjt_name, subjects):
    subjects.add(subjt_name)
    if subjt_name in subjects:
        print("Subject Added Temprory")

def allSubjects(subjects):
    print("----> Total Temprory Saved Subjects <----")
    for subj_num, subject in enumerate(subjects, 1):
        print(f"{subj_num} - {subject}")

def AddDataToRegister():
    pass

def readRegister():
    pass

def editRegister(stnd_name):
    pass

def main():
    print("======> Welcome to Attendence Management System <======")
    
    students = {}
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
                case1 = True
                while(case1):
                    student_name = input("Enter a Student Name : ")
                    if(student_name == "exit"):
                        case1 = False
                        break
                    roll_num = int(input("Enter Roll Number : "))
                    addStudent(student_name, roll_num, students)
                    print("Type exit for Exiting")
                    print("------------------------------")
            case 2:
                case2 = True
                while case2:
                    subject_name = input("Enter a Subject Name : ")
                    if(subject_name == 'exit'):
                        case2 = False
                        break
                    addSubjects(subject_name, subjects)
                    print("Type exit of Exiting")
                    print("------------------------------")
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