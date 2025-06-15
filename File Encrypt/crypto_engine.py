from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

class CryptoEngine:
    def __init__(self, password: str):
        self.password = password.encode()  # Convert password to bytes
        self.salt = os.urandom(16)  # Generate a random 16-byte salt
        self.key = self._derive_key()  # Derive the encryption key

    def _derive_key(self):
        # Use PBKDF2 to derive a 256-bit key from the password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256-bit key (32 bytes)
            salt=self.salt,
            iterations=100000,  # High iteration count for security
        )
        return kdf.derive(self.password)

    def encrypt_file(self, input_file: str, output_file: str):
        # Generate a random 16-byte IV for CBC mode
        iv = os.urandom(16)
        # Set up AES-256 in CBC mode with the derived key and IV
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        # Open input and output files
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            # Write salt and IV to the output file
            f_out.write(self.salt)
            f_out.write(iv)
            # Read and encrypt the file in 8KB chunks
            while True:
                chunk = f_in.read(8192)  # 8KB chunks for efficiency
                if not chunk:
                    break
                encrypted_chunk = encryptor.update(chunk)
                f_out.write(encrypted_chunk)
            # Finalize encryption (handles padding)
            f_out.write(encryptor.finalize())

    def decrypt_file(self, input_file: str, output_file: str):
        # Read the salt, IV, and encrypted data from the input file
        with open(input_file, 'rb') as f_in:
            salt = f_in.read(16)  # Read the 16-byte salt
            iv = f_in.read(16)  # Read the 16-byte IV
            encrypted_data = f_in.read()  # Read the rest (encrypted data)

        # Re-derive the key using the stored salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(self.password)

        # Set up AES-256 in CBC mode for decryption
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        # Decrypt and write the data to the output file
        with open(output_file, 'wb') as f_out:
            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
            f_out.write(decrypted_data)