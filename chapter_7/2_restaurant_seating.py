count = input("How many people are in your dining group? ")
count = int(count)

if count <= 8:
    print(f"Your table for {count} is ready.")
else:
    print("You will have to wait for a table. Sorry for the inconvenience.")