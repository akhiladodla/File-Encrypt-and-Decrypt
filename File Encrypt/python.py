# Quick test script
from crypto_engine import CryptoEngine

crypto = CryptoEngine("mypassword")
crypto.encrypt_file("test.txt", "test.txt.enc")
crypto = CryptoEngine("mypassword")
crypto.decrypt_file("test.txt.enc", "test.txt.dec")