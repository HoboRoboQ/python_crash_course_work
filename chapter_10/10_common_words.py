from pathlib import Path

books = ['chapter_10\\text_files\\alice.txt', 
              'chapter_10\\text_files\\crime_and_punishment.txt',
              'chapter_10\\text_files\\pride_and_prejudice.txt',
              'chapter_10\\text_files\\little_women.txt']

for book in books:
    try:
        path = Path(book)
    except FileNotFoundError:
        pass
    else:
        content = path.read_text(encoding='utf-8')
        search_word = 'the '
        content.count(search_word.lower())
        print(f"Reading {book}.\nCounting '{search_word}' in text:")
        print(f"The word '{search_word}' appears {content.count(search_word)} "
              "times!\n")