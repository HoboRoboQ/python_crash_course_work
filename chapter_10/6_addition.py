prompt = "Please enter a number: "

try: 
    first_number = int(input(prompt))
    second_number = int(input(prompt))
except ValueError:
    print("Please enter numbers only.")
else:
    print(first_number + second_number)