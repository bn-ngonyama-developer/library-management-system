#============================================================
#Name and Surname: Blessing Ngonyama
#Student Nume: 402606147
#Module: Introduction to Programming 500
#Date: 02 June 2026
#============================================================

 #============================================================
#Question 2- Repetition Structures
#============================================================

#============================================================
# QUESTION 2.1 -  Book Loan Entry Loop 
# ============================================================
#------------------------------------------------------
## DAILY LOAN ENTRY SYSTEM
#----------------------------------------------------
from datetime import datetime
#(Lutz, 2013, p. 345).

# BRANCH SELECTION
print("\n========================================")
print("       DAILY LOAN ENTRY SYSTEM")
print("========================================")
print("1. Durban Central Library")
print("2. Pinetown Public Library")
print("3. Umlazi Community Library")

branch_choice = ""
while branch_choice not in ["1", "2", "3"]:
    branch_choice = input("Select branch (1-3): ").strip()
    if branch_choice not in ["1", "2", "3"]:
        print("Invalid. Please enter 1, 2, or 3.")
           #(Matthes, 2019, p.112).
if branch_choice == "1":
    branch_name = "Durban Central Library"
elif branch_choice == "2":
    branch_name = "Pinetown Public Library"
elif branch_choice == "3":
    branch_name = "Umlazi Community Library"

print(f"\nBranch Selected: {branch_name}")
      #(Matthes, 2019, p.47).
MAX_DAILY_LOANS = 50   # 50 daily loan
         #(Lutz, 2013, p. 390).
loan_count = 0

# -------------------------------------------------------
# MAIN WHILE LOOP THAT RUNS UNTIL LIBRIARIAN TYPE EXIT OR REACHES MAX LOANS
# ----------------------------------------------------------

while loan_count < MAX_DAILY_LOANS:

    print("\n------------------------------------")
    print(f"Loans Recorded  : {loan_count}")
    print(f"Remaining Slots : {MAX_DAILY_LOANS - loan_count}")
    print("------------------------------------")

    # -----------------------------------------------------------
    # PROMPT FOR MEMBER ID (Lutz, 2013, p. 390).
    # PLACE ANY RANDOM NUMBERS FOR ID, no validation required
    # -----------------------------------------------------------
    member_id = input("Enter Member ID (or EXIT to stop): ").strip()

    if member_id.upper() == "EXIT":
        print("Loan entry session ended by librarian.")
        break

    # -----------------------------------------------------------
    # BOOK ISBN VALIDATION - nested while loop
    # PLACE ANY RANDOM NUMBERS, Must be exactly 13 digits(phyton Software Foundation, 2024).
    # -----------------------------------------------------------
    while True:
        isbn = input("Enter 13-digit ISBN: ").strip()
        if isbn.isdigit() and len(isbn) == 13:
            break
        else:
            print("Invalid ISBN. Must be exactly 13 digits. Try again.")

    # -----------------------------------------------------------
    # LOAN DATE VALIDATION - nested while loop
    # USE THESE FORMAT DD/MM/YYYY STRICTLY(Python Software Foundation, 2024).
    # -----------------------------------------------------------
    while True:
        loan_date = input("Enter loan date (DD/MM/YYYY): ").strip()

        # Check format has exactly 2 slashes
        if loan_date.count("/") != 2:
            print("Invalid format. Use DD/MM/YYYY (e.g. 15/06/2025).")
            continue

        # Try to parse the date - catches invalid days like 30/02
        try:
            valid_date = datetime.strptime(loan_date, "%d/%m/%Y")

            # Extra checks on top of strptime
            day   = valid_date.day
            month = valid_date.month
            year  = valid_date.year

            if year < 1900 or year > 2100:
                print("Invalid year. Must be between 1900 and 2100.")
                continue

            # Date passed all checks
            break

        except ValueError:
            print("Invalid date. Check day/month/year are correct (e.g. 29/02 only valid on leap years).")

    # -----------------------------------------------------------
    # LOAN COUNT AND RAIMAINING CAPACITY (Matthes, 2019, p.56).
    # -----------------------------------------------------------

    loan_count += 1

    print("\n--- Loan Successfully Recorded ---")
    print(f"Member ID  : {member_id}")
    print(f"ISBN       : {isbn}")
    print(f"Loan Date  : {loan_date}")
    print(f"Loans today: {loan_count} / {MAX_DAILY_LOANS}")
    print(f"Remaining  : {MAX_DAILY_LOANS - loan_count} slots left")
     #(Lutz, 2013, p. 387).

    #---------------------------------------------------------
    #AUTO EXIT THE LOOP WHEN THE DAILY LOAN LIMIT IS REACHED
    #----------------------------------------------------------

    if loan_count == MAX_DAILY_LOANS:
        print(f"\nMaximum daily loan limit of {MAX_DAILY_LOANS} reached. System closing.")
#------------------------------------------------        
#REFERENCES
#
# Lutz, M., 2013. Learning Python. 5th ed.
#   Sebastopol: O'Reilly Media.
#
# Matthes, E., 2019. Python Crash Course. 2nd ed.
#   San Francisco: No Starch Press.
#
# Python Software Foundation, 2024. datetime — Basic date
#   and time types. [Online] Available at:
#   https://docs.python.org/3/library/datetime.html
#   [Accessed: 28 May 2026]
#
# Python Software Foundation, 2024. Built-in Functions.
#   [Online] Available at:
#   https://docs.python.org/3/library/functions.html
#   [Accessed: 28 May 2026