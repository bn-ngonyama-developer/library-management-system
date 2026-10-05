=====================================================
THEKWINI METROPOLITAN LIBRARY MANAGEMENT SYSTEM
=====================================================

Student Name:   Blessing Ngonyama
Student Number: 402606174
Module:         Intro to Programming 500
Date:           02 June 2026
-----------------------------------------------------
FILES INCLUDED
-----------------------------------------------------

Question1.py        - Q1: Fine calculator and branch summary
Question 2.1.py     - Q2.1: Book loan entry loop
Question 2.2.py     - Q2.2: Monthly overdue report
Question 3.py       - Q3: Data structures (branches, loans, members)
Question 4.py       - Q4: Core system functions with test calls
Question 5.py       - Q5: includes Full integrated library system (run this)
 (just incase I also Split Question into 5 modules; Main, Loan, Member, and Report.) 
README.txt          - This file
References are included in all Document Questions at the bottom

-----------------------------------------------------
HOW TO RUN
-----------------------------------------------------

Requirements: Python 3.x

To run the full system:
    python "Question 5.py"

To run individual questions:
    python Question1.py
    python "Question 2.1.py"
    python "Question 2.2.py"
    python "Question 3.py"
    python "Question 4.py"

-----------------------------------------------------
TEST LOGIN DETAILS (Question 5)
-----------------------------------------------------

Librarian:        librarian1 / lib123
Senior Librarian: senior1    / sen123
Administrator:    admin1     / admin123

-----------------------------------------------------
DESIGN DECISIONS
-----------------------------------------------------

- Fine logic separated into strategy functions so new
  membership types can be added without changing existing code.
- Constants (rates, limits) kept at the top of each file.
- All data lives in dictionaries and lists in memory.
- Input validation helpers used throughout to prevent crashes.

-----------------------------------------------------
LIMITATIONS
-----------------------------------------------------

- Data resets when the program closes (no file storage).
- Console-based only.

-----------------------------------------------------
END OF README
-----------------------------------------------------
