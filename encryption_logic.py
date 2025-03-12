import base64
import os
import hashlib
import hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

class EncryptionLogic:
    @staticmethod
    def derive_key(password: str, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,  
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    @staticmethod
    def encrypt_file(file_path: str, password: str) -> str:
        if len(password) < 12:
            return "Error: Password too short. Must be at least 12 characters."

        salt = os.urandom(16) 
        key = EncryptionLogic.derive_key(password, salt)
        cipher = Fernet(key)

        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = cipher.encrypt(file_data)

            encrypted_file_path = file_path + ".enc"
            with open(encrypted_file_path, "wb") as file:
                file.write(salt + encrypted_data)

            EncryptionLogic.secure_delete(file_path)

            return encrypted_file_path
        except Exception as e:
            return str(e)

    @staticmethod
    def decrypt_file(file_path: str, password: str) -> str:
        if not file_path.endswith(".enc"):
            return "Error: This file is not encrypted."

        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            salt = encrypted_data[:16]  
            encrypted_content = encrypted_data[16:]  
            key = EncryptionLogic.derive_key(password, salt)
            cipher = Fernet(key)

            decrypted_data = cipher.decrypt(encrypted_content)

            new_file_path = file_path.replace(".enc", "")
            with open(new_file_path, "wb") as file:
                file.write(decrypted_data)

            return new_file_path
        except Exception as e:
            return "Error: Incorrect password or file integrity compromised."

    @staticmethod
    def secure_delete(file_path: str):
        try:
            with open(file_path, "ba+") as f:
                f.seek(0)
                f.write(os.urandom(1024))  
                f.flush()
            os.remove(file_path)  
        except Exception as e:
            print(f"Warning: Secure delete failed - {e}")
