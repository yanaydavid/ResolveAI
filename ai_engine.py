"""
AI Engine for Resolve AI - PDF Generation with Hebrew Support
Supports both PDF and Word (.docx) document processing
"""
import json
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
import os
import random
import hashlib

# PDF text extraction (optional, only if PyPDF2 is available)
try:
    import PyPDF2
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False
    print("Warning: PyPDF2 not available. PDF text extraction disabled.")

# Word document text extraction
try:
    from docx import Document
    DOCX_SUPPORT = True
except ImportError:
    DOCX_SUPPORT = False
    print("Warning: python-docx not available. Word document text extraction disabled.")

# Try to register Hebrew font
HEBREW_FONT = 'Helvetica'
try:
    # Try common Hebrew font paths on Linux
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf'
    ]

    for font_path in font_paths:
        if os.path.exists(font_path):
            pdfmetrics.registerFont(TTFont('HebrewFont', font_path))
            HEBREW_FONT = 'HebrewFont'
            break
except Exception as e:
    print(f"Could not register Hebrew font: {e}. Using fallback.")

def extract_text_from_pdf(file_path):
    """
    Extract text content from a PDF file

    Args:
        file_path: Path to the PDF file

    Returns:
        str: Extracted text content
    """
    if not PDF_SUPPORT:
        return "[PDF text extraction not available - PyPDF2 not installed]"

    try:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF {file_path}: {e}")
        return f"[Error extracting PDF text: {str(e)}]"

def extract_text_from_docx(file_path):
    """
    Extract text content from a Word (.docx) file

    Args:
        file_path: Path to the DOCX file

    Returns:
        str: Extracted text content
    """
    if not DOCX_SUPPORT:
        return "[Word text extraction not available - python-docx not installed]"

    try:
        doc = Document(file_path)
        text = []

        # Extract text from all paragraphs
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)

        # Extract text from tables
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text.strip():
                        text.append(cell.text)

        return "\n".join(text)
    except Exception as e:
        print(f"Error extracting text from Word document {file_path}: {e}")
        return f"[Error extracting Word text: {str(e)}]"

def extract_text_from_file(file_path):
    """
    Extract text from a file (PDF or DOCX) based on file extension

    Args:
        file_path: Path to the file

    Returns:
        str: Extracted text content
    """
    if not file_path or not os.path.exists(file_path):
        return "[File not found]"

    # Determine file type by extension
    _, ext = os.path.splitext(file_path.lower())

    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        if ext == '.doc':
            print(f"Warning: .doc files are not supported, only .docx. File: {file_path}")
            return "[.doc format not supported - please use .docx format]"
        return extract_text_from_docx(file_path)
    else:
        return f"[Unsupported file format: {ext}]"

def generate_case_id():
    """Generate a unique 5-digit case ID"""
    return str(random.randint(10000, 99999))

