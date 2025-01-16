usernames = ['nemasu', 'chesca', 'lilkusaotaku', 'puddles', 'seasonal weeb', 
            'admin','best bean', 'gomaboi']
#usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin. Would you like to see a status report?")
        else:
            print(f"Hello {user}. Thanks for logging in today")
else:
    print("We need to find some users!")