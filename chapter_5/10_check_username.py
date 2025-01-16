current_users = ['nemasu', 'chesca', 'lilkusaotaku', 'puddles', 'seasonal weeb', 
            'nayr7047','best bean', 'gomaboi']
new_users = ['NONKI', 'raigo', 'queenb', 'GOMABOI', 'nemasu', 'coolmank']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, '{new_user}' is taken. Choose another username.")
    else:
        print(f"The username '{new_user}' is available!")