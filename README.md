# Centralised Library Management & Fine System

## Project Overview
This is a command-line library management system built using Python 3 for the Introduction to Programming 500 module at Richfield. The project demonstrates core programming logic, data structure design, and automated backend reporting.

## Technical Stack
* **Language:** Python 3
* **Core Libraries:** `datetime` and `timedelta` (used for calculating date deltas and overdue timelines)

## Key Technical Features
* **Input Validation:** The program uses conditional logic and try/except blocks to check user inputs. It verifies that 13-digit ISBN numbers, SA ID numbers, and date formats (DD/MM/YYYY) are correct before processing transactions.
* **Fine Calculator:** The system automatically calculates late return fines based on user classes (Junior, Standard, Senior, and Student), enforcing specific rules and fine caps (like the R30 cap for Senior members).
* **Role-Based Login Access:** Features a secure login system that routes users into three different administrative menus based on their staff role: Librarian, Senior Librarian, and System Administrator.
* **Data & Performance Reporting:** The codebase tracks active loans and total fines across different branches to generate ranked summary reports from highest to lowest metrics.
