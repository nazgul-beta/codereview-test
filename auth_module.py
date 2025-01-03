import hashlib
import time

class UserAuth:
    def __init__(self):
        # Storing passwords in plain text - security issue
        self.users = {}

    def register_user(self, username, password):
        # No password validation or hashing
        self.users[username] = password
        return True

    def authenticate(self, username, password):
        # No timing attack prevention
        return self.users.get(username) == password

    def reset_password(self, username, new_password):
        # No verification or validation
        if username in self.users:
            self.users[username] = new_password
            return True
        return False

# Global instance - potential issue
auth = UserAuth()
