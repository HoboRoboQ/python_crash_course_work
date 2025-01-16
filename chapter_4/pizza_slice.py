pizzas = ['hawaiian', 'spicy sausage', 'pepperoni', 'vege', 'cheese burger']

print("The first three items in this list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("\nThe three items from the middle are:")
for pizza in pizzas[1:4]:
    print(pizza)

print("\nThe last 3 items on the list are:")
for pizza in pizzas[-3:]:
    print(pizza)