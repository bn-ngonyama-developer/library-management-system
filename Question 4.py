#============================================================
#Name and Surname: Blessing Ngonyama
#Student Nume: 402606147
#Module: Introduction to Programming 500
#Date: 02 June 2026
#============================================================


# ============================================================
#QUESTION 4: FUNCTIONS AND MODULAR DESIGN
#======================================================
from datetime import datetime
#(Python Software Foundation, 2024).
#-------------------------------------------------------
# QUSTION 4.1 — CORE SYSTEM FUNCTIONS (https://docs.python.org/3/functions.html).
# ------------------------------------------------------

JUNIOR_RATE    = 1.00
STANDARD_RATE  = 2.50
SENIOR_RATE    = 1.00
SENIOR_CAP     = 30.00
STUDENT_RATE   = 1.50

JUNIOR_LIMIT   = 3
STANDARD_LIMIT = 5
SENIOR_LIMIT   = 8
STUDENT_LIMIT  = 10

LOAN_PERIODS = { #(Lutz, 2013, p. 213).
    "Junior":   14,
    "Standard": 21,
    "Senior":   30,
    "Student":  21
}

LOAN_LIMITS = {
    "Junior":   JUNIOR_LIMIT,
    "Standard": STANDARD_LIMIT,
    "Senior":   SENIOR_LIMIT,
    "Student":  STUDENT_LIMIT
}

#------------------------------------------------------------------
# CALCULATION_OF_FINE()
#------------------------------------------------------------------
#(Lutz, 2013, p. 472)
def calculate_fine(membership_type: str, days_overdue: int,
                   num_books: int, first_offence: bool = False) -> float:
    """
    Calculate and return the total fine for a member.
    Delegates to the correct strategy function based on membership type (Lutz, 2013, p. 472).
    Parameters:
        membership_type (str): "Junior", "Standard", "Senior", or "Student"
        days_overdue    (int): How many days the book(s) are overdue
        num_books       (int): Number of overdue books
        first_offence  (bool): True if this is a Junior's first offence

    Returns:
        float: Total fine amount in Rands
    """
    if membership_type == "Junior":
        return junior_fine(days_overdue, first_offence)
    elif membership_type == "Standard":
        return standard_fine(days_overdue, num_books)
    elif membership_type == "Senior":
        return senior_fine(days_overdue, num_books)
    elif membership_type == "Student":
        return student_fine(days_overdue, num_books)
    else:
        print(f"[ERROR] Unknown membership type: {membership_type}")
        return 0.00

 #============================================================
# ISSUE_LOAN()
# ============================================================
def issue_loan(loan_records: list, members: dict, branches: dict,
               member_id: str, isbn: str, issue_date: str) -> dict | None:
    """
    Issue a loan after validating member eligibility and branch capacity.(Matthes, 2019, p. 112).

    Parameters:
        loan_records (list): The global list of loan records
        members      (dict): The global members dictionary
        branches     (dict): The global branches dictionary
        member_id    (str) : The member's ID
        isbn         (str) : 13-digit ISBN of the book being issued
        issue_date   (str) : Date in DD/MM/YYYY format

    Returns:
        dict | None: The new loan record dict, or None if blocked
    """
    # --- Member existence check ---(Lutz, 2013, p. 213).
    if member_id not in members:
        print(f"[ISSUE LOAN] Error: Member {member_id} not found.")
        return None

    member = members[member_id]

    # --- Member status check ---
    if member["status"] != "Active":
        print(f"[ISSUE LOAN] Error: Member {member_id} account is {member['status']}.")
        return None

    # --- Outstanding fines check, blocks if is over R50.00 ---
    if member["outstanding_fines"] > 50.00:
        print(f"[ISSUE LOAN] Error: Member {member_id} has outstanding fines of "
              f"R{member['outstanding_fines']:.2f}. Must be under R50.00 to borrow.")
        return None

    # --- Loan limit check ---
    #(Lutz, 2013, p. 213).
    limit = LOAN_LIMITS.get(member["membership_type"], 5)
    if len(member["active_loans"]) >= limit:
        print(f"[ISSUE LOAN] Error: Member {member_id} has reached their loan limit of {limit}.")
        return None

    # --- Branch capacity check ---
    branch_code = member["branch"]
    if branch_code not in branches:
        print(f"[ISSUE LOAN] Error: Branch {branch_code} not found.")
        return None

    branch = branches[branch_code]
    if branch["active_loans"] >= branch["max_daily_loans"]:
        print(f"[ISSUE LOAN] Error: Branch {branch_code} has reached its daily loan limit.")
        return None

    # --- Build the new loan record ---
    #(Python Software Foundation, 2024).
    issue_dt   = datetime.strptime(issue_date, "%d/%m/%Y")
    period     = LOAN_PERIODS.get(member["membership_type"], 21)
    due_dt     = issue_dt + __import__("datetime").timedelta(days=period)
    due_date   = due_dt.strftime("%d/%m/%Y")

    # Assign next loan ID
    loan_id = max((loan["loan_id"] for loan in loan_records), default=0) + 1

    new_loan = {
        "loan_id"     : loan_id,
        "member_id"   : member_id,
        "isbn"        : isbn,
        "branch_code" : branch_code,
        "issue_date"  : issue_date,
        "due_date"    : due_date,
        "return_date" : "",
        "days_overdue": 0,
        "fine_amount" : 0.00,
        "fine_paid"   : False
    }

    loan_records.append(new_loan)
    member["active_loans"].append(isbn)
    branch["active_loans"] += 1

    print(f"\n[ISSUE LOAN] Loan {loan_id} issued to {member['name']}.")
    print(f"             ISBN: {isbn} | Due: {due_date}")
    return new_loan

 #============================================================
