favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")

polling = ['ryan', 'fran', 'jen', 'sarah', 'nat']
for pollee in polling:
    if pollee in favorite_languages.keys():
        print(f"Thank you {pollee.title()} for taking the poll.")
    else:
        print(f"What is your favorite programming language {pollee.title()}?")
