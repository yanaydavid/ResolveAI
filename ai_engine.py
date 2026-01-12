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
                "issue": "Delay in delivery - Ai aemidah bemoadi aspaqa",
                "claimant_version": "Hanitba hithaiv lesapeq et hamutarim tokh 30 yom velo amad bekha, ma shegaram lenezek calkali shel 5,000 shekel",
                "defendant_version": "Hateakhavut navaa mikoah alion (magefat corona) velakhen ain ahariut, kmefurat basaif 15 lahoze",
                "ai_analysis": "Nimtza ki akhen haita iteakhavut shel 14 ymei asakim. Im zat, taanat koah haalion mequbelet raq beofen helqi. Mumlatz pitzui shel 2,500 shekel hamesaqef ahariut helqit."
            },
            {
                "issue": "Quality of delivered products - Aikhut hamutarim shesupqu",
                "claimant_version": "Hamutarim shesupqu haiu pgumim velo amdu btaqan hamusakm baheskem",
                "defendant_version": "Hamutarim amdu bekhol hataqanim hamusaqmim vehbediqot hamtzurpot maasherot zat",
                "ai_analysis": "Lefi mismakhi habediqa hametzurpim, hamutarim amdu btaqan. Taanat hatovea nidheit bneqoda zo."
            },
            {
                "issue": "Additional expenses - Hotzaot nosfot shenigrmu latovea",
                "claimant_version": "Nealatzti lirqosh mutarim halufim balut shel 3,000 shekel eqev haaikhub",
                "defendant_version": "Harekhisha hanosefet lo haita hekhrahit venaasa beyotzmat hatovea lelo tiaum",
                "ai_analysis": "Heleq mehaotzaot (1,500 shekel) niraot sevirot vehekhrahiot benasibut hainian. Yesh lehakir bhen."
            }
        ],

        "mediation_proposal": {
            "proposal": "Mediation proposal: Hanitba yeshalem 3,500 shekel (bimqom 4,000 shekel) uvtmura hatovea yaskym levater al kol tbiuot nosfot velhadesh et hitqashrut asakit leshana nosefet bitnuaim mutavim",
            "rationale": "Pshra zo shomeret al hayehasim haiskiyim ben hatzadim, hosekhet hotzaot mishpat nosfot, vemaapsheret hamshekh shituf peula poreh"
        },

        "final_verdict": {
            "verdict": "Hatebia mitqabelet behelqa",
            "amount_awarded": 4000.0,
            "legal_expenses": 35.0,
            "total_payment": 4035.0,
            "payment_deadline_days": 30
        },

        "reasoning": {
            "summary": "Behitbasesut al haraut vehatiunim, nimtza ki hanitba aharai beofen helqi laneqezim shengrmu",
            "detailed_analysis": [
                "Regarding the delay in deadlines: Found that there was a breach of contract, but the force majeure claim is partially accepted. The 14-day delay is beyond reasonable even during crisis period.",
                "Regarding product quality: Evidence indicates products met standards. Claim rejected.",
                "Regarding additional expenses: Some expenses (1,500 shekel) were necessary and reasonable in the circumstances.",
                "Total compensation (4,000 shekel) reflects proportional liability of defendant and is appropriate given circumstances."
            ],
            "legal_basis": "Hahahlata nitna al pi Hoq Hahotzim (heleq clali), Hashla'g-1973, veHoq Haborerut, Hashtsa'h-1968"
        },

        "legal_expenses": {
            "registered_mail": 35.0,
            "explanation": "Demi hamishloah bedoar rashum (35 shekel) yuhzru latovea keheleq mehotzaot hamishpat, behataama lsaif 76 leHoq Batei Hamishpat [nosah meshulab], Hashtsa'd-1984",
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

    # Title
    elements.append(Paragraph("ARBITRAL AWARD", title_style))
    elements.append(Paragraph("Pesaq Borerot", title_style))
    elements.append(Spacer(1, 0.8*cm))

    # Case Information Box
    case_info = f"""
    <b>Case Number / Mispar Tik:</b> {case_data['case_id']}<br/>
    <b>Date / Tarikh:</b> {datetime.now().strftime('%d/%m/%Y')}<br/>
    <b>Claimant / Hatovea:</b> {case_data['claimant']}<br/>
    <b>Defendant / Hanitba:</b> {case_data['defendant']}<br/>
    """
    elements.append(Paragraph(case_info, normal_style))
    elements.append(Spacer(1, 0.8*cm))

    # Introduction
    elements.append(Paragraph("Introduction / Haqdama", heading_style))
    intro_text = """
    In accordance with the Arbitration Law, 5728-1968, and after thorough examination of the claim and defense documents,
    and analysis of evidence using the Resolve AI system, the following arbitral award is hereby published.
    <br/><br/>
    Behataama leHoq Haborerut, Hashtsa'h-1968, veleahar behina mamiqa shel ktav hatebia vektav hagana,
    venituah harauot beemtzaut maarekhet Resolve AI, mitparses bezo pesaq haborerut haba.
    """
    elements.append(Paragraph(intro_text, normal_style))
    elements.append(Spacer(1, 0.8*cm))

    # Disputes Analysis Table
    elements.append(Paragraph("Analysis of Dispute Points / Nituah Neqodot Hamahloqut", heading_style))

    table_data = [
        ['AI Analysis', 'Defendant Version', 'Claimant Version', 'Issue']
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
        elements.append(Paragraph("Mediation Proposal / Hatzaat Psara", heading_style))
        mediation = analysis['mediation_proposal']
        mediation_text = f"""
        <b>Proposal / Hahatzaa:</b> {mediation['proposal']}<br/><br/>
        <b>Rationale / Nimuk:</b> {mediation['rationale']}
        """
        elements.append(Paragraph(mediation_text, normal_style))
        elements.append(Spacer(1, 0.8*cm))

    # Final Decision
    elements.append(Paragraph("Final Decision / Hahahlata Hasofit", heading_style))
    decision = analysis['final_verdict']
    reasoning = analysis['reasoning']

    verdict_text = f"""
    <b>Ruling / Psiqa:</b> {decision['verdict']}<br/><br/>
    """
    elements.append(Paragraph(verdict_text, normal_style))

    # Reasoning
    elements.append(Paragraph("Reasoning / Nimuqim", heading_style))
    reasoning_summary = f"<b>Summary / Sikum:</b> {reasoning['summary']}<br/><br/>"
    elements.append(Paragraph(reasoning_summary, normal_style))

    if 'detailed_analysis' in reasoning:
        for i, point in enumerate(reasoning['detailed_analysis'], 1):
            elements.append(Paragraph(f"{i}. {point}", normal_style))
            elements.append(Spacer(1, 0.3*cm))

    if 'legal_basis' in reasoning:
        legal_basis_text = f"<br/><b>Legal Basis / Basis Mishpati:</b> {reasoning['legal_basis']}"
        elements.append(Paragraph(legal_basis_text, normal_style))

    elements.append(Spacer(1, 0.8*cm))

    # Financial Summary
    elements.append(Paragraph("Financial Summary / Sikum Kaspi", heading_style))

    legal_exp = analysis.get('legal_expenses', {})
    legal_exp_amount = legal_exp.get('registered_mail', decision.get('legal_expenses', 35.0))

    financial_data = [
        ['Amount / Sekum', 'Item / Prit'],
        [f"{decision['amount_awarded']:,.2f} ILS", 'Compensation Amount / Sekum Hapitzui'],
        [f"{legal_exp_amount:.2f} ILS", 'Registered Mail Fee / Dmei Mishloah Doar Rashum'],
        [f"{decision['total_payment']:,.2f} ILS", 'Total Payment / Sakh Hakol Letashlum']
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
    <b>Payment Deadline / Moad Tashlum:</b> The defendant must pay the full amount within {decision['payment_deadline_days']} days
    from the date of receiving this arbitral award.
    <br/><br/>
    Al hanitba leshalem et meloa hasekum tokh {decision['payment_deadline_days']} yamim
    miyom qabalt pesaq borerot ze.
    """
    elements.append(Paragraph(payment_text, normal_style))
    elements.append(Spacer(1, 1.2*cm))

    # Signature section
    elements.append(Paragraph("Signatures / Hatimot", heading_style))
    elements.append(Spacer(1, 0.5*cm))

    signature_data = [
        ['____________________', '____________________'],
        ['Resolve AI System Signature', f'Date / Tarikh: {datetime.now().strftime("%d/%m/%Y")}'],
        ['', ''],
        ['____________________', '____________________'],
        ['Defendant Acknowledgment', 'Claimant Acknowledgment'],
        ['Ishur Qabala - Nitba', 'Ishur Qabala - Tovea']
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
    Convert analysis to formatted HTML for UI display

    Args:
        analysis: The analysis dictionary

    Returns:
        str: HTML formatted analysis summary
    """

    html = """
    <div style='background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
                padding: 40px; border-radius: 20px; margin: 30px 0;
                box-shadow: 0 10px 40px rgba(0,0,0,0.1);'>
        <h2 style='color: #1a4d5e; text-align: center; font-size: 2rem; margin-bottom: 30px;'>
            📊 Analysis Results / Totzuot Nituah
        </h2>

        <div style='background: white; padding: 25px; border-radius: 15px; margin-bottom: 20px;
                    border-right: 4px solid #00d4ff;'>
            <h3 style='color: #00d4ff; font-size: 1.4rem; margin-bottom: 15px;'>
                📋 Dispute Points / Neqodot Mahloqut
            </h3>
    """

    for i, dispute in enumerate(analysis['dispute_table'], 1):
        html += f"""
            <div style='background: #f8fafc; padding: 20px; border-radius: 12px; margin-bottom: 15px;'>
                <h4 style='color: #1a4d5e; font-size: 1.2rem; margin-bottom: 10px;'>
                    {i}. {dispute['issue']}
                </h4>
                <p style='margin: 8px 0; line-height: 1.6;'>
                    <b style='color: #667eea;'>Claimant:</b> {dispute['claimant_version']}
                </p>
                <p style='margin: 8px 0; line-height: 1.6;'>
                    <b style='color: #f59e0b;'>Defendant:</b> {dispute['defendant_version']}
                </p>
                <p style='margin: 8px 0; padding: 12px; background: #e8f5e9; border-radius: 8px; line-height: 1.6;'>
                    <b style='color: #10b981;'>AI Analysis:</b> {dispute['ai_analysis']}
                </p>
            </div>
        """

    html += """
        </div>
    """

    # Mediation Proposal
    if 'mediation_proposal' in analysis:
        mediation = analysis['mediation_proposal']
        html += f"""
        <div style='background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
                    padding: 30px; border-radius: 15px; color: white; margin-bottom: 20px;'>
            <h3 style='font-size: 1.6rem; margin-bottom: 15px; text-align: center;'>
                🤝 Mediation Proposal / Hatzaat Psara
            </h3>
            <div style='background: rgba(255,255,255,0.15); padding: 20px; border-radius: 12px;'>
                <p style='margin-bottom: 15px; line-height: 1.8;'>
                    <b>Proposal:</b><br/>{mediation['proposal']}
                </p>
                <p style='line-height: 1.8;'>
                    <b>Rationale:</b><br/>{mediation['rationale']}
                </p>
            </div>
        </div>
        """

    # Final Verdict
    decision = analysis['final_verdict']
    html += f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                    padding: 30px; border-radius: 15px; color: white; margin-bottom: 20px;'>
            <h3 style='font-size: 1.6rem; margin-bottom: 15px; text-align: center;'>
                ⚖️ Final Decision / Hahahlata Hasofit
            </h3>
            <p style='font-size: 1.3rem; text-align: center; margin-bottom: 20px;'>
                <b>{decision['verdict']}</b>
            </p>
            <div style='background: rgba(255,255,255,0.15); padding: 20px; border-radius: 12px;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
                    <span>Compensation / Pitzui:</span>
                    <span style='font-size: 1.2rem; font-weight: bold;'>{decision['amount_awarded']:,.0f} ILS</span>
                </div>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
                    <span>Legal Expenses (Mail) / Hotzuot Mishpat:</span>
                    <span style='font-size: 1.2rem; font-weight: bold;'>{decision['legal_expenses']:.0f} ILS</span>
                </div>
                <hr style='border: none; border-top: 2px solid rgba(255,255,255,0.3); margin: 15px 0;'>
                <div style='display: flex; justify-content: space-between;'>
                    <span style='font-size: 1.2rem;'><b>Total Payment / Sakh Hakol:</b></span>
                    <span style='font-size: 1.5rem; font-weight: bold;'>{decision['total_payment']:,.0f} ILS</span>
                </div>
                <p style='text-align: center; margin-top: 15px; font-size: 0.95rem;'>
                    Payment within {decision['payment_deadline_days']} days / Tashlum tokh {decision['payment_deadline_days']} yamim
                </p>
            </div>
        </div>
    """

    html += """
    </div>
    """

    return html
