prompt = "Please input the topping you would like on your pizza."
prompt += "\n(Enter 'done' once you have finished choosing toppings.): "

while True:
    topping = input(prompt)
    if topping != 'done':
        print(f"\n\tWe will add {topping} to your pizza.\n")
    else:
        break