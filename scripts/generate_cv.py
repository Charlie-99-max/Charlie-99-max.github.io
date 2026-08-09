#!/usr/bin/env python3
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Hao_Luo_CV_EN.pdf"
WEB_COPY = ROOT / "assets" / "cv" / "Hao_Luo_CV_EN.pdf"
PORTRAIT = ROOT / "assets" / "images" / "hao-luo.png"
SEAL = ROOT / "assets" / "images" / "tsinghua-seal.png"

PURPLE = colors.HexColor("#82318E")
BLUE = colors.HexColor("#073F78")
LINK = colors.HexColor("#0B5E9A")
INK = colors.HexColor("#191919")
MUTED = colors.HexColor("#5F6670")
LINE = colors.HexColor("#D9DEE5")
SOFT = colors.HexColor("#F7F8FA")

PAGE_W, PAGE_H = A4
LEFT = 16 * mm
RIGHT = 16 * mm
TOP = 13 * mm
BOTTOM = 14 * mm

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=23, leading=25, textColor=PURPLE, spaceAfter=2))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=10.2, leading=13, textColor=BLUE, spaceAfter=4))
styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=8.3, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="Profile", fontName="Helvetica", fontSize=8.6, leading=12.3, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=12, leading=14, textColor=BLUE, spaceBefore=6, spaceAfter=5, borderColor=LINE, borderWidth=0, borderPadding=0))
styles.add(ParagraphStyle(name="Subsection", fontName="Helvetica-Bold", fontSize=9.6, leading=12, textColor=PURPLE, spaceBefore=5, spaceAfter=3))
styles.add(ParagraphStyle(name="EntryTitle", fontName="Helvetica-Bold", fontSize=9.1, leading=11.5, textColor=INK))
styles.add(ParagraphStyle(name="EntryMeta", fontName="Helvetica", fontSize=8, leading=10.5, textColor=MUTED))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=8.1, leading=11.1, textColor=INK, leftIndent=0, bulletIndent=0, spaceAfter=2))
styles.add(ParagraphStyle(name="Small", fontName="Helvetica", fontSize=7.2, leading=9.5, textColor=MUTED))
styles.add(ParagraphStyle(name="Publication", fontName="Helvetica", fontSize=7.7, leading=10.6, textColor=INK, leftIndent=12, firstLineIndent=-12, spaceAfter=5))
styles.add(ParagraphStyle(name="Patent", fontName="Helvetica", fontSize=7.7, leading=10.6, textColor=INK, leftIndent=16, firstLineIndent=-16, spaceAfter=5))
styles.add(ParagraphStyle(name="Tag", fontName="Helvetica-Bold", fontSize=6.6, leading=8, textColor=colors.white, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="Footer", fontName="Helvetica", fontSize=7.3, leading=9, textColor=MUTED))
styles.add(ParagraphStyle(name="FooterRight", fontName="Helvetica", fontSize=7.3, leading=9, textColor=MUTED, alignment=TA_RIGHT))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


def section(title):
    return [Spacer(1, 1.5 * mm), P(title, "Section"), HRFlowable(width="100%", thickness=.55, color=LINE, spaceAfter=3.5 * mm)]


