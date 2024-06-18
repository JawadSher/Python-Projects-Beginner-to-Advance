# Attendance Management System

## Overview

This project provides a comprehensive Attendance Management System, designed to track and manage student attendance efficiently. The system allows users to add students and subjects temporarily, create attendance registers, and perform various operations on the attendance data.

## Features

1.  **Add Students**: Temporarily store student information (name and roll number).
2.  **Add Subjects**: Temporarily store subject names.
3.  **Display Students**: Display all temporarily saved students.
4.  **Display Subjects**: Display all temporarily saved subjects.
5.  **Create Attendance Register**: Create a default or dynamic attendance register with customizable options.
6.  **Read Attendance Register**: Read and display the content of a saved attendance register.
7.  **Edit Attendance Register**: Perform various operations such as deleting rows/columns, merging/unmerging cells, inserting rows/columns, and adding data to specific cells.
8.  **Check Attendance**: Evaluate attendance status at the end of the month.

## Getting Started

### Prerequisites

-   Python 3.x
-   `openpyxl` library

Install the `openpyxl` library using pip:

`pip install openpyxl` 

### Running the Program
Clone the repository and navigate to the project directory. Run the main script:

`python main.py` 

## Usage

Upon running the script, you will be presented with a menu to interact with the system. Below is a detailed explanation of each feature:

### 1. Add Students Temporarily

Add student details temporarily to the system.

`def addStudent(stnd_name, roll_num, students_dict):` 

### 2. Add Subjects Temporarily

Add subjects to the system temporarily.

`def addSubjects(subjt_name, subjects):` 

### 3. Show Total Temporarily Saved Students

Display the list of all temporarily saved students.

`def allStudents(students_dict):` 

### 4. Show Total Temporarily Saved Subjects

Display the list of all temporarily saved subjects.

`def allSubjects(subjects):` 

### 5. Create Attendance Register

Create an attendance register in either default or dynamic mode. The default mode generates a register for the current month, while the dynamic mode allows the user to customize the register name, month, and year.

`def createRegister(students_dict, subjects_set):` 

### 6. Read Class Attendance Register

Read and display the content of a saved attendance register.

`def readRegister():` 

### 7. Edit Attendance Register

Perform various operations on the attendance register such as deleting rows/columns, merging/unmerging cells, inserting rows/columns, and adding data to specific cells.

`def editRegister():` 

### 8. Check Attendance at the End of the Month

Evaluate and display the attendance status of students at the end of the month.

`def check_attendence():` 

### 9. Exit
Exit the system.

## Code Structure

The main components of the code are as follows:

-   **`addStudent`**: Adds a student to the temporary list and saves it in a JSON file.
-   **`allStudents`**: Prints all temporarily saved students.
-   **`addSubjects`**: Adds a subject to the temporary set.
-   **`allSubjects`**: Prints all temporarily saved subjects.
-   **`createRegister`**: Creates an attendance register with the option to choose between a default or dynamic register.
-   **`readRegister`**: Reads and prints the content of a specified attendance register.
-   **`editRegister`**: Allows various edit operations on the attendance register such as deleting rows/columns, merging/unmerging cells, and inserting rows/columns.
-   **`check_attendence`**: Checks and prints the attendance status of students for the specified register.
-   **`main`**: Main function to display the menu and handle user inputs.

## Example
`======> Welcome to Attendance Management System <======

1 - Add Students Temporarily

2 - Add Subjects Temporarily

3 - Show Total Temporarily Students

4 - Show Total Temporarily Subjects

5 - Create Attendance Register

6 - Read Class Attendance Register

7 - Edit Attendance Register

8 - Check Attendance in the end of Month

9 - Exit

Enter a Number:` 

Follow the prompts to use the system effectively.