# PROCESS_RETURN()
# ============================================================
def process_return(loan_records: list, members: dict,
                   member_id: str, isbn: str, return_date: str) -> float:
    """
    Find the active loan, compute the fine, update the record
    and the member's outstanding balance.

    Parameters:
        loan_records (list): The global list of loan records
        members      (dict): The global members dictionary
        member_id    (str) : The member's ID
        isbn         (str) : 13-digit ISBN of the returned book
        return_date  (str) : Date in DD/MM/YYYY format

    Returns:
        float: Fine amount owed, or -1.0 if loan not found
    """
    for loan in loan_records:
        if (loan["member_id"] == member_id and
                loan["isbn"] == isbn and
                loan["return_date"] == ""):

            loan["return_date"] = return_date
            due      = datetime.strptime(loan["due_date"],  "%d/%m/%Y")
            returned = datetime.strptime(return_date,        "%d/%m/%Y")
            overdue_days = (returned - due).days

            if overdue_days > 0:
                loan["days_overdue"] = overdue_days
                member = members.get(member_id, {})
                m_type = member.get("membership_type", "Standard") #(Lutz, 2013, p. 472).
                fine   = calculate_fine(m_type, overdue_days, 1)
                loan["fine_amount"] = fine
                if member:
                    member["outstanding_fines"] += fine
            else:
                loan["days_overdue"] = 0
                loan["fine_amount"]  = 0.00
                fine = 0.00

            # Remove ISBN from member active loans (Python Software Foundation, 2024).
            member = members.get(member_id)
            if member and isbn in member["active_loans"]:
                member["active_loans"].remove(isbn)

            print(f"\n[RETURN] Loan returned: {member_id} | ISBN: {isbn}")
            print(f"         Days overdue : {loan['days_overdue']}")
            print(f"         Fine amount  : R{loan['fine_amount']:.2f}")
            return loan["fine_amount"]

    print(f"\n[RETURN] No active loan found for member {member_id} with ISBN {isbn}.")
    return -1.0


# ============================================================
# AUTHENTICATE_STAFF()
# ============================================================
def authenticate_staff(staff_accounts: dict, username: str,
                       password: str) -> dict | None:
    """
    Validate staff login credentials.

    Parameters:
        staff_accounts (dict): The global staff accounts dictionary
        username       (str) : Entered username
        password       (str) : Entered password

    Returns:
        dict | None: {"role": ..., "full_name": ...} on success, None on failure
    """
    if username in staff_accounts:
        account = staff_accounts[username]
        if account["password"] == password:
            print(f"\n[AUTH] Login successful. Welcome {account['full_name']} "
                  f"({account['role']}).")
            return {"role": account["role"], "full_name": account["full_name"]}
    print("\n[AUTH] Login failed. Invalid username or password.")
    return None


