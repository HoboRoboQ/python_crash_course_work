class User:
    """Creates model of user"""

    def __init__(self, first_name, last_name, username, email, date_of_birth):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def describe_user(self):
        """Display summary of user information"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Date of Birth: {self.date_of_birth}")
    
    def greet_user(self):
        """Display greeting to user"""
        print(f"\nWelcome back, {self.username}")

    def set_login_attempts(self, login_attempts):
         """Set the number of login attempts."""
         self.login_attempts = login_attempts
    
    def increment_login_attempts(self):
        """Increase the number of login attempts."""
        self.login_attempts += 1
    
    def rest_login_attempts(self):
        """Resets the number of login attempts."""
        self.login_attempts = 0

class Admin(User):
    """Create model of Admin, special type of user."""
    def __init__(self, first_name, last_name, username, email, date_of_birth):
        super().__init__(first_name, last_name, username, email, date_of_birth)
        self.privileges = []

    def show_privileges(self):
        """Display the admin privileges."""
        print("\nThese are the privileges given to the admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")

carlos = Admin('carlos', 'lopez', 'HRQ', 'mangayatsu@gmail.com', '1992')
carlos.describe_user()

carlos.privileges = [
    'can add post',
    'can delete post',
    'can ban user'
]

carlos.show_privileges()