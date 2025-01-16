class User:
    """Creates model of user"""

    def __init__(self, first_name, last_name, username, email, date_of_birth):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.date_of_birth = date_of_birth

    def describe_user(self):
        """Display summary of user information"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Date of Birth: {self.date_of_birth}")
    
    def greet_user(self):
        """Display greeting to user"""
        print(f"\nWelcome back, {self.username}")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'June 2nd')
eric.describe_user()
eric.greet_user()

carlos = User('carlos', 'lopez', 'hoboroboq', 'mangayatsu@gmail.com', 
              'March 14th')
carlos.describe_user()
carlos.greet_user()