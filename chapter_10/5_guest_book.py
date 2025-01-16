from pathlib import Path

path = Path('chapter_10\\text_files\\guest_book.txt')

# prompt = "What's your name?"
# prompt += "\nType 'quit' once finished: "

# guest_book = ''
# while True:
#     name = input(f"{prompt}")
#     if name == 'quit':
#         break
#     else:
#         guest_book += f"{name.title()}\n"
#         path.write_text(guest_book)

prompt = "\nHi, what's your name?"
prompt += "\nEnter 'quit' if you're the last guest. "

guest_name = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you the the guest book.")
    guest_name.append(name.title())

file_string = ''
for name in guest_name:
    file_string += f"{name}\n"

path.write_text(file_string)