# ============================================================
# GENERATE_BRANCH_REPORT()
# ============================================================
def generate_branch_report(loan_records: list, members: dict,
                            branch_code: str) -> dict:
    """
    Generate and return a summary report for a specific branch.

    Parameters:
        loan_records (list): The global list of loan records
        members      (dict): The global members dictionary
        branch_code  (str) : Branch code to report on

    Returns:
        dict: {
            "total_loans"    : int,
            "active_loans"   : int,
            "overdue_count"  : int,
            "fines_issued"   : float,
            "fines_collected": float,
            "avg_duration"   : float  (days, returned loans only)
        }
    """
    total_loans     = 0
    active_loans    = 0
    overdue_count   = 0
    fines_issued    = 0.00
    fines_collected = 0.00
    durations       = []

    for loan in loan_records:
        if loan["branch_code"] != branch_code:
            continue

        total_loans += 1

        if loan["return_date"] == "":
            active_loans += 1
        else:
            # Calculate loan duration in days (Python Software Foundation, 2024).
            issue    = datetime.strptime(loan["issue_date"],  "%d/%m/%Y")
            returned = datetime.strptime(loan["return_date"], "%d/%m/%Y")
            durations.append((returned - issue).days)

        if loan["days_overdue"] > 0:
            overdue_count += 1
            fines_issued  += loan["fine_amount"]
            if loan["fine_paid"]:
                fines_collected += loan["fine_amount"]
                #(Matthes, 2019, p. 120).

    avg_duration = round(sum(durations) / len(durations), 1) if durations else 0.0

    report = {
        "total_loans"    : total_loans,
        "active_loans"   : active_loans,
        "overdue_count"  : overdue_count,
        "fines_issued"   : fines_issued,
        "fines_collected": fines_collected,
        "avg_duration"   : avg_duration
    }

    print(f"\n[REPORT] Branch {branch_code}")
    print(f"  Total Loans     : {report['total_loans']}")
    print(f"  Active Loans    : {report['active_loans']}")
    print(f"  Overdue         : {report['overdue_count']}")
    print(f"  Fines Issued    : R{report['fines_issued']:.2f}")
    print(f"  Fines Collected : R{report['fines_collected']:.2f}")
    print(f"  Avg Duration    : {report['avg_duration']} days")

    return report

# ============================================================
# QUESTION 4.2 — FINE RATE STRATEGY FUNCTIONS
# ============================================================

#-------------------------------------------------------------
#JUNIOR_FINE
#-----------------------------------------------------------
def junior_fine(days_overdue: int, first_offence: bool) -> float:
    """
    Calculate fine for a Junior member.
    First offence = R0.00. After that, R1.00/day. (Matthes, 2019, p. 130).
    """
    if first_offence:
        return 0.00
    return days_overdue * JUNIOR_RATE

#-------------------------------------------------------------
#STANDARD_FINE
#-------------------------------------------------------------
def standard_fine(days_overdue: int, num_books: int) -> float:
    """
    Calculate fine for a Standard member.
    R2.50 per day per book. No cap.
    (matthes, 2019, p. 130).
    """
    return days_overdue * STANDARD_RATE * num_books


#-------------------------------------------------------------
#SENIOR_FINE
#-------------------------------------------------------------
def senior_fine(days_overdue: int, num_books: int) -> float:
    """
    Calculate fine for a Senior member.
    R1.00 per day per book, capped at R30.00 per book.
    (matthes, 2019, p. 95).
    """
    fine_per_book = days_overdue * SENIOR_RATE
    if fine_per_book > SENIOR_CAP:
        fine_per_book = SENIOR_CAP
    return fine_per_book * num_books


#-------------------------------------------------------------
#STUDENT_FINE
#-------------------------------------------------------------
def student_fine(days_overdue: int, num_books: int) -> float:
    """
    Calculate fine for a Student member.
    R1.50 per day per book. No cap.
    (matthes, 2019, p. 130).
    """
    return days_overdue * STUDENT_RATE * num_books

