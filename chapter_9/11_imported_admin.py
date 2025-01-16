from imported_admin import Admin

carlos = Admin('carlos', 'lopez', 'hoboroboq', 'mangayatsu@gmail.com', 1992)
carlos.describe_user()

carlos_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

carlos.privileges.privileges = carlos_privileges

print(f"\nThe admin {carlos.username} has these privileges:")
carlos.privileges.show_privileges()