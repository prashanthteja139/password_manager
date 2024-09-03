# Password Manager

A simple password manager tool built with Python that allows users to securely store, manage, and generate passwords. The project uses encryption to ensure that stored passwords are kept safe.

## Features

- **Password Storage**: Securely store passwords using encryption.
- **Password Retrieval**: Retrieve stored passwords.
- **Password Generation**: Generate strong, random passwords.
- **Secure Access**: Access to stored passwords is protected using encryption keys.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/prashanthteja139/password_manager.git
   cd password_manager
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not provided, you can manually install the `cryptography` library:

   ```bash
   pip install cryptography
   ```

## Usage

1. **Run the Password Manager**:

   ```bash
   python password_manager.py
   ```

2. **Options**:
   - **Save Password**: Save a new password for a specific service.
   - **Retrieve Password**: Retrieve an existing password for a specific service.
   - **Generate Password**: Generate a strong, random password.
   - **Exit**: Exit the password manager.

## Encryption

This password manager uses the `cryptography` library's `Fernet` symmetric encryption to secure passwords. A unique encryption key is generated and stored locally in the `secret.key` file. Ensure this file is kept secure, as it is required to encrypt and decrypt your passwords.

## Project Structure

```
password_manager/
├── venv/                 # Virtual environment directory
├── passwords.json        # Encrypted passwords storage (created on first use)
├── secret.key            # Encryption key file
├── password_manager.py   # Main script
├── utils.py              # Utility functions for encryption/decryption
└── README.md             # Project documentation
```

## Security Considerations

- Keep the `secret.key` file secure. If this key is lost or compromised, you will not be able to access your encrypted passwords.
- Use a strong password for your services to enhance security.
- Regularly back up the `passwords.json` and `secret.key` files.


## Acknowledgments

- This project uses the [cryptography](https://cryptography.io/) library for secure encryption.
- Inspired by the need for simple and secure password management.
