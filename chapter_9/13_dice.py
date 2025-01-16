from random import randint

class Die:
    """Represent a die, which can be rolled."""

    def __init__(self,sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_dice(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

#D6 rolls
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("10 rolls of a d6:")
print(results)

#D10 rolls
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print("10 rolls of a d10:")
print(results)

#D20 rolls
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)
print("10 rolls of a d20:")
print(results)