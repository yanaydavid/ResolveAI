import sqlite3
import random
import string
from datetime import datetime

DATABASE_NAME = "resolve_ai.db"

def get_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the database and create tables"""
    conn = get_connection()
    cursor = conn.cursor()

    # Create cases table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            case_id TEXT PRIMARY KEY,
            claimant_name TEXT NOT NULL,
            defendant_details TEXT,
            claim_file_path TEXT NOT NULL,
            defendant_name TEXT,
            defendant_id_number TEXT,
            defendant_agreed_arbitration INTEGER DEFAULT 0,
            defense_file_path TEXT,
            status TEXT DEFAULT 'Pending',
            mailing_cost REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def generate_case_id():
    """Generate a unique 5-digit case ID"""
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        # Generate random 5-digit number
        case_id = ''.join(random.choices(string.digits, k=5))

        # Check if it already exists
        cursor.execute("SELECT case_id FROM cases WHERE case_id = ?", (case_id,))
        if not cursor.fetchone():
            conn.close()
            return case_id

def create_case(claimant_name, claim_file_path, defendant_details="", mailing_cost=0.0):
    """Create a new case and return the case_id"""
    conn = get_connection()
    cursor = conn.cursor()

    case_id = generate_case_id()

    cursor.execute("""
        INSERT INTO cases (case_id, claimant_name, defendant_details, claim_file_path, mailing_cost)
        VALUES (?, ?, ?, ?, ?)
    """, (case_id, claimant_name, defendant_details, claim_file_path, mailing_cost))

    conn.commit()
    conn.close()

    return case_id

def get_case(case_id):
    """Get case details by case_id"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cases WHERE case_id = ?", (case_id,))
    case = cursor.fetchone()

    conn.close()
    return dict(case) if case else None

def update_case_status(case_id, status):
    """Update the status of a case"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE cases
        SET status = ?, updated_at = CURRENT_TIMESTAMP
        WHERE case_id = ?
    """, (status, case_id))

    conn.commit()
    conn.close()

def get_all_cases():
    """Get all cases"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cases ORDER BY created_at DESC")
    cases = cursor.fetchall()

    conn.close()
    return [dict(case) for case in cases]

def update_defendant_info(case_id, defendant_name, defendant_id_number, defense_file_path):
    """Update defendant information and defense file"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE cases
        SET defendant_name = ?,
            defendant_id_number = ?,
            defendant_agreed_arbitration = 1,
            defense_file_path = ?,
            status = 'In Progress',
            updated_at = CURRENT_TIMESTAMP
        WHERE case_id = ?
    """, (defendant_name, defendant_id_number, defense_file_path, case_id))

    conn.commit()
    conn.close()

# Initialize database when module is imported
init_database()
