from datetime import datetime


class User:
    """abstract User class"""
    
    def __init__(self, user_id, email, password, last_name, is_active):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.last_name = last_name
        self.is_active = is_active
    
    def get_full_name(self):
        """Returns the full name of the user"""
        return f"{self.last_name}"
    
    def can_access_system(self):
        """Checks if user can access the system"""
        return self.is_active
