#============================================================
#Name and Surname: Blessing Ngonyama
#Student Nume: 402606147
#Module: Introduction to Programming 500
#Date: 02 June 2026
#============================================================

#Question 3 - Data Structures in Python 
#============================================================



# ============================================================
# QUESTION 3.1 — Library Data Mode
# ============================================================

from datetime import datetime, timedelta

# -----------------------------------------------------------------
# BRANCHES DICTIONARY #(Lutz, 2013, p. 218).
# ---------------------------------------------------------------
branches = {
    "DBN001": {
        "name"           : "Durban Central Library",
        "address"        : "45 Anton Lembede St, Durban CBD",
        "librarian"      : "Ms N. Mkhize",
        "catalogue_size" : 12000,
        "max_daily_loans": 50,
        "active_loans"   : 340
    },
    "PIN002": {
        "name"           : "Pinetown Public Library",
        "address"        : "41 Kings Road, Pinetown",
        "librarian"      : "Mr S. Pillay",
        "catalogue_size" : 7500,
        "max_daily_loans": 30,
        "active_loans"   : 210
    },
    "UML003": {
        "name"           : "Umlazi Community Library",
        "address"        : "Section V, Umlazi Township",
        "librarian"      : "Ms T. Zungu",
        "catalogue_size" : 5800,
        "max_daily_loans": 20,
        "active_loans"   : 150
    },
}

# -----------------------------------------------------------
# LOAN RECORDS LIST (Matthes, 2019, p. 92).
# ----------------------------------------------------------
loan_records = [
    {
        "loan_id"     : 1,
        "member_id"   : "M001",
        "isbn"        : "9780747532699",
        "branch_code" : "DBN001",
        "issue_date"  : "01/05/2026",
        "due_date"    : "21/05/2026",
        "return_date" : "25/05/2026",
        "days_overdue": 4,
        "fine_amount" : 10.00,
        "fine_paid"   : False
    },
    {
        "loan_id"     : 2,
        "member_id"   : "M002",
        "isbn"        : "9780439023481",
        "branch_code" : "PIN002",
        "issue_date"  : "05/05/2026",
        "due_date"    : "25/05/2026",
        "return_date" : "",
        "days_overdue": 0,
        "fine_amount" : 0.00,
        "fine_paid"   : False
    },
    {
        "loan_id"     : 3,
        "member_id"   : "M003",
        "isbn"        : "9780261103573",
        "branch_code" : "UML003",
        "issue_date"  : "10/05/2026",
        "due_date"    : "30/05/2026",
        "return_date" : "",
        "days_overdue": 0,
        "fine_amount" : 0.00,
        "fine_paid"   : False
    },
]

# -----------------------------------------------------------
#  ADD A NEW LOAN RECORD (Python Software Foundation, 2024).
# ----------------------------------------------------------
def add_loan(loan_records, loan_id, member_id, isbn, branch_code, issue_date, due_date):
    """Add a new loan record to the loan_records list."""
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
    print(f"\n[ADD LOAN] Loan ID {loan_id} added for member {member_id}.")
    return new_loan

# -----------------------------------------------------------
# UPDATE ON RETURN (Python Software Foundation, 2024).
# -----------------------------------------------------------
def update_on_return(loan_records, loan_id, return_date):
    """Update a loan record when a book is returned."""
    for loan in loan_records:
        if loan["loan_id"] == loan_id:
            loan["return_date"] = return_date
            due      = datetime.strptime(loan["due_date"],    "%d/%m/%Y")
            returned = datetime.strptime(return_date,          "%d/%m/%Y")
            overdue  = (returned - due).days
            if overdue > 0:
                loan["days_overdue"] = overdue
                loan["fine_amount"]  = overdue * 2.50
            else:
                loan["days_overdue"] = 0
                loan["fine_amount"]  = 0.00
            print(f"\n[RETURN] Loan ID {loan_id} updated.")
            print(f"         Days overdue : {loan['days_overdue']}")
            print(f"         Fine amount  : R{loan['fine_amount']:.2f}")
            return loan
    print(f"\n[RETURN] Loan ID {loan_id} not found.")
    return None

