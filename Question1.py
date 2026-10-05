#============================================================
#Name and Surname: Blessing Ngonyama
#Student Nume: 402606147
#Module: Introduction to Programming 500
#Date: 02 June 2026
#============================================================


# ============================================================
# QUESTION 1.1 — Library Fine Calculator  
# ============================================================
#-------------------------
# MEMBERSHIP MENU
#------------------------

# (Python Software Foundation, 2024).
print("===== MEMBERSHIP TYPE MENU =====")
print("1. Junior (under 18)")
print("2. Senior (60 and over)")
print("3. Standard")
print("4. Student")

option = ""
while option not in ["1", "2", "3", "4"]:
    option = input("Enter option (1-4): ").strip()
    if option not in ["1", "2", "3", "4"]:
        print("Invalid option. Please enter 1, 2, 3, or 4.")

# ------------------------------------------------------------
# LOAN LIMIT CONSTANTS (Matthes, 2019, p. 47).
# ------------------------------------------------------------
JUNIOR_LIMIT   = 3
STANDARD_LIMIT = 5
SENIOR_LIMIT   = 8
STUDENT_LIMIT  = 10
# ------------------------------------------------------------
# AGE VALIDATION(Lutz, 2013, p. 387).
# ------------------------------------------------------------

if option == "1":#(Matthes, 2019, p. 112).
    while True:
        age = int(input("Enter your age: "))
        if 0 <= age < 18:
            break
        print("Error: Junior members must be under 18. Please re-enter.")
    membership_type = "Junior" #JUNIOR HAVE TO UNDER 18 YEARS OLD
    loan_limit = JUNIOR_LIMIT
    print("Junior membership selected.")

elif option == "2":#(Matthes, 2019, p. 112).
    while True:
        age = int(input("Enter your age: "))
        if age >= 60:
            break
        print("Error: Senior members must be 60 or older. Please re-enter.")
    membership_type = "Senior" #SENIOR HAVE TO 60 YEARS OLD OR OLDER
    loan_limit = SENIOR_LIMIT
    print("Senior membership selected.")

elif option == "3":
    membership_type = "Standard"
    loan_limit = STANDARD_LIMIT
    print("Standard membership selected.")

elif option == "4":
    membership_type = "Student"
    loan_limit = STUDENT_LIMIT
    print("Student membership selected.")

# ----------------------------------------------------------
#DAYS OVERDUE & NUMBER OF BOOKS OVERDUE INPUT(Python Software Foundation, 2024).
#--------------------------------------------------------------

days_overdue = int(input("\nEnter days overdue: "))
num_books    = int(input("Enter number of overdue books: "))


# Loan limit check with re-prompt (Lutz, 2013, p. 390).
while num_books > loan_limit:
    print(f"\nWarning: {membership_type} members can only borrow {loan_limit} books.")
    print(f"You entered {num_books}. Please re-enter.")
    num_books = int(input("Enter number of overdue books: "))

# --------------------------------------------------------------
# FINE CALCULATION #(Matthes, 2019, p. 95).
# -------------------------------------------------------------

JUNIOR_RATE    = 1.00
STANDARD_RATE  = 2.50
SENIOR_RATE    = 1.00
SENIOR_CAP     = 30.00 # Maximum fine per book for Senior members
STUDENT_RATE   = 1.50


if membership_type == "Junior":
     #First offence: R0.00. Subsequent offences: R1.00/day
    # (Lutz, 2013, p. 392).
    first_offence = input("Is this the first offence? (Y/N): ").strip().upper()
    if first_offence == "Y":
        fine_per_book = 0.00
    else:
        fine_per_book = days_overdue * JUNIOR_RATE
    total_fine = fine_per_book * num_books

elif membership_type == "Standard":
    fine_per_book = days_overdue * STANDARD_RATE
    total_fine    = fine_per_book * num_books

elif membership_type == "Senior":
     # Senior rate: R1.00 per day per book, capped at R30.00
    # Comparison operator used to apply cap (Matthes, 2019, p. 95).
    fine_per_book = days_overdue * SENIOR_RATE
    if fine_per_book > SENIOR_CAP:
        fine_per_book = SENIOR_CAP
    total_fine = fine_per_book * num_books

elif membership_type == "Student":
    fine_per_book = days_overdue * STUDENT_RATE
    total_fine    = fine_per_book * num_books

# ============================================================
#FINE PER BOOK, TOTAL FINE(Matthes, 2019, p. 68). AND MEMBERSHIP TYPE APPLIED (Python Software Foundation, 2024.).
# ============================================================

print("\n===== FINE SUMMARY =====")
print("Membership Type :", membership_type)
print("Days Overdue    :", days_overdue)
print("Books Overdue   :", num_books)
print(f"Fine Per Book   : R{fine_per_book:.2f}")
print(f"Total Fine      : R{total_fine:.2f}")

