from import_user import User

class Admin(User):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name, username, email, date_of_birth):
        super().__init__(first_name, last_name, username, email, date_of_birth)
        self.privileges = Privileges()

class Privileges:
    """A class to store admin privileges."""
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        """Display the admin privileges."""
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")