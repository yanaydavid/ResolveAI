"""
Database module for Resolve AI - User registration and case management
"""
import sqlite3
from datetime import datetime
import os

DB_PATH = "resolve_ai.db"

def init_database():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            user_type TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(email),
            UNIQUE(phone)
        )
    """)

    # Cases table (updated with more fields)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            case_id TEXT PRIMARY KEY,
            claimant_name TEXT NOT NULL,
            claimant_phone TEXT NOT NULL,
            claimant_email TEXT NOT NULL,
            defendant_name TEXT NOT NULL,
            defendant_phone TEXT NOT NULL,
            claimant_file_path TEXT,
            defendant_file_path TEXT,
            status TEXT DEFAULT 'Pending',
            postal_mail_cost REAL DEFAULT 35.0,
            submission_fee REAL DEFAULT 120.0,
            resolution_fee REAL DEFAULT 200.0,
            terms_accepted BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            pdf_path TEXT
        )
    """)

    conn.commit()
    conn.close()

def create_user(full_name, phone, email, user_type='claimant'):
    """
    Create a new user in the database

    Args:
        full_name: Full name of the user
        phone: Phone number
        email: Email address
        user_type: Type of user ('claimant' or 'defendant')

    Returns:
        int: User ID if successful, None otherwise
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (full_name, phone, email, user_type)
            VALUES (?, ?, ?, ?)
        """, (full_name, phone, email, user_type))

        conn.commit()
        user_id = cursor.lastrowid
        return user_id
    except sqlite3.IntegrityError:
        # User already exists
        return None
    except Exception as e:
        print(f"Error creating user: {e}")
        return None
    finally:
        conn.close()

def get_user_by_email(email):
    """
    Retrieve a user by email

    Args:
        email: User's email address

    Returns:
        dict: User data or None if not found
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name, phone, email, user_type, created_at
        FROM users
        WHERE email = ?
    """, (email,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'id': row[0],
            'full_name': row[1],
            'phone': row[2],
            'email': row[3],
            'user_type': row[4],
            'created_at': row[5]
        }

    return None

def get_user_by_phone(phone):
    """
    Retrieve a user by phone number

    Args:
        phone: User's phone number

    Returns:
        dict: User data or None if not found
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name, phone, email, user_type, created_at
        FROM users
        WHERE phone = ?
    """, (phone,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'id': row[0],
            'full_name': row[1],
            'phone': row[2],
            'email': row[3],
            'user_type': row[4],
            'created_at': row[5]
        }

    return None

def save_case(case_id, claimant_name, claimant_phone, claimant_email, defendant_name, defendant_phone,
              claimant_file=None, defendant_file=None, pdf_path=None, terms_accepted=True,
              postal_mail_cost=35.0, submission_fee=120.0):
    """
    Save a case to the database

    Args:
        case_id: Unique case identifier
        claimant_name: Full name of the claimant
        claimant_phone: Claimant's phone number
        claimant_email: Claimant's email
        defendant_name: Full name of the defendant
        defendant_phone: Defendant's phone number
        claimant_file: Path to claimant's file (optional)
        defendant_file: Path to defendant's file (optional)
        pdf_path: Path to generated PDF (optional)
        terms_accepted: Whether terms were accepted (default True)
        postal_mail_cost: Cost of postal mail (default 35.0 ILS)
        submission_fee: Submission fee (default 120.0 ILS)

    Returns:
        bool: True if successful
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO cases (case_id, claimant_name, claimant_phone, claimant_email,
                             defendant_name, defendant_phone, claimant_file_path,
                             defendant_file_path, pdf_path, terms_accepted,
                             postal_mail_cost, submission_fee)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (case_id, claimant_name, claimant_phone, claimant_email,
              defendant_name, defendant_phone, claimant_file, defendant_file,
              pdf_path, terms_accepted, postal_mail_cost, submission_fee))

        conn.commit()
        return True
    except Exception as e:
        print(f"Error saving case: {e}")
        return False
    finally:
        conn.close()

def get_case(case_id):
    """
    Retrieve a case from the database

    Args:
        case_id: Unique case identifier

    Returns:
        dict: Case data or None if not found
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT case_id, claimant_name, claimant_phone, claimant_email,
               defendant_name, defendant_phone, claimant_file_path,
               defendant_file_path, status, postal_mail_cost, submission_fee,
               resolution_fee, terms_accepted, created_at, pdf_path
        FROM cases
        WHERE case_id = ?
    """, (case_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'case_id': row[0],
            'claimant_name': row[1],
            'claimant_phone': row[2],
            'claimant_email': row[3],
            'defendant_name': row[4],
            'defendant_phone': row[5],
            'claimant_file_path': row[6],
            'defendant_file_path': row[7],
            'status': row[8],
            'postal_mail_cost': row[9],
            'submission_fee': row[10],
            'resolution_fee': row[11],
            'terms_accepted': row[12],
            'created_at': row[13],
            'pdf_path': row[14]
        }

    return None

def get_all_cases():
    """
    Retrieve all cases from the database

    Returns:
        list: List of case dictionaries
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT case_id, claimant_name, defendant_name, status, created_at
        FROM cases
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    cases = []
    for row in rows:
        cases.append({
            'case_id': row[0],
            'claimant_name': row[1],
            'defendant_name': row[2],
            'status': row[3],
            'created_at': row[4]
        })

    return cases
