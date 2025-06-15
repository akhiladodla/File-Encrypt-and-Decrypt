# File Encryption/Decryption Tool
## Overview
The File Encryption/Decryption Tool is a Python-based desktop application that securely encrypts and decrypts files using AES-256 encryption. It features a graphical user interface (GUI) built with Tkinter, allowing users to protect sensitive files with a password. The tool incorporates security best practices, such as random salts and initialization vectors (IVs), to ensure robust encryption.
This project was created to learn about file encryption, GUI development, and secure coding in Python.

## Features
- **AES-256 Encryption:** Uses AES-256 in CBC mode with PBKDF2 key derivation. </br>
- **Tkinter GUI:** Simple interface with file selection, password entry, and encrypt/decrypt buttons. </br>
- **Error Handling:** Validates inputs and shows errors (e.g., wrong password, non-.enc file for decryption). </br>
- **File Support:** Works with various file types (text, images, PDFs, etc.).</br>


## Security
- Random salt and IV for unique encryptions.</br>
- **Unit Testing**: Includes a test script to verify functionality.</br>

## Requirements
- Python 3.6+
- **Libraries:**
cryptography
tkinter (usually included with Python)</br>
### Encrypt a File:
- Open the GUI.</br>
- Click "Select File" and choose a file (e.g., test.txt).</br>
- Enter a password.</br>
- Click "Encrypt" to create test.txt.enc.</br>
### Decrypt a File:
- Select the .enc file (e.g., test.txt.enc).
- Enter the same password.
- Click "Decrypt" to create test.txt.dec.

## Project Structure
- **main.py:** GUI and application logic.
- **crypto_engine.py:** Encryption/decryption logic using the cryptography library.
- **test_crypto.py:** Unit test script.
- Sample files (e.g., test.txt) are not included; create your own for testing.

## Future Enhancements
- Add HMAC for file integrity.
- Include a progress bar for large files.
- Package as an executable with PyInstaller.

