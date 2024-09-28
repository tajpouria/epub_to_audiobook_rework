import PyPDF2
import re


def locate_chapters(pdf_path):
    chapters_dict = {}
    last_chapter_page = 0

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        print(f"Total pages in the PDF: {total_pages}")
        print("Locating chapters...")

        chapter_pattern = re.compile(r"^\s*CHAPTER\s+(\d+)", re.MULTILINE)

        for page_num in range(total_pages):
            page = reader.pages[page_num]
            text = page.extract_text()

            # Remove any leading whitespace from the page text
            text = text.lstrip()

            if text.startswith("CHAPTER"):
                match = chapter_pattern.match(text)
                if match:
                    chapter_num = match.group(1)
                    if last_chapter_page > 0:
                        chapters_dict[str(int(chapter_num) - 1)] = (
                            last_chapter_page,
                            page_num,
                        )
                    last_chapter_page = page_num + 1
                    print(f"Found CHAPTER {chapter_num} on page {page_num + 1}")

    # Add the last chapter
    if last_chapter_page > 0:
        chapters_dict[str(len(chapters_dict) + 1)] = (last_chapter_page, total_pages)

    return chapters_dict


# Use the provided file path
pdf_path = "examples/transformed-moving-to-the-product-operating-model-silicon-valley-product-group-1nbsped-9781119697336-9781119697404-9781119697398.pdf"
result = locate_chapters(pdf_path)

print("\nFinal chapters_dict:")
print("chapters_dict = {")
for chapter, (start, end) in result.items():
    print(f'    "{chapter}": ({start}, {end}),')
print("}")