# ============================================================
# SAMPLE DATA FOR TESTING
# ============================================================
loan_records = [
    {"loan_id": 1, "member_id": "M001", "isbn": "9780747532699",
     "branch_code": "DBN001", "issue_date": "01/05/2026", "due_date": "22/05/2026",
     "return_date": "28/05/2026", "days_overdue": 6, "fine_amount": 9.00, "fine_paid": False},
    {"loan_id": 2, "member_id": "M002", "isbn": "9780439023481",
     "branch_code": "PIN002", "issue_date": "05/05/2026", "due_date": "26/05/2026",
     "return_date": "", "days_overdue": 0, "fine_amount": 0.00, "fine_paid": False},
    {"loan_id": 3, "member_id": "M003", "isbn": "9780261103573",
     "branch_code": "DBN001", "issue_date": "10/05/2026", "due_date": "24/05/2026",
     "return_date": "30/05/2026", "days_overdue": 6, "fine_amount": 6.00, "fine_paid": True},
]

members = {
    "M001": {"name": "Ayanda Sithole", "sa_id": "0001015001088", "contact": "083111",
             "email": "a@a.com", "branch": "DBN001", "membership_type": "Student",
             "status": "Active", "active_loans": [], "outstanding_fines": 9.00},
    "M002": {"name": "Bongani Mnisi", "sa_id": "9005105002083", "contact": "082222",
             "email": "b@b.com", "branch": "PIN002", "membership_type": "Standard",
             "status": "Active", "active_loans": ["9780439023481"], "outstanding_fines": 0.00},
    "M003": {"name": "Sipho Cele", "sa_id": "8803065003081", "contact": "071333",
             "email": "c@c.com", "branch": "DBN001", "membership_type": "Senior",
             "status": "Active", "active_loans": [], "outstanding_fines": 0.00},
    "M004": {"name": "Overdue Member", "sa_id": "7001015004082", "contact": "060444",
             "email": "d@d.com", "branch": "DBN001", "membership_type": "Standard",
             "status": "Active", "active_loans": [], "outstanding_fines": 60.00},
}

branches = {
    "DBN001": {"name": "Durban Central Library", "address": "45 Anton Lembede St",
               "librarian": "Mr. Ngonyama", "catalogue_size": 12000,
               "max_daily_loans": 50, "active_loans": 10},
    "PIN002": {"name": "Pinetown Public Library", "address": "41 Kings Road",
               "librarian": "Mr. Thwala", "catalogue_size": 7500,
               "max_daily_loans": 30, "active_loans": 5},
}

staff_accounts = {
    "Ngonyama": {"password": "lib123", "role": "Librarian",
                "full_name": "Mr. Ngonyama", "branch": "DBN001"},
    "Thwala": {"password": "sen123", "role": "Senior Librarian",
                "full_name": "Mr. Thwala", "branch": "PIN002"},
    "admin01": {"password": "admin123", "role": "System Administrator",
                "full_name": "Mrs. Peterson", "branch": "UML003"},
}

# ============================================================
# TEST CALLS
# ============================================================
print("=" * 60)
print("Q4 — FUNCTION TESTS")
print("=" * 60)

# Test calculate_fine — all four types
print("\n--- calculate_fine() tests ---")
print(f"Junior  (first):  R{calculate_fine('Junior',   5, 1, first_offence=True):.2f}")
print(f"Junior  (repeat): R{calculate_fine('Junior',   5, 1, first_offence=False):.2f}")
print(f"Standard:         R{calculate_fine('Standard', 5, 2):.2f}")
print(f"Senior  (capped): R{calculate_fine('Senior',  40, 2):.2f}")
print(f"Student:          R{calculate_fine('Student',  7, 3):.2f}")

# Test issue_loan — valid
print("\n--- issue_loan() tests ---")
issue_loan(loan_records, members, branches, "M003", "9780131103627", "27/05/2026")

# Test issue_loan — blocked (fines > R50)
issue_loan(loan_records, members, branches, "M004", "9780131103628", "27/05/2026")

# Test process_return
print("\n--- process_return() tests ---")
process_return(loan_records, members, "M002", "9780439023481", "30/05/2026")

# Test process_return — not found
process_return(loan_records, members, "M999", "0000000000000", "27/05/2026")

# Test authenticate_staff
print("\n--- authenticate_staff() tests ---")
authenticate_staff(staff_accounts, "Ngonyama", "lib123")
authenticate_staff(staff_accounts, "Ngonyama", "wrongpassword")

# Test generate_branch_report
print("\n--- generate_branch_report() tests ---")
generate_branch_report(loan_records, members, "DBN001")
generate_branch_report(loan_records, members, "PIN002")

#-----------------------------------------------------------------------------------
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
#   [Accessed: 28 May 2026]