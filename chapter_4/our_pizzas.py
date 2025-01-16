my_pizzas = ['hawaiian', 'spicy sausage', 'pepperoni']
friend_pizzas = my_pizzas[:]

my_pizzas.append('cheese burger')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friend's favorites pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)