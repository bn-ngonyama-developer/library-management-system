# Centralised Library Management & Fine System

## Project Description
This is a command-line library management system built using Python. The project was created for the Introduction to Programming 500 module at Richfield to show core coding logic, data validation, and automated report generation.

## Technical Tools Used
* **Language:** Python 3
* **Libraries:** `datetime` (used for checking loan dates and counting overdue days)

## Main Features of the Code
* **Input Checking:** The program checks user inputs to make sure student numbers, 13-digit ISBN numbers, and SA ID numbers are entered correctly before saving them.
* **Fine Calculator:** The system automatically calculates late fines based on different membership types (Junior, Standard, Senior, and Student), applying a R30 cap for Senior members.
* **Staff Login Levels:** Includes a simple login system with three different access levels: Librarian, Senior Librarian, and System Administrator.
* **Branch Reports:** The code counts active loans and total fines collected to print out a ranked summary report for different library branches.