def analyze_case(claimant_name, defendant_name):
    """
    Analyze case and return structured JSON output

    Returns:
        dict: Structured analysis with dispute_table, mediation_proposal,
              final_verdict, reasoning, and legal_expenses
    """

    # Simulate AI analysis with realistic mock data
    analysis = {
        "case_metadata": {
            "claimant": claimant_name,
            "defendant": defendant_name,
            "date_analyzed": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "case_id": generate_case_id()
        },

        "dispute_table": [
            {
                "issue": "עיכוב במועד האספקה",
                "claimant_version": "הנתבע התחייב לספק את המוצרים תוך 30 יום ולא עמד בכך, מה שגרם לנזק כלכלי של 5,000 שקל",
                "defendant_version": "העיכוב נבע מכוח עליון (מגפת קורונה) ולכן אין אחריות, כמפורט בסעיף 15 לחוזה",
                "ai_analysis": "נמצא כי אכן היה עיכוב של 14 ימי עסקים. עם זאת, טענת כוח עליון מתקבלת רק באופן חלקי. מומלץ פיצוי של 2,500 שקל המשקף אחריות חלקית."
            },
            {
                "issue": "איכות המוצרים שסופקו",
                "claimant_version": "המוצרים שסופקו היו פגומים ולא עמדו בתקן המוסכם בהסכם",
                "defendant_version": "המוצרים עמדו בכל התקנים המוסכמים והבדיקות המצורפות מאשרות זאת",
                "ai_analysis": "לפי מסמכי הבדיקה המצורפים, המוצרים עמדו בתקן. טענת התובע נדחית בנקודה זו."
            },
            {
                "issue": "הוצאות נוספות שנגרמו לתובע",
                "claimant_version": "נאלצתי לרכוש מוצרים חלופיים בעלות של 3,000 שקל עקב העיכוב",
                "defendant_version": "הרכישה הנוספת לא הייתה הכרחית ונעשתה ביוזמת התובע ללא תיאום",
                "ai_analysis": "חלק מההוצאות (1,500 שקל) נראות סבירות והכרחיות בנסיבות העניין. יש להכיר בהן."
            }
        ],

        "mediation_proposal": {
            "proposal": "הנתבע ישלם 3,500 שקל (במקום 4,000 שקל) ובתמורה התובע יסכים לוותר על כל תביעות נוספות ולחדש את ההתקשרות העסקית לשנה נוספת בתנאים מותאמים",
            "rationale": "פשרה זו שומרת על היחסים העסקיים בין הצדדים, חוסכת הוצאות משפט נוספות, ומאפשרת המשך שיתוף פעולה פורה"
        },

        "final_verdict": {
            "verdict": "התביעה מתקבלת בחלקה",
            "amount_awarded": 4000.0,
            "legal_expenses": 35.0,
            "total_payment": 4035.0,
            "payment_deadline_days": 30
        },

        "reasoning": {
            "summary": "בהתבסס על הראיות והטיעונים, נמצא כי הנתבע אחראי באופן חלקי לנזקים שנגרמו",
            "detailed_analysis": [
                "לגבי העיכוב במועדים: נמצא כי הייתה הפרת חוזה, אך טענת כוח עליון מתקבלת באופן חלקי. העיכוב של 14 יום הוא מעבר לסביר גם בתקופת משבר.",
                "לגבי איכות המוצרים: הראיות מצביעות על כך שהמוצרים עמדו בתקנים. התביעה נדחית בנקודה זו.",
                "לגבי הוצאות נוספות: חלק מההוצאות (1,500 שקל) היו הכרחיות וסבירות בנסיבות העניין.",
                "הפיצוי הכולל (4,000 שקל) משקף אחריות יחסית של הנתבע והוא הולם את הנסיבות."
            ],
            "legal_basis": "ההחלטה ניתנה על פי חוק החוזים (חלק כללי), התשל\"ג-1973, וחוק הבוררות, התשכ\"ח-1968"
        },

        "legal_expenses": {
            "registered_mail": 35.0,
            "explanation": "דמי המשלוח בדואר רשום (35 שקל) יוחזרו לתובע כחלק מהוצאות המשפט, בהתאם לסעיף 76 לחוק בתי המשפט [נוסח משולב], התשמ\"ד-1984",
            "included_in_total": True
        }
    }

    return analysis

