guests = ['francesca valcarcel', 'eiichiro oda', 'shinonome umi']
print(guests)
print(f"Unfortunately, {guests[1].title()} will not be able to join us.")

#Removing guest and replacing
removed_guests = guests.pop(1)
guests.insert(1, 'huta chan')
print(guests)

print(f"Dear {guests[0].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[1].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[2].title()}, you are invited to dinner tonight.")
print("A bigger table is now available!")

#Adding people to bigger table
guests.insert(0, 'amagami rui')
guests.insert(2, 'nishimura kinu')
guests.append('shimura takako')
print(guests)

print(f"Dear {guests[0].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[1].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[2].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[3].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[4].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[5].title()}, you are invited to dinner tonight.")

#Shrinking list to 2
removed_1 = guests.pop(5)
print(f"Sorry {removed_1.title()}, I can only invite two to dinner.")

removed_2 = guests.pop(4)
print(f"Sorry {removed_2.title()}, I can only invite two to dinner.")

removed_3 = guests.pop(3)
print(f"Sorry {removed_3.title()}, I can only invite two to dinner.")

removed_4 = guests.pop(2)
print(f"Sorry {removed_4.title()}, I can only invite two to dinner.")

print(f"Dear {guests[0].title()}, you are still invited to dinner tonight.")
print(f"Dear {guests[1].title()}, you are still invited to dinner tonight.")

del guests[1]
del guests[0]
print(guests)