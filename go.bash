epub_path=$1
dest_dir=$2


if [ -z "$epub_path" ] || [ -z "$dest_dir" ]; then
    echo "Usage: go.bash <epub_path> <dest_dir>"
    exit 1
fi

python main.py $epub_path out --tts openai --newline_mode double --output_text --voice_name nova

# python semantic_paragraph_splitter.py

# python process_audio_text_sync.py

# cp out/*.mp3 out/*.json $dest_dir
