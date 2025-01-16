from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('chapter_10\\text_files\\programming.txt')
path.write_text(contents)