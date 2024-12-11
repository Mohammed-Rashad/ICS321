class User:
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

    @staticmethod
    def find_by_username(username):
        # Example query logic (replace with real DB query)
        return None