def generate_arbitral_award_pdf(case_data, analysis, output_path):
    """
    Generate a formal Arbitral Award PDF document with Hebrew support

    Args:
        case_data: Dictionary with case information (case_id, claimant, defendant)
        analysis: The AI analysis result with structured data
        output_path: Path where to save the PDF

    Returns:
        str: Path to generated PDF file
    """

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles with Hebrew font
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#0A2647'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName=HEBREW_FONT,
        leading=28
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#0A2647'),
        spaceAfter=15,
        spaceBefore=15,
        alignment=TA_RIGHT,
        fontName=HEBREW_FONT,
        leading=20
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_RIGHT,
        fontName=HEBREW_FONT,
        leading=18,
        wordWrap='RTL'
    )

    # Legal Header - According to Arbitration Law
    legal_header_style = ParagraphStyle(
        'LegalHeader',
        parent=normal_style,
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0A2647'),
        spaceAfter=15
    )
    elements.append(Paragraph("פסק בורר לפי חוק הבוררות, התשכ\"ח-1968", legal_header_style))
    elements.append(Paragraph("Arbitral Award pursuant to the Arbitration Law, 5728-1968", legal_header_style))
    elements.append(Spacer(1, 0.5*cm))

    # Title
    elements.append(Paragraph("ARBITRAL AWARD", title_style))
    elements.append(Paragraph("פסק בוררות", title_style))
    elements.append(Spacer(1, 0.8*cm))

    # Generate timestamp for the arbitral award
    award_timestamp = datetime.now()
    timestamp_str = award_timestamp.strftime('%d/%m/%Y %H:%M:%S')

    # Case Information Box
    case_info = f"""
    <b>Case Number / מספר תיק:</b> {case_data['case_id']}<br/>
    <b>Date & Time Issued / תאריך וזמן מתן הפסק:</b> {timestamp_str}<br/>
    <b>Claimant / התובע:</b> {case_data['claimant']}<br/>
    <b>Defendant / הנתבע:</b> {case_data['defendant']}<br/>
    """
    elements.append(Paragraph(case_info, normal_style))
    elements.append(Spacer(1, 0.8*cm))

    # Introduction
    elements.append(Paragraph("הקדמה / Introduction", heading_style))
    intro_text = """
    בהתאם לחוק הבוררות, התשכ"ח-1968, ולאחר בחינה מעמיקה של כתב התביעה וכתב ההגנה,
    וניתוח הראיות באמצעות מערכת Resolve AI, מתפרסם בזו פסק הבוררות הבא.
    <br/><br/>
    In accordance with the Arbitration Law, 5728-1968, and after thorough examination of the claim and defense documents,
    and analysis of evidence using the Resolve AI system, the following arbitral award is hereby published.
    """
    elements.append(Paragraph(intro_text, normal_style))
    elements.append(Spacer(1, 0.5*cm))

    # Objectivity Declaration
    elements.append(Paragraph("הצהרת אובייקטיביות / Declaration of Objectivity", heading_style))
    objectivity_text = """
    <b>ההכרעה התקבלה על ידי אלגוריתם בינה מלאכותית המבוסס על ניתוח עובדתי של המסמכים שהוגשו בלבד,
    ללא מגע יד אדם וללא ניגוד עניינים.</b>
    <br/><br/>
    This decision was made by an artificial intelligence algorithm based solely on factual analysis of the submitted documents,
    without human intervention and without any conflict of interest.
    <br/><br/>
    המערכת מבצעת ניתוח אוטומטי ואובייקטיבי של הטיעונים והראיות שהוצגו על ידי שני הצדדים,
    ומפיקה החלטה מבוססת על עקרונות משפטיים מקובלים וצדק טבעי.
    <br/><br/>
    The system performs automatic and objective analysis of the arguments and evidence presented by both parties,
    and produces a decision based on accepted legal principles and natural justice.
    """
    elements.append(Paragraph(objectivity_text, normal_style))
    elements.append(Spacer(1, 0.8*cm))

    # Disputes Analysis Table
    elements.append(Paragraph("ניתוח נקודות המחלוקת / Analysis of Dispute Points", heading_style))

    table_data = [
        ['ניתוח AI', 'גרסת הנתבע', 'גרסת התובע', 'נושא']
    ]

    for dispute in analysis['dispute_table']:
        table_data.append([
            dispute['ai_analysis'][:150] + '...' if len(dispute['ai_analysis']) > 150 else dispute['ai_analysis'],
            dispute['defendant_version'][:150] + '...' if len(dispute['defendant_version']) > 150 else dispute['defendant_version'],
            dispute['claimant_version'][:150] + '...' if len(dispute['claimant_version']) > 150 else dispute['claimant_version'],
            dispute['issue']
        ])

    # Create table with proper styling
    dispute_table = Table(table_data, colWidths=[4*cm, 4*cm, 4*cm, 4*cm])
    dispute_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0A2647')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), HEBREW_FONT),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))

    elements.append(dispute_table)
    elements.append(Spacer(1, 0.8*cm))

    # Mediation Proposal
    if 'mediation_proposal' in analysis:
        elements.append(Paragraph("הצעת פשרה / Mediation Proposal", heading_style))
        mediation = analysis['mediation_proposal']
        mediation_text = f"""
        <b>ההצעה / Proposal:</b> {mediation['proposal']}<br/><br/>
        <b>נימוק / Rationale:</b> {mediation['rationale']}
        """
        elements.append(Paragraph(mediation_text, normal_style))
        elements.append(Spacer(1, 0.8*cm))

    # Final Decision
    elements.append(Paragraph("ההחלטה הסופית / Final Decision", heading_style))
    decision = analysis['final_verdict']
    reasoning = analysis['reasoning']

    verdict_text = f"""
    <b>פסיקה / Ruling:</b> {decision['verdict']}<br/><br/>
    """
    elements.append(Paragraph(verdict_text, normal_style))

    # Reasoning
    elements.append(Paragraph("נימוקים / Reasoning", heading_style))
    reasoning_summary = f"<b>סיכום / Summary:</b> {reasoning['summary']}<br/><br/>"
    elements.append(Paragraph(reasoning_summary, normal_style))

    if 'detailed_analysis' in reasoning:
        for i, point in enumerate(reasoning['detailed_analysis'], 1):
            elements.append(Paragraph(f"{i}. {point}", normal_style))
            elements.append(Spacer(1, 0.3*cm))

    if 'legal_basis' in reasoning:
        legal_basis_text = f"<br/><b>בסיס משפטי / Legal Basis:</b> {reasoning['legal_basis']}"
        elements.append(Paragraph(legal_basis_text, normal_style))

    elements.append(Spacer(1, 0.8*cm))

    # Financial Summary
    elements.append(Paragraph("סיכום כספי / Financial Summary", heading_style))

    legal_exp = analysis.get('legal_expenses', {})
    legal_exp_amount = legal_exp.get('registered_mail', decision.get('legal_expenses', 35.0))

    financial_data = [
        ['סכום / Amount', 'פריט / Item'],
        [f"{decision['amount_awarded']:,.2f} ₪", 'סכום הפיצוי / Compensation Amount'],
        [f"{legal_exp_amount:.2f} ₪", 'דמי משלוח דואר רשום / Registered Mail Fee'],
        [f"{decision['total_payment']:,.2f} ₪", 'סה"כ לתשלום / Total Payment']
    ]

    financial_table = Table(financial_data, colWidths=[6*cm, 8*cm])
    financial_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7C3AED')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#F1F5F9')),
        ('GRID', (0, 0), (-1, -1), 1.5, colors.black),
        ('FONTNAME', (0, -1), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, -1), (-1, -1), 12),
        ('FONTWEIGHT', (0, -1), (-1, -1), 'BOLD'),
    ]))

    elements.append(financial_table)
    elements.append(Spacer(1, 0.8*cm))

    # Payment terms
    payment_text = f"""
    <b>מועד תשלום / Payment Deadline:</b> על הנתבע לשלם את מלוא הסכום תוך {decision['payment_deadline_days']} ימים
    מיום קבלת פסק בוררות זה.
    <br/><br/>
    The defendant must pay the full amount within {decision['payment_deadline_days']} days
    from the date of receiving this arbitral award.
    """
    elements.append(Paragraph(payment_text, normal_style))
    elements.append(Spacer(1, 1.2*cm))

    # Authentication Appendix / Judge's Explanatory Page
    elements.append(Paragraph("נספח אימות - דף הסבר לשופט / Authentication Appendix", heading_style))

    auth_text = f"""
    <b>שורת אימות טכנולוגית / Technological Authentication:</b><br/>
    מסמך זה הופק במערכת Resolve AI לאחר ששני הצדדים אישרו את הסכם הבוררות.
    התובע הגיש את התביעה והנתבע הגיש את כתב ההגנה דרך הפלטפורמה הדיגיטלית.
    <br/><br/>
    This document was produced in the Resolve AI system after both parties confirmed the arbitration agreement.
    The claimant submitted the claim and the defendant submitted the defense through the digital platform.
    <br/><br/>
    <b>תיעוד הגישה / Access Documentation:</b><br/>
    הנתבע נכנס למערכת באמצעות קוד גישה ייחודי (מספר תיק: {case_data['case_id']}) שנשלח אליו ב-SMS,
    ואישר את השתתפותו בהליך הבוררות הדיגיטלי.
    <br/><br/>
    The defendant accessed the system using a unique access code (Case No: {case_data['case_id']}) sent via SMS,
    and confirmed participation in the digital arbitration process.
    <br/><br/>
    <b>תאריכי אישור / Confirmation Dates:</b><br/>
    מערכת Resolve AI שומרת את תיעוד המועדים המדויקים בהם כל צד ביצע את פעולותיו במערכת,
    כולל העלאת מסמכים ואישור תנאי הבוררות.
    <br/><br/>
    The Resolve AI system maintains precise records of when each party performed their actions in the system,
    including document uploads and confirmation of arbitration terms.
    """
    elements.append(Paragraph(auth_text, normal_style))
    elements.append(Spacer(1, 0.8*cm))

    # Signature section
    elements.append(Paragraph("חתימות / Signatures", heading_style))
    elements.append(Spacer(1, 0.5*cm))

    signature_data = [
        ['____________________', '____________________'],
        ['Resolve AI System Signature', f'תאריך / Date: {award_timestamp.strftime("%d/%m/%Y")}'],
        ['', ''],
        ['____________________', '____________________'],
        ['אישור קבלה - נתבע', 'אישור קבלה - תובע'],
        ['Defendant Acknowledgment', 'Claimant Acknowledgment']
    ]

    sig_table = Table(signature_data, colWidths=[7*cm, 7*cm])
    sig_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))

    elements.append(sig_table)
    elements.append(Spacer(1, 1.2*cm))

    # Generate document hash for verification
    hash_content = f"{case_data['case_id']}|{case_data['claimant']}|{case_data['defendant']}|{timestamp_str}|{decision['amount_awarded']}|{decision['total_payment']}"
    doc_hash = hashlib.sha256(hash_content.encode('utf-8')).hexdigest()

    # Hash verification section
    hash_style = ParagraphStyle(
        'HashStyle',
        parent=normal_style,
        fontSize=9,
        textColor=colors.HexColor('#0A2647'),
        alignment=TA_CENTER,
        leading=14,
        spaceBefore=10,
        spaceAfter=10
    )

    hash_text = f"""
    <b>קוד אימות (Hash) / Verification Code:</b><br/>
    {doc_hash}<br/>
    <i>קוד ייחודי לאימות שלמות המסמך / Unique code to verify document integrity</i>
    """
    elements.append(Paragraph(hash_text, hash_style))
    elements.append(Spacer(1, 0.5*cm))

    # Footer
    footer_text = """
    <i>This arbitral award is issued in accordance with the Arbitration Law, 5728-1968, and constitutes a final and binding judgment.<br/>
    An appeal against this arbitral award may be submitted to the court in accordance with the provisions of the law.<br/>
    This document was created using the Resolve AI system - AI-powered digital arbitration.</i>
    <br/><br/>
    <i>Pesaq borerot ze nitan al pi Hoq Haborerut, Hashtsa'h-1968, umehave pesaq din sofi umhaiyv.<br/>
    Arur al pesaq borerot ze nitan lehagish lebeit hamishpat behatamaa lehoraut hahoq.<br/>
    Mismakh ze notzar beemtzaut maarekhet Resolve AI - borerot digitali mesubeset binah meluakhtit.</i>
    """
    elements.append(Paragraph(footer_text, ParagraphStyle(
        'Footer',
        parent=normal_style,
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER,
        leading=12
    )))

    # Build PDF
    try:
        doc.build(elements)
        return output_path
    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise

