# Source Code Explanation

1.  **Import Necessary Libraries**
    

    
    ```
    from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from datetime import datetime
    import win10toast
    ``` 
    
    -   `reportlab` is used for creating PDF documents.
    -   `datetime` is used to get the current date and time.
    -   `win10toast` is used for showing desktop notifications on Windows.
2.  **Define `store_products` Function**

    
    ```
    def store_products():
        print('=====> WELCOME TO MY-SCHOOL <=====')
	``` 
    
    -   This function displays available courses, allows the user to purchase them, and generates a receipt in PDF format.
3.  **Initialize Default Courses**
    

    
    ```
    default_courses = [
        ...
    ]
    ``` 
    
    -   This list contains dictionaries representing different courses available for purchase. Each dictionary includes the course name, duration, access type, and price.
4.  **Display Available Courses**
    

    
    ```
    for i, data in enumerate(default_courses, start=0):
        print(f'--> Course : {i}')
        ...
      ``` 
    
    -   This loop prints the details of each available course with an index.
5.  **Initialize Template for Receipt**
    
  
    
    ```
    templete = [
        ['Date', 'Name', 'Duration', 'Access', 'Price']
    ]
    ``` 
    
    -   This list will be used to store the details of the purchased courses and will be used to generate the PDF receipt.
6.  **Start Purchasing Loop**
    
 
    
	   ```
    course_index = -1
    parchasing = True
    totalFee = 0
    discount = 3000
    while(parchasing):
        ...
      ``` 
    
    -   This loop allows the user to select courses to purchase. It continues until the user decides to exit.
7.  **Get User Input for Course Selection**
    

    
    ```
    buy_course = int(input("Which Course Do you wan to Buy (0, 1, 2....) : "))
    if(buy_course > len(default_courses)):
        ...
       ``` 
    
    -   The user inputs the index of the course they want to purchase. If the index is invalid, an error message is displayed.
8.  **Add Selected Course to Template**
    

    
    ```
    course = default_courses[buy_course]
    current_date = datetime.now()
    formated_time = current_date.strftime('%d/%m/%Y')
    buy_date = [{'date': formated_time}]
    date = buy_date[0]
                
    templete.append([
        date['date'],
        course['Course'],
        course['Duration'],
        course['Access'],
        course['Price']
    ])
    ...
    ``` 
    
    -   The selected course details, along with the current date, are added to the `templete` list.
9.  **Calculate Total Fee**
    
    ```
    if course['Price'] != 'Free':
        totalFee += course['Price']
	  ``` 
    
    -   The total fee is calculated by summing the prices of all purchased courses, excluding free courses.
    
10.  **Exit Option**

	  ```
			exit = input("\nDo you want to exit (0 - exit - No) : ")
	    if(exit == 'exit' or exit == '0'):
	        parchasing = False
	  ```

-   The user can choose to exit the purchasing loop by entering '0' or 'exit'.
  
11.  **Add Discount and Total Fee to Template**

  ```
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
  ```
  
  -   The discount and total fee (after discount) are added to the `templete` list.
    
12.  **Generate PDF Receipt**

```
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
        ...
    )
    table = Table(templete, style=style)
    pdf.build([title, table])
``` 
    
  -   A PDF receipt is created using `reportlab`. The receipt includes a title and a table with the details of the purchased courses.
  -   A desktop notification is shown to inform the user that the receipt is ready.
    
13.  **Call the Function**
    

    
    `store_products()` 
    

### How to Use

1.  **Run the Script**
    
    -   Simply run the script using a Python interpreter.
    -   The script will display the available courses and prompt you to select which courses you want to buy.
2.  **Select Courses**
    
    -   Enter the index number of the course you wish to purchase.
    -   Continue selecting courses until you are done. Enter '0' or 'exit' to stop purchasing.
3.  **Generate Receipt**
    
    -   Once you exit the purchasing loop, a PDF receipt will be generated and saved as `Receipt.pdf` in the current directory.
    -   A desktop notification will inform you that the receipt is ready.

### Features

-   **Course Listing**: Displays a list of available courses with details.
-   **Course Selection**: Allows users to select multiple courses to purchase.
-   **Receipt Generation**: Generates a PDF receipt with the details of the purchased courses.
-   **Discount Calculation**: Applies a discount to the total fee.
-   **Desktop Notification**: Notifies the user when the receipt is ready.

This explanation should help GitHub viewers understand how the function works and how to use it. Feel free to customize the explanation further based on your specific needs.
