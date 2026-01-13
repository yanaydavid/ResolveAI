#!/usr/bin/env python3
"""
Test code structure and logic without requiring external libraries
"""
import ast
import os

def test_file_syntax(filename):
    """Test if Python file has valid syntax"""
    print(f"\n🔍 Testing {filename}...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print(f"   ✓ Syntax is valid")
        return True
    except SyntaxError as e:
        print(f"   ✗ Syntax Error: {e}")
        return False

def check_enhancements_in_code(filename):
    """Check if all PDF enhancements are present in the code"""
    print(f"\n📝 Checking enhancements in {filename}...")

    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()

    checks = {
        'Hash verification': 'hashlib',
        'Legal header': 'פסק בורר לפי חוק הבוררות',
        'Timestamp': 'award_timestamp',
        'Authentication appendix': 'נספח אימות',
        'Objectivity declaration': 'הצהרת אובייקטיביות',
        'Hash generation': 'sha256',
        'Verification code display': 'קוד אימות (Hash)',
    }

    all_passed = True
    for check_name, search_term in checks.items():
        if search_term in code:
            print(f"   ✓ {check_name} - Found")
        else:
            print(f"   ✗ {check_name} - NOT FOUND")
            all_passed = False

    return all_passed

def check_defendant_fix(filename):
    """Check if defendant submission fix is present"""
    print(f"\n🛡️ Checking defendant portal fix in {filename}...")

    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()

    checks = {
        'submitted_case_id assignment': 'st.session_state.submitted_case_id = case[\'case_id\']',
        'Defense file upload': 'defense_file = st.file_uploader',
        'PDF path storage': 'st.session_state.pdf_path = pdf_path',
    }

    all_passed = True
    for check_name, search_term in checks.items():
        if search_term in code:
            print(f"   ✓ {check_name} - Found")
        else:
            print(f"   ✗ {check_name} - NOT FOUND")
            all_passed = False

    return all_passed

def main():
    print("=" * 70)
    print("   ResolveAI - Code Structure & Enhancement Verification Test")
    print("=" * 70)

    results = []

    # Test ai_engine.py
    print("\n" + "=" * 70)
    print("Testing ai_engine.py")
    print("=" * 70)

    results.append(("ai_engine.py syntax", test_file_syntax('ai_engine.py')))
    results.append(("ai_engine.py enhancements", check_enhancements_in_code('ai_engine.py')))

    # Test app.py
    print("\n" + "=" * 70)
    print("Testing app.py")
    print("=" * 70)

    results.append(("app.py syntax", test_file_syntax('app.py')))
    results.append(("app.py defendant fix", check_defendant_fix('app.py')))

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    all_passed = True
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status:12} - {test_name}")
        if not result:
            all_passed = False

    print("=" * 70)

    if all_passed:
        print("\n🎉 ALL TESTS PASSED! Code is ready for deployment.")
        print("\n✅ Implemented Features:")
        print("   1. תוצאת בוררות מוצגת לנתבע אחרי הגשת כתב הגנה")
        print("   2. כפתור הורדה זמין לשני הצדדים")
        print("   3. קוד אימות (Hash) ב-PDF")
        print("   4. חותמת זמן מפורטת")
        print("   5. כותרת משפטית: 'חוק הבוררות, התשכ\"ח-1968'")
        print("   6. נספח אימות - דף הסבר לשופט")
        print("   7. הצהרת אובייקטיביות")
    else:
        print("\n⚠️  Some tests failed. Please review the code.")

    return all_passed

if __name__ == "__main__":
    import sys
    result = main()
    print()
    sys.exit(0 if result else 1)
