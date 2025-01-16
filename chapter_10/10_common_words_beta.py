from pathlib import Path

book_list = ['chapter_10\\text_files\\alice.txt', 
              'chapter_10\\text_files\\crime_and_punishment.txt',
              'chapter_10\\text_files\\pride_and_prejudice.txt',
              'chapter_10\\text_files\\little_women.txt']

def count_common_words(file, search):
    path = Path(file)
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        word_count = content.lower().count(search)
        print(f"The word '{search}' appears in {file} {word_count} times.\n")

search = input("What word would you like to search?: ")
search_book = input("Which file would you like to search in (0-3): ")
book = book_list[int(search_book)]
count_common_words(book, search)