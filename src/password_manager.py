from cryptography.fernet import Fernet, InvalidToken
import json
import base64

class PasswordManager:
    def __init__(self, key_file='key.key', data_file='passwords.json'):
        self.key_file = key_file
        self.data_file = data_file

        # Load or generate encryption key
        self.load_or_generate_key()

        # Initialize the Fernet symmetric encryption object
        self.cipher_suite = Fernet(self.key)

        # Load passwords from file
        self.load_passwords()

    def edit_password(self):
        service = input("Enter the service you want to edit: ")
        if service in self.passwords:
            print(f"Current details for {service}:")
            print(f"Username: {self.passwords[service]['username']}")
            print(f"Password: {self.passwords[service]['password']}")

            new_username = input("Enter the new username (press Enter to keep current): ")
            new_password = input("Enter the new password (press Enter to keep current): ")

            if new_username:
                self.passwords[service]['username'] = new_username
            if new_password:
                self.passwords[service]['password'] = new_password

            self.save_passwords()
            print(f"Details updated for {service}.")
        else:
            print(f"No password found for {service}.")

    def show_passwords(self):
        if not self.passwords:
            print("No passwords stored.")
        else:
            print("\nPasswords:")
            print("{:<20} {:<20} {:<20}".format("Service", "Username", "Password"))
            print("="*60)
            for service, credentials in self.passwords.items():
                print("{:<20} {:<20} {:<20}".format(service, credentials['username'], credentials['password']))
            print("="*60)
    
    def remove_password(self):
        service = input("Enter the service you want to remove: ")
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            print(f"Password removed for {service}.")
        else:
            print(f"No password found for {service}.")

    def load_or_generate_key(self):
        try:
            # Load the key from file
            with open(self.key_file, 'rb') as key_file:
                self.key = key_file.read()

            # Check if the key is the correct length
            if len(self.key) != 44 or not base64.urlsafe_b64decode(self.key):
                raise ValueError("Invalid key format")

        except (FileNotFoundError, ValueError):
            # Generate a new key if not found or invalid
            key = Fernet.generate_key()
            self.key = base64.urlsafe_b64encode(key[:32])  # Ensure the key is 32 bytes
            with open(self.key_file, 'wb') as key_file:
                key_file.write(self.key)

    def load_passwords(self):
        try:
            # Load encrypted passwords from file
            with open(self.data_file, 'rb') as data_file:
                encrypted_data = data_file.read()

            # Decrypt and deserialize passwords
            decrypted_data = self.cipher_suite.decrypt(encrypted_data)

            # Deserialize the decrypted data as JSON
            self.passwords = json.loads(decrypted_data.decode())

        except (FileNotFoundError, json.JSONDecodeError, InvalidToken):
            # Initialize with an empty dictionary if file not found, invalid format, or invalid token
            self.passwords = {}

    def save_passwords(self):
        # Serialize and encrypt passwords
        encrypted_data = self.cipher_suite.encrypt(json.dumps(self.passwords).encode())

        # Save encrypted passwords to file
        with open(self.data_file, 'wb') as data_file:
            data_file.write(encrypted_data)

    def add_password(self, service, username, password):
        # Add or update password for a service
        self.passwords[service] = {'username': username, 'password': password}
        self.save_passwords()
        print(f"Password added/updated for {service}.")

    def get_password(self, service):
        # Retrieve password for a service
        return self.passwords.get(service, None)

def print_welcome():
    welcome_message = """
    *************************************
    Welcome to the Password Manager App!
    *************************************
    Developed by: [ Danial Pilehvarzadeh ]
    """
    print(welcome_message)

def main():
    print_welcome()
    
    password_manager = PasswordManager()

    while True:
        print("\nOptions:")
        print("1. Add Password")
        print("2. Edit Password")
        print("3. Remove Password")
        print("4. Show Passwords")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # Add Password
            service = input("Enter the service: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            password_manager.add_password(service, username, password)
            print(f"Password added/updated for {service}.")

        elif choice == '2':
            # Edit Password
            password_manager.edit_password()

        elif choice == '3':
            # Remove Password
            password_manager.remove_password()

        elif choice == '4':
            # Show Passwords
            password_manager.show_passwords()

        elif choice == '5':
            # Exit the loop
            password_manager.save_passwords()  # Save passwords before exiting
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
