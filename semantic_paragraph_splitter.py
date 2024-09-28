import spacy
import os
import glob

# Load the spaCy English model
nlp = spacy.load("en_core_web_lg")

# Define the input and output directories
input_directory = "out"
output_suffix = "-splitted.txt"

# Get all .txt files from the input directory
txt_files = glob.glob(os.path.join(input_directory, "*.txt"))

# Loop through each file in the directory
for txt_file in txt_files:
    # Read the input text from the file
    with open(txt_file, "r") as file:
        long_string = file.read()

    # Process the text using spaCy
    doc = nlp(long_string)

    # Create paragraphs based on semantic shifts (based on sentence dependencies and topic changes)
    paragraphs = []
    current_paragraph = []

    # Loop through the sentences and detect shifts
    for sent in doc.sents:
        if len(current_paragraph) > 0:
            # You can use the root verb or other dependency parsing to decide when to start a new paragraph
            if current_paragraph[-1].root.head != sent.root.head:
                paragraphs.append(" ".join([s.text for s in current_paragraph]))
                current_paragraph = []
        current_paragraph.append(sent)

    # Don't forget the last paragraph
    if current_paragraph:
        paragraphs.append(" ".join([s.text for s in current_paragraph]))

    # Generate the output filename by appending the suffix
    output_filename = txt_file.replace(".txt", output_suffix)

    # Save the processed paragraphs to the new file
    with open(output_filename, "w") as f:
        f.write("\n\n".join(paragraphs))

    print(f"Output saved to {output_filename}")
