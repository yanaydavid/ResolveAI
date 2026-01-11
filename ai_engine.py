import json
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
import os

# Register Hebrew font (you'll need to have a Hebrew font file)
# For now, we'll use a fallback approach
try:
    pdfmetrics.registerFont(TTFont('Hebrew', 'Arial.ttf'))
    HEBREW_FONT = 'Hebrew'
except:
    HEBREW_FONT = 'Helvetica'

def analyze_case_mock(claim_file_path, defense_file_path, claimant_name, defendant_name):
    """
    Mock AI analysis function
    In production, this would use actual AI/NLP to analyze the PDFs

    Returns a structured JSON with the analysis
    """

    # Mock analysis - in production, this would analyze the actual PDFs
    analysis = {
        "case_summary": {
            "claimant": claimant_name,
            "defendant": defendant_name,
            "date_analyzed": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "files_analyzed": {
                "claim": os.path.basename(claim_file_path),
                "defense": os.path.basename(defense_file_path)
            }
        },
        "disputes": [
            {
                "point_of_dispute": "אי עמידה במועדי אספקה",
                "claimant_version": "הנתבע התחייב לספק את המוצרים תוך 30 יום ולא עמד בכך, מה שגרם לנזק כלכלי של 5,000 ₪",
                "defendant_version": "התעכבות נבעה מכוח עליון (מגפת קורונה) ולכן אין אחריות, כמפורט בסעיף 15 לחוזה",
                "ai_suggestion": "יש להכיר בעיכוב חלקי בשל נסיבות, אך לא בפטור מוחלט. מומלץ פיצוי של 2,500 ₪"
            },
            {
                "point_of_dispute": "איכות המוצרים שסופקו",
                "claimant_version": "המוצרים שסופקו היו פגומים ולא עמדו בתקן המוסכם",
                "defendant_version": "המוצרים עמדו בכל התקנים המוסכמים והבדיקות מאשרות זאת",
                "ai_suggestion": "לפי הראיות, המוצרים עמדו בתקן. יש לדחות טענה זו"
            },
            {
                "point_of_dispute": "הוצאות נוספות שנגרמו",
                "claimant_version": "נאלצתי לרכוש מוצרים חלופיים בעלות של 3,000 ₪",
                "defendant_version": "הרכישה הנוספת לא הייתה הכרחית ונעשתה ביוזמת התובע",
                "ai_suggestion": "חלק מההוצאות (1,500 ₪) נראות מוצדקות ויש להכיר בהן"
            }
        ],
        "final_decision": {
            "ruling": "התביעה מתקבלת בחלקה",
            "amount_awarded": 4000.0,
            "legal_expenses": 35.0,
            "total_payment": 4035.0,
            "payment_deadline_days": 30,
            "reasoning": "בהתבסס על הראיות והטיעונים, נמצא כי הנתבע אחראי באופן חלקי לנזקים שנגרמו. סכום הפיצוי משקף את האחריות היחסית ואת הנזקים המוכחים."
        }
    }

    return analysis

