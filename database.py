"""
Database module for Resolve AI - Simple case management
"""
import sqlite3
from datetime import datetime
import os

DB_PATH = "resolve_ai.db"

def init_database():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            case_id TEXT PRIMARY KEY,
            claimant_name TEXT NOT NULL,
            defendant_name TEXT NOT NULL,
            claimant_file_path TEXT,
            defendant_file_path TEXT,
            status TEXT DEFAULT 'Completed',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            pdf_path TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_case(case_id, claimant_name, defendant_name, claimant_file=None, defendant_file=None, pdf_path=None):
    """
    Save a case to the database

    Args:
        case_id: Unique case identifier
        claimant_name: Name of the claimant
        defendant_name: Name of the defendant
        claimant_file: Path to claimant's file (optional)
        defendant_file: Path to defendant's file (optional)
        pdf_path: Path to generated PDF (optional)

    Returns:
        bool: True if successful
    """
    init_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO cases (case_id, claimant_name, defendant_name, claimant_file_path, defendant_file_path, pdf_path)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (case_id, claimant_name, defendant_name, claimant_file, defendant_file, pdf_path))

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
        SELECT case_id, claimant_name, defendant_name, claimant_file_path,
               defendant_file_path, status, created_at, pdf_path
        FROM cases
        WHERE case_id = ?
    """, (case_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'case_id': row[0],
            'claimant_name': row[1],
            'defendant_name': row[2],
            'claimant_file_path': row[3],
            'defendant_file_path': row[4],
            'status': row[5],
            'created_at': row[6],
            'pdf_path': row[7]
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
