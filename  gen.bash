python main.py ./examples/1984.epub out/ --tts openai --newline_mode double --chapter_start 2 --chapter_e
nd 4 --output_text

autosubsync ./openai/0004_Chapter_1.mp3 ./openai/0004_Chapter_1-draft.srt ./openai/0004_Chapter_1.srt


ffs ./openai/0004_Chapter_1.mp3 -i ./openai/0004_Chapter_1-draft.srt -o ./openai/0004_Chapter_1.srt

./alass-linux64 ./openai/0004_Chapter_1.mp3 ./openai/0004_Chapter_1-draft.srt ./openai/0004_Chapter_1.srt

time auto_subtitle ./openai/0004_Chapter_1.mp3 -o openai/


time faster_auto_subtitle ./openai/0004_Chapter_1.mp3 -o openai/


# Solution 1
# sudo apt-get install ffmpeg espeak libespeak-dev
# python -m pip install aeneas
python -m aeneas.tools.execute_task ./openai/0004_Chapter_1.mp3 ./openai/0004_Chapter_1.txt \
"task_language=eng|is_text_type=plain|os_task_file_format=json" \
output.json
