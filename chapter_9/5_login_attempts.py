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

    # def set_login_attempts(self, login_attempts):
    #     """Set the number of login attempts."""
    #     self.login_attempts = login_attempts
    
    def increment_login_attempts(self):
        """Increase the number of login attempts."""
        self.login_attempts += 1
    
    def rest_login_attempts(self):
        """Resets the number of login attempts."""
        self.login_attempts = 0

carlos = User('carlos', 'lopez', 'hoboroboq', 'mangayatsu@gmail.com', 
              'March 14th')
carlos.describe_user()
print(f"Login attempts: {carlos.login_attempts}")
carlos.increment_login_attempts()
print(f"Login attempts: {carlos.login_attempts}")
carlos.increment_login_attempts()
print(f"Login attempts: {carlos.login_attempts}")
carlos.increment_login_attempts()
print(f"Login attempts: {carlos.login_attempts}")

carlos.rest_login_attempts()
print(f"Login attempts: {carlos.login_attempts}")