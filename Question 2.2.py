#============================================================
#Name and Surname: Blessing Ngonyama
#Student Nume: 402606147
#Module: Introduction to Programming 500
#Date: 02 June 2026
#============================================================


# ============================================================
# QUESTION 2.2 — MONTHLY OVERDUE REPORT
# ============================================================

print("\n============================================================")
print("        MONTHLY OVERDUE REPORT — ALL BRANCHES")
print("============================================================")

#(Matthes, 2019, p.55).
branch_names = [
    "Durban Central Library",
    "Pinetown Public Library",
    "Umlazi Community Library"
]
branch_codes = ["DBN001", "PIN002", "UML003"]

#---------------------------------------------------------------------------------
#CODED LIST OF 6 LOAN RECORDS PER BRANCH
#LEACH RECORD HAVE 4 FIELDS: MEMBER NAME, MEMBERSHIP TYPE, BOOK TITLE, DAYS OVERDUE
#---------------------------------------------------------------------------------
#(Lutz, 2013, p. 218)
loans_per_branch = {
    "DBN001": [
        ["Ayanda Sithole",       "Student",  "Harry Potter",          5],
        ["Bongani Mnisi",        "Standard", "The Alchemist",         0],
        ["Jack Mabaso",          "Standard", "Sapiens",              19],
        ["Ntombifuthi Mahlenge", "Standard", "Atomic Habits",         7],
        ["Doris Shezi",          "Senior",   "Man's Search for Meaning", 0],
        ["Alwande Mvala",        "Student",  "Rich Dad Poor Dad",     3]
    ],
    "PIN002": [
        ["Mzwakhe Ngoma",   "Senior",   "Long Walk to Freedom",  5],
        ["Nobuhle Mkhize",  "Junior",   "Charlotte's Web",        0],
        ["Hleziphi Khumo",  "Student",  "The Great Gatsby",       8],
        ["Dumisani Cele",   "Senior",   "Things Fall Apart",     10],
        ["Hlengiwe Ntuli",  "Student",  "1984",                   2],
        ["Sipho Ngobeni",   "Junior",   "Alice in Wonderland",    0]
    ],
    "UML003": [
        ["Angelina Muadi",        "Junior",   "The Lion, the Witch", 6],
        ["John Peterson",         "Senior",   "War and Peace",        0],
        ["Bandile Shandu",        "Standard", "Brave New World",      4],
        ["Thokozane Hlope",       "Standard", "Lord of the Flies",    0],
        ["Sikhumbuzo Hlongwane",  "Senior",   "Crime and Punishment", 10],
        ["Sibongile Mpanza",      "Junior",   "The Little Prince",    0]
    ]
}

# -------------------------------------------------------------------------------
#(Matthes, 2019, p.47). — FINE RATES PER MEMBERSHIP TYPE AND SENIOR CAP
FINE_RATES = {
    "Junior":   1.00,
    "Standard": 2.50,
    "Senior":   1.00,
    "Student":  1.50
}
SENIOR_CAP = 30.00
#--------------------------------------------------------------------------------

branch_totals = [] #(Lutz, 2013, p. 218). — list to store total fines per branch for ranked summary

# OUTER LOOP — each branch (Phython Software Foundation, 2024)
for code_index in range(len(branch_codes)):
    branch_code = branch_codes[code_index]
    branch_name = branch_names[code_index]

    print("\n------------------------------------------------------------")
    print(f"Branch: {branch_name} ({branch_code})")
    print("------------------------------------------------------------")
    print(f"{'Member':<22} {'Type':<10} {'Book Title':<25} {'Days':>5} {'Fine':>10}")

    total_fines   = 0
    overdue_count = 0

    # INNER LOOP — records in each branch (Lutz, 2013, p.312)
    for record in loans_per_branch[branch_code]:
        member_name     = record[0]
        membership_type = record[1]
        book_title      = record[2]
        days_overdue    = record[3]

        #--------------------------------------------
        # COONTIUE TO SKIP WHERE DAYS_OVER DUE IS ZERO
        #---------------------------------------------
        if days_overdue == 0: #(Lutz, 2013, p. 390).
            continue

 
        #--------------------------------------------
        #OVERDUE COUNT AND TOTAL FINE CAALCULATIONS
        #-------------------------------------------
        #(Matthes, 2019, p.47)
        rate = FINE_RATES[membership_type]
        fine = days_overdue * rate

    
        if membership_type == "Senior" and fine > SENIOR_CAP:
            fine = SENIOR_CAP

        total_fines   += fine
        overdue_count += 1

        print(f"{member_name:<22} {membership_type:<10} {book_title:<25} {days_overdue:>5} R{fine:>8.2f}") #Matthes, 2019, p. 120)
    
    #AVAERAGE FINE CALCULATION
    average_fine = total_fines / overdue_count if overdue_count > 0 else 0

    branch_totals.append([branch_name, total_fines])

    print("------------------------------------------------------------")
    print(f"Overdue Books : {overdue_count}")
    print(f"Total Fines   : R{total_fines:.2f}")
    print(f"Average Fine  : R{average_fine:.2f}")

# ============================================================
# RANKED SUMMARY FROM HIGHEST TO LOWEST TOTAL FINES#(Lutz, 2013, p. 412).
# ============================================================
print("\n============================================================")
print("      RANKED SUMMARY — HIGHEST TO LOWEST FINES")
print("============================================================")

branch_totals.sort(key=lambda x: x[1], reverse=True)#(phython Software Foundation, 2024).

for rank, item in enumerate(branch_totals, start=1):
    print(f"{rank}. {item[0]:<30} R{item[1]:.2f}")

print("============================================================")
#-------------------------------------------------------------------------
 #REFERENCES 
#
# Lutz, M., 2013. Learning Python. 5th ed.
#   Sebastopol: O'Reilly Media.
#
# Matthes, E., 2019. Python Crash Course. 2nd ed.
#   San Francisco: No Starch Press.
#
# Python Software Foundation, 2024. Built-in Functions.
#   [Online] Available at:
#   https://docs.python.org/3/library/functions.html
#   [Accessed: 28 May 2026]