def generate_arbitral_award_pdf(case_data, analysis, output_path):
    """
    Generate a formal Arbitral Award PDF document

    Args:
        case_data: Dictionary with case information (case_id, claimant, defendant, etc.)
        analysis: The AI analysis result
        output_path: Path where to save the PDF
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

    # Custom styles for Hebrew (right-aligned)
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#0A2647'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName=HEBREW_FONT
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#0A2647'),
        spaceAfter=12,
        spaceBefore=12,
        alignment=TA_RIGHT,
        fontName=HEBREW_FONT
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_RIGHT,
        fontName=HEBREW_FONT,
        leading=16
    )

    # Title
    elements.append(Paragraph("פסק בוררות", title_style))
    elements.append(Paragraph("ARBITRAL AWARD", title_style))
    elements.append(Spacer(1, 0.5*cm))

    # Case Information
    case_info = f"""
    <b>מספר תיק:</b> {case_data['case_id']}<br/>
    <b>תאריך:</b> {datetime.now().strftime('%d/%m/%Y')}<br/>
    <b>התובע:</b> {case_data['claimant_name']}<br/>
    <b>הנתבע:</b> {case_data['defendant_name']}<br/>
    """
    elements.append(Paragraph(case_info, normal_style))
    elements.append(Spacer(1, 0.5*cm))

    # Introduction
    elements.append(Paragraph("הקדמה", heading_style))
    intro_text = """
    בהתאם לחוק הבוררות, התשכ"ח-1968, ולאחר בחינה מעמיקה של כתב התביעה וכתב ההגנה,
    וניתוח הראיות באמצעות מערכת Resolve AI, מתפרסם בזה פסק הבוררות הבא:
    """
    elements.append(Paragraph(intro_text, normal_style))
    elements.append(Spacer(1, 0.5*cm))

    # Disputes Analysis Table
    elements.append(Paragraph("ניתוח נקודות המחלוקת", heading_style))

    table_data = [['המלצת המערכת', 'גרסת הנתבע', 'גרסת התובע', 'נקודת מחלוקת']]

    for dispute in analysis['disputes']:
        table_data.append([
            dispute['ai_suggestion'],
            dispute['defendant_version'],
            dispute['claimant_version'],
            dispute['point_of_dispute']
        ])

    # Create table with RTL support
    dispute_table = Table(table_data, colWidths=[4*cm, 4*cm, 4*cm, 4*cm])
    dispute_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0A2647')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), HEBREW_FONT),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))

    elements.append(dispute_table)
    elements.append(Spacer(1, 0.5*cm))

    # Final Decision
    elements.append(Paragraph("ההחלטה", heading_style))
    decision = analysis['final_decision']

    decision_text = f"""
    <b>פסיקה:</b> {decision['ruling']}<br/><br/>
    <b>נימוקים:</b><br/>
    {decision['reasoning']}<br/><br/>
    """
    elements.append(Paragraph(decision_text, normal_style))
    elements.append(Spacer(1, 0.3*cm))

    # Financial Summary
    elements.append(Paragraph("סיכום כספי", heading_style))

    financial_data = [
        ['סכום', 'פריט'],
        [f"{decision['amount_awarded']:,.2f} ₪", 'סכום הפיצוי'],
        [f"{decision['legal_expenses']:,.2f} ₪", 'הוצאות משפט (כולל דמי משלוח)'],
        [f"{decision['total_payment']:,.2f} ₪", 'סה״כ לתשלום']
    ]

    financial_table = Table(financial_data, colWidths=[5*cm, 8*cm])
    financial_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7C3AED')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#F1F5F9')),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, -1), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, -1), (-1, -1), 12),
    ]))

    elements.append(financial_table)
    elements.append(Spacer(1, 0.5*cm))

    # Payment terms
    payment_text = f"""
    <b>מועד תשלום:</b> על הנתבע לשלם את מלוא הסכום תוך {decision['payment_deadline_days']} ימים
    מיום קבלת פסק בוררות זה.
    """
    elements.append(Paragraph(payment_text, normal_style))
    elements.append(Spacer(1, 1*cm))

    # Signature section
    elements.append(Paragraph("חתימות", heading_style))
    elements.append(Spacer(1, 0.5*cm))

    signature_data = [
        ['____________________', '____________________'],
        ['חתימת מערכת Resolve AI', f'תאריך: {datetime.now().strftime("%d/%m/%Y")}'],
        ['', ''],
        ['____________________', '____________________'],
        ['אישור קבלת פסק הדין - נתבע', 'אישור קבלת פסק הדין - תובע']
    ]

    sig_table = Table(signature_data, colWidths=[7*cm, 7*cm])
    sig_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), HEBREW_FONT),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
    ]))

    elements.append(sig_table)
    elements.append(Spacer(1, 1*cm))

    # Footer
    footer_text = """
    <i>פסק בוררות זה ניתן על פי חוק הבוררות, התשכ"ח-1968, ומהווה פסק דין סופי ומחייב.<br/>
    ערעור על פסק בוררות זה ניתן להגיש לבית המשפט בהתאם להוראות החוק.<br/>
    מסמך זה נוצר באמצעות מערכת Resolve AI - בוררות דיגיטלית מבוססת בינה מלאכותית.</i>
    """
    elements.append(Paragraph(footer_text, ParagraphStyle(
        'Footer',
        parent=normal_style,
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER
    )))

    # Build PDF
    doc.build(elements)

    return output_path

def get_analysis_summary_table(analysis):
    """
    Convert analysis to a formatted table for UI display
    Returns HTML table string
    """

    html = """
    <table style='width: 100%; border-collapse: collapse; direction: rtl;'>
        <thead>
            <tr style='background: #0A2647; color: white;'>
                <th style='padding: 15px; text-align: right; border: 1px solid #ddd;'>נקודת מחלוקת</th>
                <th style='padding: 15px; text-align: right; border: 1px solid #ddd;'>גרסת התובע</th>
                <th style='padding: 15px; text-align: right; border: 1px solid #ddd;'>גרסת הנתבע</th>
                <th style='padding: 15px; text-align: right; border: 1px solid #ddd;'>המלצת המערכת</th>
            </tr>
        </thead>
        <tbody>
    """

    for i, dispute in enumerate(analysis['disputes']):
        bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
        html += f"""
            <tr style='background: {bg_color};'>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top;'><b>{dispute['point_of_dispute']}</b></td>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top;'>{dispute['claimant_version']}</td>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top;'>{dispute['defendant_version']}</td>
                <td style='padding: 12px; border: 1px solid #ddd; vertical-align: top; background: #e8f5e9;'>{dispute['ai_suggestion']}</td>
            </tr>
        """

    html += """
        </tbody>
    </table>
    """

    return html
