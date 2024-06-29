<h1>Life Span Calculator</h1>

Calculate your age in various units with this simple web application built using Python and PyWebIO.

## Table of Contents

-   [Introduction](#introduction)
-   [Functionality](#functionality)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)

## Introduction

The Life Span Calculator is a web application that allows users to input their date of birth and calculates their age in years, months, days, and other time units. It is built using Python and the PyWebIO framework, providing an interactive and user-friendly experience.

## Features

-   Calculate age based on date of birth and current date.
-   Display age in years, months, days, total days, total hours, total minutes, and total seconds.
-   Responsive UI with progress bar and formatted output using PyWebIO.

## Installation

1.  Clone the repository:
    
    `git clone https://github.com/your_username/life-span-calculator.git
    cd life-span-calculator` 
    
2.  Install the required dependencies:
    
    
    `pip install pywebio` 
    

## Usage

1.  Run the application:
    
    
    `python main.py` 
    
2.  Open your web browser and navigate to http://localhost:8080/ to access the Life Span Calculator.
    
3.  Enter your date of birth in the provided input field and click "Calculate" to see your age displayed in various units.

This Python project, titled "Life Span Calculator," is a web application built using the PyWebIO framework. It allows users to calculate their age based on their date of birth and view the result in various time units (years, months, days, etc.). Here's an explanation of the components and functionalities of the project for GitHub viewers:

### Functionality:

1.  **User Input (`user_birth()` Function):**
    
    -   The `user_birth()` function prompts the user to enter their date of birth using PyWebIO's `input` function with `type=DATE`. It ensures that the entered date of birth is not in the future relative to the current year by validating against `datetime.datetime.now().year`.
2.  **Date Calculation (`calculate_age()` Function):**
    
    -   The `calculate_age()` function computes the age in years, months, days, total days, total hours, total minutes, and total seconds based on the user's date of birth and the current date. It handles edge cases where the number of months or days might need adjustment due to differences in calendar dates.
3.  **Output (`info_table()` Function):**
    
    -   The `info_table()` function displays the calculated results using PyWebIO's output functions (`put_progressbar` for a loading bar and `put_table` for a formatted table). It presents the date of birth, current date, total age, total days, total months, total hours, total minutes, and total seconds in a structured format within a table. Additionally, it includes an image fetched from an external URL to enhance the visual presentation.
4.  **Main Function (`main()` Function):**
    
    -   The `main()` function serves as the entry point of the application. It initializes the PyWebIO server, displays a welcome message (`put_html`), retrieves the user's date of birth, calculates the age, and then displays the results using the `info_table()` function.
5.  **Server Start (`start_server()` Function):**
    
    -   The `start_server()` function starts the PyWebIO server, running the `main()` function. It opens the application in the default web browser (`auto_open_webbrowser=True`) on port 8080.

### Project Usage:

-   This project can be used as a learning example for building web applications using PyWebIO, demonstrating how to handle user input, perform calculations, and display results in a user-friendly format.
-   GitHub viewers can clone the repository, explore the code, and run the application locally to understand its functionality and modify it according to their needs.

### Project Benefits:

-   **Educational:** Demonstrates integration of PyWebIO for web-based user interfaces in Python.
-   **Practical:** Provides a practical example of date manipulation and age calculation.
-   **Interactive:** Utilizes PyWebIO's interactive input and output features for a seamless user experience.
  
This README template provides a structured and informative overview of your Life Span Calculator project, helping GitHub viewers understand its purpose, features, installation steps, and how to use the application effectively. Adjust it further to fit any additional details or specifics unique to your implementation.
