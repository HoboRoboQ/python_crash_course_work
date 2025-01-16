age = int(input("How old are you?\n"))

if age < 2:
    stage = 'baby'
elif age >= 2 and age < 4:
    stage = 'toddler'
elif age >= 4 and age < 13:
    stage = 'kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f"You are a(n) {stage}!")