print("I will determine whether or not a number is a multiple of 10.")
number = input("Please give me a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10!")
else:
    print(f"{number} is not a multiple of 10.")