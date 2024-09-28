import nltk
import os

# Download the necessary tokenizer from NLTK
nltk.download("punkt")

# Function to split the text into words and keep punctuation attached to the previous word
def split_text_into_words(input_file, output_file):
    # Read the content of the input text file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Use nltk to tokenize the text into words
    words = nltk.word_tokenize(text)

    # Create an empty list to hold words with punctuation attached
    adjusted_words = []
    
    for i in range(len(words)):
        # If the word is punctuation, attach it to the previous word
        if words[i] in ['.', ',', '!', '?', ';', ':', '...', "'", '"', '’']:
            adjusted_words[-1] += words[i]
        else:
            adjusted_words.append(words[i])

    # Write each adjusted word on a new line in the output file
    with open(output_file, "w", encoding="utf-8") as file:
        for word in adjusted_words:
            file.write(word + "\n\n")


# Example usage
input_file = "out/0001_Introduction_The_Greatest_Show_On_Earth.txt"  # Replace with the path to your input file
output_file = "output_text.txt"  # Replace with the path to your output file

# Split text into words, keeping punctuation attached to the previous word
split_text_into_words(input_file, output_file)

print(f"Words have been written to {output_file}")
