# Password Manager

## Introduction

Welcome to the Password Manager App! This Python script allows users to securely manage their passwords for various services. Developed by Danial Pilehvarzadeh, this app utilizes encryption to store and retrieve passwords.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required libraries installed: `cryptography`.

```bash
pip install cryptography
```

### How to Run

1- Download the script `password_manager.py`.

2- Open a terminal or command prompt.

3- Navigate to the directory containing `password_manager.py`.

4- Run the script:

```bash
python password_manager.py
```

### Features

### 1-  Add Password:
- Allows users to add or update a password for a specific service.
- Enter the service name, username, and password when prompted.

### 2- Edit Password:
- Provides an option to edit an existing password for a service.
- Users can update the username or password for a specific service.

### 3- Remove Password:
- Allows users to remove a password for a specific service.
- Enter the service name to remove its associated password.

### 4- Show Passwords:
- Displays a list of stored passwords for all services.
- Shows service names along with their corresponding usernames and passwords.

### 5- Exit:
- Safely exits the Password Manager, saving any changes made.

### Security
- Passwords are stored in an encrypted format using the Fernet symmetric encryption algorithm.
- Encryption key is generated or loaded from a file (`key.key`) for secure password storage.

### Troubleshooting
If passwords are not persisting after reopening the app:
- Check file permissions for the key file (`key.key`) and data file (`passwords.json`).
- Verify that file paths are correct in the script.
- Ensure you are running the script in an environment that supports file persistence.
- Check the console for error messages during loading or saving of passwords.



Feel free to further customize the content or add more sections as needed for your project.
