import a_make_album as ama

# Prompts for the inputs
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who is the artist? "

# Let user know how to quit
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = ama.make_album(artist, title)
    print(album)

print("\nThanks for responding!")