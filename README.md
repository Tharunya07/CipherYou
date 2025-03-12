# CipherYou


CipherYou is a lightweight file encryption tool designed with Python, PyQt5 and PBKDF2.

---

## Features
- AES-256 Encryption
- Only you can decrypt your files
- Secure File Deletion

---

## 🔧 Installation
### 1. Install Dependencies
Ensure Python **3.8+** is installed, then run:
```
pip install pyqt5 cryptography
```
### 2. Clone the Repo
```
git clone https://github.com/Tharunya07/CipherYou.git
cd CipherYou
```
### 3. Run the tool
```
python main.py
```

---
CipherYou uses AES encryption with PBKDF2 key derivation, ensuring strong security:
- PBKDF2 Key Derivation – Prevents brute-force attacks.
- Unique Salt for Each Encryption – Ensures every encryption is unique.
- 12-Character Minimum Password – Blocks weak passwords.
- Three Tries, Then Lockout – Stops repeated password guessing.
- Metadata Protection – Keeps file information hidden.
- Secure File Deletion – Original files are erased after encryption.
---

## 🛠 How It Works

#### 1. Open CipherYou and select Encrypt a File.
#### 2. Choose a file and enter a strong password.
#### 3. The file is encrypted and the original securely erased.

To decrypt, simply select an encrypted file (.enc), enter the correct password (3 attempts max), and restore your file.
