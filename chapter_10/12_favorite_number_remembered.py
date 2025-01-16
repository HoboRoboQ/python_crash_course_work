from pathlib import Path
import json

def get_stored_number(path):
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None
    
def get_new_number(path):
    favorite_number = input("What is your favorite number?: ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number

def give_favorite_number():
    path = Path('favorite_number.json')
    favorite_number = get_stored_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_number(path)

give_favorite_number()