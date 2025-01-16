prompt = "Enter a number: "

print("Please enter 2 numbers. Enter 'q' to quit.\n")

while True:
    try:
        first_number = input(prompt)
        if first_number == 'q':
            break
        first_number = int(first_number)

        second_number = input(prompt)
        if second_number == 'q':
            break
        second_number = int(second_number)
    except ValueError:
        print("Please enter only numbers.\n")
    else:
        sum = first_number + second_number
        print(f"Sum = {sum}\n")