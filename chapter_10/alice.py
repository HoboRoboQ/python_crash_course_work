from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

file_names = ['chapter_10\\text_files\\alice.txt', 
              'siddhartha.txt',
              'chapter_10\\text_files\\moby_dick.txt',
              'chapter_10\\text_files\\little_women.txt']

for filename in file_names:
    path = Path(filename)
    count_words(path)