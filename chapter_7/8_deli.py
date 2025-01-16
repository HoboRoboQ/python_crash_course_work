sandwich_order = ['pastrami', 'meatball melt', 'philly cheese',]

finished_orders = []

while sandwich_order:
    current_order = sandwich_order.pop()

    print(f"Now preparing your {current_order}.")
    finished_orders.append(current_order)

print("The following orders have been completed:")
for finished in finished_orders:
    print(f"\t{finished}")