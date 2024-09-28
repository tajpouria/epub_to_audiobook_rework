import os
import subprocess

# Define the folder containing the text and audio files
folder_path = "./out"
audio_extension = ".mp3"
text_extension = "-splitted.txt"

# Loop through each text file ending with "-splitted.txt"
for filename in os.listdir(folder_path):
    if filename.endswith(text_extension):
        # Get the base name (without the extension) for both audio and text files
        base_name = filename.replace(text_extension, "")
        audio_file = os.path.join(folder_path, base_name + audio_extension)
        text_file = os.path.join(folder_path, filename)
        output_file = os.path.join(folder_path, base_name + ".json")

        # Check if corresponding audio file exists
        if os.path.exists(audio_file):
            # Build the aeneas command
            command = [
                "python", "-m", "aeneas.tools.execute_task",
                audio_file, text_file,
                "task_language=eng|is_text_type=plain|os_task_file_format=json",
                output_file
            ]

            # Run the command
            subprocess.run(command)

            print(f"Processed {text_file} with {audio_file} -> {output_file}")
        else:
            print(f"Audio file not found for {filename}")