#-----------------------------------------------------------------
# SEARCH BY MEMBER ID (Lutz, 2013, p. 470).
#-----------------------------------------------------------------
def search_by_member(loan_records, member_id):
    """Return all loan records for a given member ID."""
    results = [loan for loan in loan_records if loan["member_id"] == member_id]
    if results:
        print(f"\n[SEARCH] Loans for member {member_id}:")
        for loan in results:
            returned = loan['return_date'] if loan['return_date'] else 'Not yet returned'
            print(f"  Loan {loan['loan_id']} | ISBN: {loan['isbn']} | "
                  f"Branch: {loan['branch_code']} | Due: {loan['due_date']} | "
                  f"Returned: {returned}")
    else:
        print(f"\n[SEARCH] No loans found for member {member_id}.")
    return results

# ============================================================
# FILTER ACTIVE LOANS BY BRANCH (Lutz, 2013, p. 470).
# ============================================================
def filter_active_by_branch(loan_records, branch_code):
    """Return all active (not yet returned) loans for a given branch."""
    active = [
        loan for loan in loan_records
        if loan["branch_code"] == branch_code and loan["return_date"] == ""
    ]
    if active:
        print(f"\n[ACTIVE LOANS] Branch {branch_code}:")
        for loan in active:
            print(f"  Loan {loan['loan_id']} | Member: {loan['member_id']} | "
                  f"ISBN: {loan['isbn']} | Due: {loan['due_date']}")
    else:
        print(f"\n[ACTIVE LOANS] No active loans found for branch {branch_code}.")
    return active

# ============================================================================================================


#============================================================================================================
# QUESTION 3.2 - MEMBER AND STAFF ACCOUNTS
#============================================================================================================


#------------------------------------------------------------
# MEMBERS DICTIONARY (min. 8 members)
#------------------------------------------------------------
#(Matthes, 2019, p. 92)
members = {
    "M001": {
        "name"           : "Ayanda Sithole",
        "sa_id"          : "0001015001088",
        "contact"        : "0831234567",
        "email"          : "ayanda@email.com",
        "branch"         : "DBN001",
        "membership_type": "Student",
        "status"         : "Active",
        "active_loans"   : ["9780747532699"],
        "outstanding_fines": 10.00
    },
    "M002": {
        "name"           : "Bongani Mnisi",
        "sa_id"          : "9005105002083",
        "contact"        : "0829876543",
        "email"          : "bongani@email.com",
        "branch"         : "PIN002",
        "membership_type": "Standard",
        "status"         : "Active",
        "active_loans"   : ["9780439023481"],
        "outstanding_fines": 0.00
    },
    "M003": {
        "name"           : "Nobuhle Mkhize",
        "sa_id"          : "8803065003081",
        "contact"        : "0711112233",
        "email"          : "nobuhle@email.com",
        "branch"         : "UML003",
        "membership_type": "Junior",
        "status"         : "Active",
        "active_loans"   : ["9780261103573"],
        "outstanding_fines": 0.00
    },
    "M004": {
        "name"           : "Dumisani Cele",
        "sa_id"          : "5501015004082",
        "contact"        : "0834445566",
        "email"          : "dumisani@email.com",
        "branch"         : "DBN001",
        "membership_type": "Senior",
        "status"         : "Active",
        "active_loans"   : [],
        "outstanding_fines": 25.00
    },
    "M005": {
        "name"           : "Hlengiwe Ntuli",
        "sa_id"          : "0102025005089",
        "contact"        : "0607778899",
        "email"          : "hlengiwe@email.com",
        "branch"         : "PIN002",
        "membership_type": "Student",
        "status"         : "Active",
        "active_loans"   : [],
        "outstanding_fines": 0.00
    },
    "M006": {
        "name"           : "Sipho Ngobeni",
        "sa_id"          : "9210105006086",
        "contact"        : "0822223344",
        "email"          : "sipho@email.com",
        "branch"         : "UML003",
        "membership_type": "Standard",
        "status"         : "Suspended",
        "active_loans"   : [],
        "outstanding_fines": 75.00
    },
    "M007": {
        "name"           : "Angelina Muadi",
        "sa_id"          : "0804085007083",
        "contact"        : "0611234567",
        "email"          : "angelina@email.com",
        "branch"         : "DBN001",
        "membership_type": "Junior",
        "status"         : "Active",
        "active_loans"   : [],
        "outstanding_fines": 0.00
    },
    "M008": {
        "name"           : "Mzwakhe Ngoma",
        "sa_id"          : "4906035008080",
        "contact"        : "0839990011",
        "email"          : "mzwakhe@email.com",
        "branch"         : "PIN002",
        "membership_type": "Senior",
        "status"         : "Active",
        "active_loans"   : [],
        "outstanding_fines": 5.00
    },
}
#---------------------------------------------------------
# STAFF ACCOUNTS DICTIONARY (one per role)
#---------------------------------------------------------
#(Matthes, 2019, p. 56).
staff_accounts = {
    "nmkhize": {
        "password" : "lib@2026",
        "role"     : "Librarian",
        "full_name": "Ms N. Mkhize",
        "branch"   : "DBN001"
    },
    "spillay": {
        "password" : "senior@2026",
        "role"     : "Senior Librarian",
        "full_name": "Mr S. Pillay",
        "branch"   : "PIN002"
    },
    "admin01": {
        "password" : "admin@2026",
        "role"     : "System Administrator",
        "full_name": "Ms T. Zungu",
        "branch"   : "UML003"
    },
}

