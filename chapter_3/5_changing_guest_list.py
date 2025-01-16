guests = ['francesca valcarcel', 'eiichiro oda', 'shinonome umi']
print(guests)

print(f"Dear {guests[0].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[1].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[2].title()}, you are invited to dinner tonight.")

print(f"Unfortunately, {guests[1].title()} will not be able to join us.")

removed_guests = guests.pop(1)
print(removed_guests.title())

guests.insert(1, 'hutachan')
print(guests)
print(f"Dear {guests[0].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[1].title()}, you are invited to dinner tonight.")
print(f"Dear {guests[2].title()}, you are invited to dinner tonight.")