def dated_entry(title, meta, date, bullets=None):
    table = Table(
        [[P(title, "EntryTitle"), Paragraph(date, ParagraphStyle("date", parent=styles["EntryMeta"], alignment=TA_RIGHT, textColor=PURPLE))],
         [P(meta, "EntryMeta"), ""]],
        colWidths=[139 * mm, 23 * mm],
    )
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("SPAN", (0, 1), (1, 1)),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * mm),
    ]))
    parts = [table]
    for bullet in bullets or []:
        parts.append(P(f"<font color='#073F78'>•</font>&nbsp;&nbsp;{bullet}", "Body"))
    parts.append(Spacer(1, 1.5 * mm))
    return KeepTogether(parts)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(.45)
    canvas.line(LEFT, 10.2 * mm, PAGE_W - RIGHT, 10.2 * mm)
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(LEFT, 6.5 * mm, "Hao Luo · Academic Curriculum Vitae")
    canvas.drawRightString(PAGE_W - RIGHT, 6.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    WEB_COPY.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT), pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=TOP, bottomMargin=BOTTOM, title="Academic CV - Hao Luo",
        author="Hao Luo", subject="Living DNA Data Storage and Bioengineering",
    )
    frame = Frame(LEFT, BOTTOM, PAGE_W - LEFT - RIGHT, PAGE_H - TOP - BOTTOM, id="main")
    doc.addPageTemplates([PageTemplate(id="cv", frames=frame, onPage=header_footer)])
    story = []

    seal = Image(str(SEAL), width=18 * mm, height=18 * mm)
    portrait = Image(str(PORTRAIT), width=22.5 * mm, height=30.9 * mm)
    identity = [
        P("HAO LUO", "Name"),
        P("Ph.D. Candidate in Mechanical Engineering · Tsinghua University", "Role"),
        P("Living DNA Data Storage · Engineered Living Materials · Microfluidics · Biofabrication · Automation", "Contact"),
        Spacer(1, 2.2 * mm),
        P("Beijing, China &nbsp;·&nbsp; <link href='mailto:longalonga888@163.com' color='#0B5E9A'>longalonga888@163.com</link> &nbsp;·&nbsp; <link href='https://orcid.org/0000-0003-2239-3928' color='#0B5E9A'>ORCID</link> &nbsp;·&nbsp; <link href='https://github.com/Charlie-99-max' color='#0B5E9A'>GitHub</link>", "Contact"),
    ]
    identity_table = Table([[seal, identity, portrait]], colWidths=[23 * mm, 126 * mm, 27 * mm])
    identity_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("RIGHTPADDING", (-1, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5 * mm),
    ]))
    story += [identity_table, HRFlowable(width="100%", thickness=1.15, color=PURPLE, spaceBefore=1.5 * mm, spaceAfter=3.5 * mm)]
    story += [P("PROFILE", "Subsection"), P(
        "Ph.D. candidate developing physically addressable and regenerative living systems for DNA data storage. Research spans digital-to-DNA encoding, plasmid and bacterial engineering, droplet microfluidics, living microspheroid fabrication, fluorescence-assisted random access, dry-state preservation, information regeneration and rewriting, and automated system integration. First author of two <i>Advanced Materials</i> papers introducing the ELMM archival file system and regenerative Living Disk-Drive architecture.",
        "Profile")]
    story += section("EDUCATION")
    story.append(dated_entry("Tsinghua University", "Ph.D. in Mechanical Engineering · Advisor: Prof. Zhuo Xiong · GPA: 3.8 / 4.0", "2021—2026", ["Expected graduation: December 2026 · Beijing Key Laboratory of Intelligent Organ Biofabrication and Regenerative Repair."]))
    story.append(dated_entry("Tsinghua University", "B.Eng. in Mechanical Engineering · GPA: 3.77 / 4.0 · Rank: 3 / 106", "2017—2021"))
    story += section("SELECTED RESEARCH CONTRIBUTIONS")
    story.append(dated_entry("Regenerative Living Disk-Drive for DNA Data Storage", "System architecture, process development, and instrument integration", "2024—2025", [
        "Connected a lyophilized Living Disk, fluorescence-based Optical Retriever, and desktop Living Drive for release, bacterial expansion, re-encapsulation, and database replenishment.",
        "Validated 10 automated regeneration cycles, 13 lyophilization-rehydration cycles, and four months of ambient dry storage; established a CRISPR-Cas12a/λ-Red rewriting interface.",
    ]))
    story.append(dated_entry("Engineered Living Memory Microspheroid (ELMM) Archival File System", "Full-stack process and algorithm development", "2023—2024", [
        "Developed DNA encoding/decoding, functional plasmid indexing, droplet-microfluidic fabrication of ~50 µm living file units, Boolean retrieval, and freeze-drying workflows.",
        "Demonstrated >98% fluorescence-assisted sorting accuracy and recoverable information after seven lyophilization-rehydration cycles.",
    ]))
    story.append(dated_entry("Patient-derived Cancer Assembloids", "Microfluidic platform and fabrication process development", "2021—2022", [
        "Developed droplet-microfluidic processes for patient-derived lung and gastric cancer assembloids used in tumor-microenvironment modeling and drug screening.",
    ]))
    story.append(dated_entry("Chip-based High-throughput DNA Synthesizer", "Automation prototype development", "2022—2023", ["Developed a chip-assisted synthesis prototype and collaborative encoding method; validated 13-nt DNA synthesis."]))

    story.append(PageBreak())
    story += section("PEER-REVIEWED PUBLICATIONS")
    pubs = [
        ("1", "<b>Hao Luo</b>, JinKai Gao, XiangXiang Huang, YongCong Fang, TianYu Huang, YingKai Xia, ZeYang Yu, ChengHao Cao, and Zhuo Xiong. <b>Thermo-Responsive Living Microspheroids Enable a Regenerative Living Disk-Drive System for DNA Data Storage.</b> <i>Advanced Materials</i> 38(42), e73806 (2026). <link href='https://doi.org/10.1002/adma.73806' color='#0B5E9A'>doi:10.1002/adma.73806</link>. <font color='#82318E'><b>FIRST AUTHOR</b></font>"),
        ("2", "<b>Hao Luo</b>, Wen Huang, ZhongHui He, Yongcong Fang, Yueming Tian, and Zhuo Xiong. <b>Engineered Living Memory Microspheroid-Based Archival File System for Random Accessible In Vivo DNA Storage.</b> <i>Advanced Materials</i> 37(13), 2415358 (2025). <link href='https://doi.org/10.1002/adma.202415358' color='#0B5E9A'>doi:10.1002/adma.202415358</link>. <font color='#82318E'><b>FIRST AUTHOR</b></font>"),
        ("3", "Yanmei Zhang, Qifan Hu, Yuquan Pei, <b>Hao Luo</b>, et al. <b>A Patient-Specific Lung Cancer Assembloid Model with Heterogeneous Tumor Microenvironments.</b> <i>Nature Communications</i> 15, 3382 (2024). <link href='https://doi.org/10.1038/s41467-024-47737-z' color='#0B5E9A'>doi:10.1038/s41467-024-47737-z</link>."),
        ("4", "Xinxin Xu, Yunhe Gao, Jianli Dai, Qianqian Wang, Zixuan Wang, Wenquan Liang, Qing Zhang, Wenbo Ma, Zibo Liu, <b>Hao Luo</b>, et al. <b>Gastric Cancer Assembloids Derived from Patient-Derived Xenografts: A Preclinical Model for Therapeutic Drug Screening.</b> <i>Small Methods</i> 8(9), 2400204 (2024). <link href='https://doi.org/10.1002/smtd.202400204' color='#0B5E9A'>doi:10.1002/smtd.202400204</link>."),
        ("5", "Min Ye, Yiran Shan, Bingchuan Lu, <b>Hao Luo</b>, et al. <b>Creating a Semi-Opened Micro-Cavity Ovary Through Sacrificial Microspheres as an In Vitro Model for Discovering the Potential Effect of Ovarian Toxic Agents.</b> <i>Bioactive Materials</i> 26, 216-230 (2023). <link href='https://doi.org/10.1016/j.bioactmat.2023.02.029' color='#0B5E9A'>doi:10.1016/j.bioactmat.2023.02.029</link>."),
        ("6", "Yanmei Zhang, Zixuan Wang, Qifan Hu, <b>Hao Luo</b>, et al. <b>3D Bioprinted GelMA-Nanoclay Hydrogels Induce Colorectal Cancer Stem Cells Through Activating Wnt/β-Catenin Signaling.</b> <i>Small</i> 18(18), 2200364 (2022). <link href='https://doi.org/10.1002/smll.202200364' color='#0B5E9A'>doi:10.1002/smll.202200364</link>."),
    ]
    for n, text in pubs:
        story.append(P(f"<font color='#82318E'><b>[{n}]</b></font> {text}", "Publication"))

    story += section("CHINESE INVENTION PATENTS")
    patents = [
        "Zhuo Xiong, Yanmei Zhang, Ting Zhang, <b>Hao Luo</b> (student first inventor). <b>Method and Device for Constructing Personalized Tumor Assembloids Based on Droplet Microfluidics.</b> CN113583960B / ZL202110613983.6. Granted, 2023.",
        "Zhuo Xiong, <b>Hao Luo</b> (student first inventor), Liliang Ouyang, Yu Yang. <b>DNA-based Information Storage and Reading Method and Device.</b> CN117789788A. Published, 2024.",
        "Zhuo Xiong, Ben Pei, Liliang Ouyang, <b>Hao Luo</b>. <b>Hierarchical DNA Data Storage and Reading Method.</b> CN115421669B / ZL202211217725.7. Granted, 2025.",
        "Min Ye, Ting Zhang, Zhuo Xiong, Bingchuan Lu, <b>Hao Luo</b>. <b>Ovulating Artificial Ovary Scaffold and Its Preparation and Application.</b> CN114748690B / ZL202210248677.1. Granted, 2022.",
        "Zhuo Xiong, <b>Hao Luo</b> (student first inventor). <b>Rewritable Engineered Living DNA Information Storage Unit and Construction Method.</b> Chinese invention patent application, 2026.",
        "Zhuo Xiong, <b>Hao Luo</b> (student first inventor), XiangXiang Huang. <b>Hierarchical Living DNA Data Storage System and Operating Method.</b> Chinese invention patent application, 2026.",
    ]
    for i, text in enumerate(patents, 1):
        story.append(P(f"<font color='#82318E'><b>[P{i}]</b></font> {text}", "Patent"))

    story += section("SELECTED ENGINEERING PROJECTS")
    story.append(dated_entry("Machine Vision Dot Recognition", "Project lead · Python/OpenCV algorithm, DLL packaging, and integration", "2025", ["Developed image preprocessing, feature extraction, and dot-pattern recognition; deployed the packaged module within an information system."]))
    story.append(dated_entry("Laser Galvanometer Dynamic Focusing and Embedded Servo Control", "Core developer · National Undergraduate Innovation Project", "2019—2021", ["Integrated mechanical design, MATLAB simulation, STM32 control, sensors, actuators, part manufacturing, and prototype testing; project rated Excellent."]))

    story.append(PageBreak())
    story += section("SELECTED TALKS & CONFERENCES")
    story.append(dated_entry("BDMC 2026 · The Chinese University of Hong Kong", "Thermo-Responsive Living Microspheroids Enable a Regenerative Living Disk-Drive System for DNA Data Storage · Oral presentation", "Jul 2026"))
    story.append(dated_entry("ICCES 2025 · Changsha, China", "Engineered Living Memory Microspheroid-Based Archival File System for Random Accessible In Vivo DNA Storage · Oral presentation", "May 2025"))
    story.append(dated_entry("ACBD-ISBM 2023 · Beijing, China", "Research on the Fabrication of Cancer Assembloids Based on Droplet Microfluidics · Oral presentation", "Mar 2023"))

    story += section("TEACHING")
    story.append(dated_entry("Biomaterials Engineering and Devices", "Teaching Assistant · Tsinghua University", "2021—2026", ["Outstanding Teaching Assistant, 2022 · Evaluation in the top 5% university-wide; contributed to AI-enabled course reform and the Biomanufacturing Brain teaching platform."]))
    story.append(dated_entry("Physics Laboratory B", "Teaching Assistant · Tsinghua University", "2025—2026"))
    story.append(dated_entry("Fundamentals of Physics", "Teaching Assistant · Tsinghua University", "2025—2026"))

    story += section("SELECTED HONORS & AWARDS")
    awards = [
        [P("Outstanding Teaching Assistant", "EntryTitle"), P("Tsinghua University · Top 5%", "EntryMeta"), P("2022", "EntryMeta")],
        [P("Comprehensive Excellence Scholarship", "EntryTitle"), P("Tsinghua University", "EntryMeta"), P("2022", "EntryMeta")],
        [P("Excellent Completion · National Undergraduate Innovation Project", "EntryTitle"), P("Laser galvanometer control system", "EntryMeta"), P("2021", "EntryMeta")],
        [P("Energy Science Scholarship", "EntryTitle"), P("Tsinghua University", "EntryMeta"), P("2020", "EntryMeta")],
        [P("National Encouragement Scholarship", "EntryTitle"), P("Two-time recipient", "EntryMeta"), P("2018, 2019", "EntryMeta")],
    ]
    award_table = Table(awards, colWidths=[78 * mm, 65 * mm, 19 * mm])
    award_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1.3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.3 * mm),
        ("LINEBELOW", (0, 0), (-1, -2), .35, LINE),
    ]))
    story.append(award_table)

    story += section("TECHNICAL EXPERTISE")
    skill_data = [
        [P("BIOENGINEERING", "Subsection"), P("ENGINEERING", "Subsection"), P("COMPUTING", "Subsection")],
        [P("Plasmid engineering · Bacterial culture · Droplet microfluidics · Hydrogel microspheres · Freeze-drying · Organoids / assembloids", "Body"), P("SolidWorks · AutoCAD · ANSYS · STM32 · Arduino · CNC · 3D printing · Mechanical design · System integration", "Body"), P("Python · OpenCV · MATLAB · C/C++ · DNA encoding · Image processing · DLL packaging · Scientific automation", "Body")],
    ]
    skill_table = Table(skill_data, colWidths=[54 * mm, 54 * mm, 54 * mm])
    skill_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), SOFT),
        ("BOX", (0, 0), (-1, -1), .5, LINE),
        ("INNERGRID", (0, 0), (-1, -1), .4, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    story.append(skill_table)

    story += section("ADDITIONAL EXPERIENCE")
    story.append(dated_entry("Guangdong Shunde Graduate School of Innovation", "R&D Assistant · GelMA-PVA artificial vessel rapid-forming process", "2023"))
    story.append(dated_entry("Silver Basis Technology", "Structural Design Intern · Axial cam-compression rotary engine concept and analysis", "2020"))
    story.append(Spacer(1, 2 * mm))
    story.append(P("Website: <link href='https://charlie-99-max.github.io' color='#0B5E9A'>charlie-99-max.github.io</link> &nbsp;·&nbsp; Updated August 2026", "Small"))

    doc.build(story)
    WEB_COPY.write_bytes(OUTPUT.read_bytes())
    print(OUTPUT)
    print(WEB_COPY)


if __name__ == "__main__":
    build()