#------------------------------------------------------------------
# REGISTER A MEMBER (reject duplicate SA ID)
#----------------------------------------------------------------
#(Lutz, 2013, p. 213).
def register_member(members, member_id, name, sa_id, contact, email,
                    branch, membership_type):
    """Register a new member. Rejects duplicate SA IDs."""
    # Check for duplicate SA ID
    for existing in members.values():
        if existing["sa_id"] == sa_id:
            print(f"\n[REGISTER] Error: SA ID {sa_id} is already registered.")
            return None
    members[member_id] = {
        "name"            : name,
        "sa_id"           : sa_id,
        "contact"         : contact,
        "email"           : email,
        "branch"          : branch,
        "membership_type" : membership_type,
        "status"          : "Active",
        "active_loans"    : [],
        "outstanding_fines": 0.00
    }
    print(f"\n[REGISTER] Member {name} ({member_id}) registered successfully.")
    return members[member_id]

# ============================================================
# AUTHENTICATE STAFF LOGIN (Lutz, 2013, p. 230).
# ============================================================
def authenticate_staff(staff_accounts, username, password):
    """Validate staff credentials. Returns staff dict or None."""
    if username in staff_accounts:
        account = staff_accounts[username]
        if account["password"] == password:
            print(f"\n[LOGIN] Welcome, {account['full_name']} ({account['role']}).")
            return {"role": account["role"], "full_name": account["full_name"]}
    print("\n[LOGIN] Invalid username or password.")
    return None

# ============================================================
# LIST UNIQUE MEMBERSHIP TYPES USING A SET
# ============================================================
def list_membership_types(members):
    """Return and display the unique membership types across all members."""
    types = {member["membership_type"] for member in members.values()}
    print("\n[MEMBERSHIP TYPES] Unique types registered:", types)
    return types

# ============================================================
#REFERENCES (Harvard Style):
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
# Python Software Foundation, 2024. Built-in Types.
#   [Online] Available at:
#   https://docs.python.org/3/library/stdtypes.html
#   [Accessed: 28 May 2026]
#
