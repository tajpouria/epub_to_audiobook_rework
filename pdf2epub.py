import PyPDF2
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os
import re


def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            page_text = page_text.replace("\t", " ")
            text += f"\n\n==== PAGE {i+1} ====\n\n"
            text += page_text
    return text


def create_xml_chapter(title, content):
    root = ET.Element(
        "html",
        xmlns="http://www.w3.org/1999/xhtml",
        xmlns_epub="http://www.idpf.org/2007/ops",
    )
    head = ET.SubElement(root, "head")
    title_elem = ET.SubElement(head, "title")
    title_elem.text = title

    body = ET.SubElement(root, "body")
    content_elem = ET.SubElement(body, "div")
    content_elem.text = content

    xml_str = ET.tostring(root, encoding="unicode")
    xml_pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")

    xml_pretty = "\n".join([line for line in xml_pretty.split("\n") if line.strip()])

    return f'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n{xml_pretty}'


def process_book(pdf_path, chapters_dict, output_dir):
    full_text = read_pdf(pdf_path)

    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/full_text.txt", "w", encoding="utf-8") as debug_file:
        debug_file.write(full_text)

    print(f"Full text written to {output_dir}/full_text.txt for debugging.")

    for index, (chapter_title, (start_page, end_page)) in enumerate(
        chapters_dict.items(), start=1
    ):
        start_marker = f"==== PAGE {start_page} ===="
        end_marker = f"==== PAGE {end_page + 1} ===="

        start_index = full_text.find(start_marker)
        if start_index == -1:
            print(
                f"Warning: Could not find start of chapter '{chapter_title}' (Page {start_page})"
            )
            continue

        end_index = full_text.find(end_marker)
        if end_index == -1:
            end_index = len(full_text)

        chapter_content = full_text[start_index:end_index].strip()

        chapter_content = re.sub(r"==== PAGE \d+ ====", "", chapter_content).strip()

        xml_content = create_xml_chapter(chapter_title, chapter_content)

        # Add chapter number to the filename
        filename = f"{output_dir}/{chapter_title.replace(' ', '_')}.xhtml"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(xml_content)
        print(f"Created: {filename}")


# Example usage
pdf_path = "examples/transformed-moving-to-the-product-operating-model-silicon-valley-product-group-1nbsped-9781119697336-9781119697404-9781119697398.pdf"
chapters_dict = {
    "0": (9, 28),
    "1": (29, 32),
    "2": (33, 36),
    "3": (37, 41),
    "4": (42, 50),
    "5": (51, 54),
    "6": (55, 68),
    "7": (69, 74),
    "8": (75, 85),
    "9": (86, 105),
    "10": (106, 116),
    "11": (117, 120),
    "12": (121, 125),
    "13": (126, 140),
    "14": (141, 152),
    "15": (153, 166),
    "16": (167, 176),
    "17": (177, 187),
    "18": (188, 204),
    "19": (205, 215),
    "20": (216, 239),
    "21": (240, 248),
    "22": (249, 252),
    "23": (253, 261),
    "24": (262, 268),
    "25": (269, 273),
    "26": (274, 281),
    "27": (282, 307),
    "28": (308, 309),
    "29": (310, 332),
    "30": (333, 340),
    "31": (341, 359),
    "32": (360, 371),
    "33": (372, 381),
    "34": (382, 413),
    "35": (414, 438),
    "36": (439, 443),
    "37": (444, 449),
    "38": (450, 454),
    "39": (455, 459),
    "40": (460, 463),
    "41": (464, 466),
    "42": (467, 471),
    "43": (472, 474),
    "44": (475, 476),
    "45": (477, 479),
    "46": (480, 493),
    "47": (494, 502),
    "48": (503, 516),
    "50": (517, 529),
}
output_dir = "book"

process_book(pdf_path, chapters_dict, output_dir)

print(
    "\nProcessing complete. Please check the full_text.txt file in the output directory to verify the content and page numbers."
)
