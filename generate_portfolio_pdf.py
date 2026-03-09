from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

import os
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sage_Clokey_GitHub_Portfolio.pdf")

repos = [
    {
        "name": "NetworkOS",
        "language": "JavaScript / Python (FastAPI)",
        "url": "https://github.com/Sage-Clokey/NetworkOS",
        "description": (
            "A personal networking intelligence system designed to help manage contacts from conferences and "
            "professional events. It features quick contact capture, a searchable dashboard, event organization, "
            "follow-up reminders, OCR business card scanning, and network visualization. The platform pairs a "
            "FastAPI backend with a modern frontend to streamline professional relationship management."
        ),
        "run": "Clone the repo, install dependencies in both the backend/ and frontend/ directories, then run the FastAPI server and frontend separately.",
    },
    {
        "name": "Living-works-by-the-word",
        "language": "HTML / Python",
        "url": "https://github.com/Sage-Clokey/Living-works-by-the-word",
        "site": "https://sage-clokey.github.io/Living-works-by-the-word/",
        "description": (
            "An initiative that merges morphogenetic simulation with philosophy and business strategy, positioning "
            "\"organisms, not machines\" as the design paradigm of the future. It targets synthetic biology, AI drug "
            "design, and bioinformatics through a Morphological BioCAD platform that simulates organism-scale growth "
            "and adaptation. The project combines interactive web architecture, generative simulations, and an ethical "
            "framework arguing that living systems are superior to machine-age design paradigms."
        ),
        "run": "Open index.html in a browser to explore the web interface; run the Python scripts directly for simulation output.",
    },
    {
        "name": "claude-Code",
        "language": "Python / React (JSX)",
        "url": "https://github.com/Sage-Clokey/claude-Code",
        "description": (
            "A collection of projects and scripts developed with Claude AI assistance, featuring three main components: "
            "a React UI component (LivingWorks.jsx), a Python morphogenesis simulation, and a Python generator toolkit. "
            "The work focuses on exploring generative biological systems and adaptive growth-oriented computational models."
        ),
        "run": (
            "For Python scripts: python3 livingworks.py or python3 livingworks_morphogenesis.py. "
            "For the React component: integrate LivingWorks.jsx into an existing React app."
        ),
    },
    {
        "name": "growthshapes",
        "language": "Python",
        "url": "https://github.com/Sage-Clokey/growthshapes",
        "description": (
            "Simulates biological growth patterns and morphogenetic shapes through computational methods. "
            "The coral_sim/ subdirectory contains a coral reef growth simulation that models how complex natural "
            "forms emerge through algorithmic exploration of biological systems."
        ),
        "run": "Navigate to the coral_sim/ directory and run the main Python simulation script.",
    },
    {
        "name": "sbir-Spiral-steward",
        "language": "Python",
        "url": "https://github.com/Sage-Clokey/sbir-Spiral-steward",
        "description": (
            "A grant application toolkit for the Spiral Steward / LivingWorks SBIR initiative, combining bioinformatics "
            "with living architecture research. The repository includes Python scripts to auto-generate complete SBIR "
            "applications, specific aims pages, pitch decks, and supporting documents. It also contains philosophical "
            "writings and a gRNA design subdirectory relevant to the biological research component."
        ),
        "run": "Run any of the generator scripts directly: python3 generate_sbir.py, python3 generate_pitch_deck.py, etc.",
    },
    {
        "name": "spiral-steward-website",
        "language": "HTML",
        "url": "https://github.com/Sage-Clokey/spiral-steward-website",
        "site": "https://sage-clokey.github.io/spiral-steward-website/",
        "description": (
            "The public-facing website for the Spiral Steward project, exploring bioinformatics as stewardship of living "
            "order. The site publishes philosophical essays and interdisciplinary works covering topics such as bioinformatics, "
            "legal theory, liberty, and living systems design, connecting biological pattern recognition with philosophy, law, "
            "and architecture."
        ),
        "run": "Open index.html in a browser, or deploy the static HTML files to any web host.",
    },
    {
        "name": "GoogleSheetRowViewer",
        "language": "Python",
        "url": "https://github.com/Sage-Clokey/GoogleSheetRowViewer",
        "description": (
            "A Python desktop application that provides a graphical interface for viewing and interacting with rows from "
            "Google Sheets. It connects to the Google Sheets API using credentials and displays spreadsheet data through "
            "a user-friendly tkinter GUI."
        ),
        "run": (
            "Install dependencies (google-auth, google-api-python-client, tkinter). "
            "Place your credentials.json in the project root, then run: python3 sheet_gui.py"
        ),
    },
    {
        "name": "MemberCallApp_StarCommand_Rebuild",
        "language": "Kotlin (Android)",
        "url": "https://github.com/Sage-Clokey/MemberCallApp_StarCommand_Rebuild",
        "description": (
            "A rebuilt version of the MemberCall Android app implementing the Star Command architecture pattern for a "
            "more structured and maintainable codebase. This refactor reorganizes the original member calling application "
            "around a clean architectural foundation."
        ),
        "run": "Open in Android Studio, sync Gradle, then build and run on an emulator or physical Android device.",
    },
    {
        "name": "MemberCallAppProject_Complete",
        "language": "Kotlin (Android)",
        "url": "https://github.com/Sage-Clokey/MemberCallAppProject_Complete",
        "description": (
            "The complete, production-ready version of the MemberCall Android application featuring full member call "
            "management with integrated UI and backend. This is the finished, deployable build of the application."
        ),
        "run": "Open in Android Studio, sync Gradle, build, and deploy to an Android device or emulator.",
    },
    {
        "name": "MemberCallAppProject-1",
        "language": "Kotlin (Android)",
        "url": "https://github.com/Sage-Clokey/MemberCallAppProject-1",
        "description": (
            "Version 2 of the MemberCall Android application, representing an updated iteration of the member calling "
            "mobile tool. It includes the app source code along with alternate build configuration options."
        ),
        "run": "Open in Android Studio, sync Gradle, and run on an Android device or emulator.",
    },
    {
        "name": "BME-105_exam-2",
        "language": "Python / HTML",
        "url": "https://github.com/Sage-Clokey/BME-105_exam-2",
        "site": "https://sage-clokey.github.io/BME-105_exam-2/",
        "description": (
            "An exam preparation toolkit for BME 105, containing auto-generated cheat sheets, a study guide, and a "
            "Python script (make_cheatsheet.py) that programmatically compiles course material into printable PDF "
            "documents. Also includes a small study web app in the study-app/ directory."
        ),
        "run": "Run python3 make_cheatsheet.py to regenerate the cheat sheet PDFs, or open index.html for the study app.",
    },
    {
        "name": "eeg-nuerodegenerative-test",
        "language": "Python",
        "url": "https://github.com/Sage-Clokey/eeg-nuerodegenerative-test",
        "description": (
            "An exploratory research project focused on EEG signal analysis for neurodegenerative disease detection. "
            "The project examines brain electrical patterns to uncover diagnostic indicators linked to conditions such "
            "as Alzheimer's and Parkinson's, seeking measurable patterns that could support clinical assessment of "
            "neurological decline."
        ),
        "run": "Install required Python packages (numpy, scipy, mne or similar), then run the analysis scripts in order.",
    },
    {
        "name": "L2-Sanger-Sequencing",
        "language": "Bioinformatics (data files)",
        "url": "https://github.com/Sage-Clokey/L2-Sanger-Sequencing-20250403T211637Z-001",
        "description": (
            "A lab module from BME 110 at UC Santa Cruz documenting Sanger sequencing output files and sequence "
            "alignment and analysis results. The project demonstrates practical application of bioinformatics techniques "
            "for processing and interpreting genetic sequence data."
        ),
        "run": "View sequencing output files with any bioinformatics tool (e.g., SnapGene, NCBI BLAST, or Benchling) to visualize and align sequences.",
    },
    {
        "name": "notesjson",
        "language": "JSON / PDF",
        "url": "https://github.com/Sage-Clokey/notesjson",
        "description": (
            "A personal knowledge archive that exports a year's worth of personal notes in multiple formats for easy "
            "access and organization. The repository provides both a structured JSON file and corresponding PDFs "
            "organized chronologically and by topic, enabling searchable and printable access to the content."
        ),
        "run": "Open the JSON file with any text editor or JSON viewer; open the PDFs directly in a PDF reader.",
    },
    {
        "name": "MemberCallAppProject",
        "language": "Kotlin (Android)",
        "url": "https://github.com/Sage-Clokey/MemberCallAppProject",
        "description": (
            "The original MemberCall Android application project — the first iteration of the member call management "
            "app. This repository serves as the starting foundation from which subsequent versions were developed."
        ),
        "run": "Open in Android Studio, sync Gradle, and build to an Android device or emulator.",
    },
    {
        "name": "things-to-add-to-git-hub",
        "language": "N/A",
        "url": "https://github.com/Sage-Clokey/things-to-add-to-git-hub",
        "description": (
            "A personal staging repository used to organize and track projects and files intended for future GitHub "
            "uploads. It serves as a checklist and holding area for work-in-progress items before they are published "
            "in their own dedicated repositories."
        ),
        "run": "No runnable code — this is an organizational/planning repository.",
    },
    {
        "name": "x-tweats-ideas",
        "language": "N/A",
        "url": "https://github.com/Sage-Clokey/x-tweats-ideas",
        "description": (
            "A personal brainstorming repository for drafting and storing tweet ideas and social media content. "
            "It serves as a quick-capture space for thoughts, thread concepts, and messaging ideas intended for "
            "posting on X (formerly Twitter)."
        ),
        "run": "No runnable code — this is a content planning and ideation repository.",
    },
    {
        "name": "discussion_8",
        "language": "HTML / Python / CSV",
        "url": "https://github.com/Sage-Clokey/discussion_8",
        "site": "https://sage-clokey.github.io/discussion_8/PopGen_Simulator.html",
        "description": (
            "A browser-based population genetics simulation toolkit built for UC Santa Cruz's BME 105 course. "
            "It implements the Wright-Fisher model to explore how allele frequencies change over generations, "
            "covering genetic drift, Hardy-Weinberg equilibrium, and the effect of population size on evolution. "
            "The repo includes pre-configured simulation datasets (N=500 to infinite) at varying allele frequencies, "
            "an interactive simulator (PopGen_Simulator.html), and a static analysis report (Population_Genetics_Analysis.html)."
        ),
        "run": "Open PopGen_Simulator.html in a browser, upload one of the included CSV files, and explore the interactive charts.",
    },
]


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.85 * inch,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        fontSize=22,
        leading=28,
        textColor=colors.HexColor("#1a1a2e"),
        spaceAfter=4,
        alignment=TA_CENTER,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#555555"),
        spaceAfter=2,
        alignment=TA_CENTER,
    )
    repo_name_style = ParagraphStyle(
        "RepoName",
        parent=styles["Heading2"],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1a1a2e"),
        spaceAfter=2,
        spaceBefore=14,
    )
    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["Normal"],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#666666"),
        spaceAfter=5,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#333333"),
        spaceAfter=5,
    )
    run_label_style = ParagraphStyle(
        "RunLabel",
        parent=styles["Normal"],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#0a7cba"),
        spaceAfter=2,
    )
    run_style = ParagraphStyle(
        "Run",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#444444"),
        leftIndent=10,
        spaceAfter=4,
    )

    story = []

    # Title block
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("Sage Clokey — GitHub Portfolio", title_style))
    story.append(Paragraph("github.com/Sage-Clokey", subtitle_style))
    story.append(Spacer(1, 0.08 * inch))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1a1a2e")))
    story.append(Spacer(1, 0.15 * inch))

    for repo in repos:
        story.append(Paragraph(repo["name"], repo_name_style))
        meta_parts = (
            f'<b>Language:</b> {repo["language"]} &nbsp;&nbsp; '
            f'<b>Repo:</b> <a href="{repo["url"]}" color="#0a7cba">{repo["url"]}</a>'
        )
        if repo.get("site"):
            meta_parts += (
                f' &nbsp;&nbsp; <b>Live Site:</b> <a href="{repo["site"]}" color="#0a7cba">{repo["site"]}</a>'
            )
        story.append(Paragraph(meta_parts, meta_style))
        story.append(Paragraph(repo["description"], body_style))
        story.append(Paragraph("<b>How to run / access:</b>", run_label_style))
        story.append(Paragraph(repo["run"], run_style))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc")))

    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "Generated March 2026 · sage-clokey@github · sajcsushi@gmail.com",
            ParagraphStyle(
                "Footer",
                parent=styles["Normal"],
                fontSize=8,
                textColor=colors.HexColor("#999999"),
                alignment=TA_CENTER,
            ),
        )
    )

    doc.build(story)
    print(f"PDF created: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_pdf()
