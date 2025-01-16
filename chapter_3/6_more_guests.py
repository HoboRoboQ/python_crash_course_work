guests = ['francesca valcarcel', 'eiichiro oda', 'shinonome umi']
print(f"Unfortunately, {guests[1].title()} will not be able to join us.")

removed_guests = guests.pop(1)
print(removed_guests.title())

guests.insert(1, 'huta chan')
print(guests)
print(f"Dear {guests[0].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[1].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[2].title()}, you are invited to dinner tonight.")
print("A bigger table is now available!")

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