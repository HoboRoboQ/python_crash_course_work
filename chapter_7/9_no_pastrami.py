sandwich_order = ['pastrami', 'meatball melt', 'pastrami', 'philly cheese',
                   'pastrami', 'blt', 'club',]

finished_orders = []

print("Sorry, we are out of pastrami today.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

print("\n")
while sandwich_order:
    current_order = sandwich_order.pop()
    print(f"Working on your {current_order}.")
    finished_orders.append(current_order)
    
print("\n")
for order in finished_orders:
    print(f"Done with your {order} sandwich.")