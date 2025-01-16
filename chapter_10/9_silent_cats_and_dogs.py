from pathlib import Path

file_names = ['chapter_10\\text_files\\cats.txt', 
              'chapter_10\\text_files\\dog.txt']

for file in file_names:
    path = Path(file)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"Reading file {file}:")
        print(f"{content.title()}\n")