def get_analysis_summary_html(analysis):
    """
    Convert analysis to formatted HTML for UI display with proper RTL and styling

    Args:
        analysis: The analysis dictionary

    Returns:
        str: HTML formatted analysis summary
    """

    # Build dispute table with dark blue header and zebra stripes
    html = """
    <div style='margin: 30px 0;'>
        <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
            📊 ניתוח נקודות המחלוקת
        </h3>
        <table style='width: 100%; border-collapse: collapse; direction: rtl; box-shadow: 0 10px 40px rgba(0,0,0,0.1);'>
            <thead>
                <tr style='background: #0A2647; color: white;'>
                    <th style='padding: 15px; text-align: right; border: 1px solid #ddd; font-size: 1.1rem;'>נושא</th>
                    <th style='padding: 15px; text-align: right; border: 1px solid #ddd; font-size: 1.1rem;'>גרסת התובע</th>
                    <th style='padding: 15px; text-align: right; border: 1px solid #ddd; font-size: 1.1rem;'>גרסת הנתבע</th>
                    <th style='padding: 15px; text-align: right; border: 1px solid #ddd; font-size: 1.1rem;'>ניתוח AI</th>
                </tr>
            </thead>
            <tbody>
    """

    # Add zebra-striped rows
    for i, dispute in enumerate(analysis['dispute_table']):
        bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
        html += f"""
            <tr style='background: {bg_color};'>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top; text-align: right; direction: rtl;'><b>{dispute['issue']}</b></td>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top; text-align: right; direction: rtl;'>{dispute['claimant_version']}</td>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top; text-align: right; direction: rtl;'>{dispute['defendant_version']}</td>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top; background: #e8f5e9; text-align: right; direction: rtl;'>{dispute['ai_analysis']}</td>
            </tr>
        """

    html += """
            </tbody>
        </table>
    </div>
    """

    # Mediation Proposal with RTL
    if 'mediation_proposal' in analysis:
        mediation = analysis['mediation_proposal']
        html += f"""
        <div style='background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
                    padding: 30px; border-radius: 20px; color: white; margin: 30px 0;
                    box-shadow: 0 10px 40px rgba(251,191,36,0.4);'>
            <h3 style='font-size: 1.8rem; margin-bottom: 15px; text-align: center;'>🤝 הצעת פשרה</h3>
            <div style='background: rgba(255,255,255,0.15); padding: 20px; border-radius: 12px; text-align: right; direction: rtl;'>
                <p style='margin-bottom: 15px; line-height: 1.8; font-size: 1.1rem;'>
                    <b>ההצעה:</b><br/>{mediation['proposal']}
                </p>
                <p style='line-height: 1.8; font-size: 1.1rem;'>
                    <b>נימוק:</b><br/>{mediation['rationale']}
                </p>
            </div>
        </div>
        """

    # Final Verdict - Green card with centered header and RTL reasoning
    decision = analysis['final_verdict']
    reasoning = analysis.get('reasoning', {})

    # Build reasoning text
    reasoning_html = ""
    if reasoning:
        reasoning_html = f"<b>סיכום:</b> {reasoning.get('summary', '')}<br/><br/>"

        if 'detailed_analysis' in reasoning:
            reasoning_html += "<b>ניתוח מפורט:</b><br/>"
            for i, point in enumerate(reasoning['detailed_analysis'], 1):
                reasoning_html += f"{i}. {point}<br/>"

        if 'legal_basis' in reasoning:
            reasoning_html += f"<br/><b>בסיס משפטי:</b> {reasoning['legal_basis']}"

    html += f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                    padding: 30px; border-radius: 20px; color: white; margin: 30px 0;
                    box-shadow: 0 10px 40px rgba(16,185,129,0.4);'>
            <h3 style='font-size: 2rem; margin-bottom: 15px; text-align: center;'>📜 ההחלטה הסופית</h3>
            <p style='font-size: 1.3rem; text-align: center; margin-bottom: 20px;'><b>{decision['verdict']}</b></p>

            <div style='background: rgba(255,255,255,0.15); padding: 20px; border-radius: 12px; text-align: right; direction: rtl; margin-bottom: 20px;'>
                <p style='line-height: 1.8; font-size: 1.1rem;'>
                    <b>נימוקים:</b><br/><br/>
                    {reasoning_html}
                </p>
            </div>

            <div style='background: rgba(255,255,255,0.15); padding: 20px; border-radius: 12px;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px; direction: rtl;'>
                    <span style='font-size: 1.1rem;'>סכום הפיצוי:</span>
                    <span style='font-size: 1.2rem; font-weight: bold;'>{decision['amount_awarded']:,.0f} ₪</span>
                </div>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px; direction: rtl;'>
                    <span style='font-size: 1.1rem;'>הוצאות משפט (דמי משלוח):</span>
                    <span style='font-size: 1.2rem; font-weight: bold;'>{decision['legal_expenses']:.0f} ₪</span>
                </div>
                <hr style='border: none; border-top: 2px solid rgba(255,255,255,0.3); margin: 15px 0;'>
                <div style='display: flex; justify-content: space-between; direction: rtl;'>
                    <span style='font-size: 1.2rem;'><b>סה״כ לתשלום:</b></span>
                    <span style='font-size: 1.5rem; font-weight: bold;'>{decision['total_payment']:,.0f} ₪</span>
                </div>
                <p style='text-align: center; margin-top: 15px; font-size: 0.95rem;'>
                    תשלום תוך {decision['payment_deadline_days']} ימים
                </p>
            </div>
        </div>
    """

    return html
