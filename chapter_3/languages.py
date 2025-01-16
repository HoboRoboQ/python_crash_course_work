languages = ['spanish', 'english', 'japanese', 'french', 'italian', 'german', 
             'chinese', 'korean', 'sign language']
print(languages)

print(languages[3].title())
print(languages[6].title())

message = f"The language I have studied the longest is {languages[2].title()}."
print(message)

languages[0] = 'russian'
print(f"I have never studied {languages[0].title()}.")

languages.append('spanish')
print(languages)

languages.insert(4, 'portuguese')
print(languages)

del languages[0]
print(languages)

popped_lang = languages.pop(3)
print(popped_lang.title())
print(languages)

second_lang = languages.pop(2)
print(f"The second language I ever studied was {second_lang.title()}.")

languages.remove('sign language')
print(languages)

languages = ['spanish', 'english', 'japanese', 'french', 'italian', 'german',
             'chinese', 'korean', 'sign language']
print(languages)

languages.sort()
print(languages)

languages = ['spanish', 'english', 'japanese', 'french', 'italian', 'german',
             'chinese', 'korean', 'sign language']
print(languages)
print(sorted(languages))
print(languages)
print(sorted(languages, reverse=True))

languages.reverse()