from pathlib import Path

path = Path('chapter_10\\text_files\\learning_python.txt')
contents = path.read_text()
print(contents)


print("\nNow printing in loop per line:")
lines = contents.splitlines()
for line in lines:
   print(line)