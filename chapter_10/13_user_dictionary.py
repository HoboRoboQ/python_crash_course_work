from pathlib import Path
import json

def get_new_user(path):
    username = input("What is your username?: ")
    email = input("What is your email?: ")
    game = input("What is your favorite game?: ")

    user_dict = {
        'username' : username,
        'email' : email,
        'game' : game
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def retrieve_user_info(path):
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def greet_user():
    path = Path('user_info,json')
    user_dict = retrieve_user_info(path)
    verify = input(f"Are you {user_dict['username']} (y/n)?: ")
    if verify == 'n':
        user_dict = get_new_user(path)
        print("We will remember you for next time.")
    else:
        print(f"Welcome back {user_dict['username']}.")
        print(f"\t- email: {user_dict['email']}")
        print(f"\t- Favorite game: {user_dict['game']}")

greet_user()