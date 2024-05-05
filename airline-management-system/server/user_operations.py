from datetime import datetime

class Register:
    def __init__(self, users_instance):
        self.users_instance = users_instance
        self.accounts_collection = self.users_instance.accounts_collection
        self.users_collection = self.users_instance.users_collection

    def register_user(self, username, password, email, first_name, last_name, phone_number, address):
        existing_user = self.accounts_collection.find_one({'username': username})
        if existing_user:
            return False, 'User already exists'

        user_id = str(self.accounts_collection.count_documents({}) + 1)
        user_doc = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'address': address,
            'role': 'Customer',
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.users_collection.insert_one(user_doc)

        new_user = {'username': username, 'password': password, 'user_id': user_id}
        self.accounts_collection.insert_one(new_user)

        return True, 'User registered successfully'

class Login:
    def __init__(self, users_instance):
        self.users_instance = users_instance
        self.accounts_collection = self.users_instance.accounts_collection

    def handle_login(self, username, password):
        user = self.accounts_collection.find_one({'username': username, 'password': password})
        if user:
            return True, user
        else:
            return False, None
