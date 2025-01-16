from pathlib import Path

file_names = ['chapter_10\\text_files\\cats.txt', 
              'chapter_10\\text_files\\dog.txt']

for file in file_names:
    path = Path(file)
    print(f"Reading file {file}:")
    try:
        content = path.read_text()
        print(f"{content.title()}\n")
    except FileNotFoundError:
        print(f"The file {file} does not exist.\n")