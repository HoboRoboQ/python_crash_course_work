from pathlib import Path

path = Path('chapter_10\\text_files\\guest.txt')

name = input("What's your name? ").title()
path.write_text(name)