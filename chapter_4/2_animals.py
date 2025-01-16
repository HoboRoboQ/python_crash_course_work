animals = ['alpaca', 'axlotl', 'parrot']
for pet in animals:
    print(f"A(n) {pet} would make a good pet.")

print("\nAll of these animals are freakin adorable!")

numbers = list(range(1, 11))
print(numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)