# ============================================================
# QUESTION 1.2 — Branch Collection Summary 
# ============================================================
#--------------------------------------------
#  BRANCH SELECTION
#--------------------------------------------

branch_1_name       = "Durban Central Library"
branch_1_collection = 12000
branch_1_loans      = 0
branch_1_fines      = 0.0

branch_2_name       = "Pinetown Public Library"
branch_2_collection = 7500
branch_2_loans      = 0
branch_2_fines      = 0.0

branch_3_name       = "Umlazi Community Library"
branch_3_collection = 5800
branch_3_loans      = 0
branch_3_fines      = 0.0

# BRANCH SELECTION MENU
#(Lutz, 2013, p. 345)
print("\n===== SELECT BRANCH =====")
print("1.", branch_1_name)
print("2.", branch_2_name)
print("3.", branch_3_name)

branch_choice = ""
while branch_choice not in ["1", "2", "3"]:
    branch_choice = input("Enter branch (1-3): ").strip()
    if branch_choice not in ["1", "2", "3"]:
        print("Invalid branch. Please enter 1, 2, or 3.")


#-----------------------------------------------------------
# ACTIVE LOANS AND FINES COLLECTED PER BRANCH(Matthes, 2019, p. 112).
#-------------------------------------------------------------
if branch_choice == "1":
    branch_1_loans += 1
    branch_1_fines += total_fine
elif branch_choice == "2":
    branch_2_loans += 1
    branch_2_fines += total_fine
elif branch_choice == "3":
    branch_3_loans += 1
    branch_3_fines += total_fine

#--------------------------------------------------------------------------------
# CALCULATION OF LOAN PERCENTAGES (TO 2 DECIMAL PLACES)
#-----------------------------------------------------------------------------
# Percentage formula: (loans / collection) * 100
# round() built-in used to limit to 2 decimal places
# (Python Software Foundation, 2024).
branch_1_loan_percent = round((branch_1_loans / branch_1_collection) * 100, 2)
branch_2_loan_percent = round((branch_2_loans / branch_2_collection) * 100, 2)
branch_3_loan_percent = round((branch_3_loans / branch_3_collection) * 100, 2)


#---------------------------------------------------------------
#SUMMARY TABLE: BRANCH NAME | COLLECTION | LOANS | LOAN % | FINES
#---------------------------------------------------------------
# Column alignment uses f-string format specifiers described
# in Python Software Foundation (2024) and Matthes (2019, p. 68).
print("\n===== BRANCH COLLECTION SUMMARY =====")
print(f"{'Branch Name':<30} {'Collection':>12} {'Loans':>8} {'Loan %':>8} {'Fines':>12}")
print("-" * 75)
print(f"{branch_1_name:<30} {branch_1_collection:>12} {branch_1_loans:>8} {branch_1_loan_percent:>7}% {'R'+str(round(branch_1_fines,2)):>12}")
print(f"{branch_2_name:<30} {branch_2_collection:>12} {branch_2_loans:>8} {branch_2_loan_percent:>7}% {'R'+str(round(branch_2_fines,2)):>12}")
print(f"{branch_3_name:<30} {branch_3_collection:>12} {branch_3_loans:>8} {branch_3_loan_percent:>7}% {'R'+str(round(branch_3_fines,2)):>12}")
print("-" * 75)

#--------------------------------------------------------------------------------
# IDENTIFY AND DISPLAY BRANCH WITH HIGHEST LOAN PERCENTAGE(Matthes, 2019, p. 95).
#-------------------------------------------------------------------------------
highest_percent = branch_1_loan_percent
highest_branch  = branch_1_name

if branch_2_loan_percent > highest_percent:
    highest_percent = branch_2_loan_percent
    highest_branch  = branch_2_name

if branch_3_loan_percent > highest_percent:
    highest_percent = branch_3_loan_percent
    highest_branch  = branch_3_name


print(f"Branch with highest loan percentage: {highest_branch} at {highest_percent}%")
#------------------------------------------------------------------------------------
#
# REFERENCES (Harvard Style):
#
# Lutz, M., 2013. Learning Python. 5th ed.
#   Sebastopol: O'Reilly Media.

# Matthes, E., 2019. Python Crash Course. 2nd ed.
#   San Francisco: No Starch Press.
#
# Python Software Foundation, 2024. Built-in Functions.
#   [Online] Available at:
#   https://docs.python.org/3/library/functions.html
#   [Accessed: 28 May 2026]
#
# Python Software Foundation, 2024. Input and Output.
#   [Online] Available at:
#   https://docs.python.org/3/tutorial/inputoutput.html
#   [Accessed: 28 May 2026]
# ============================================================