# Local Password Vault

A secure **offline password manager** that stores your website login credentials using **encryption**.  
The project ensures all sensitive data is encrypted and only accessible through a master password.  

---

## Why?
Everyone needs a secure, offline tool for managing passwords without relying on third-party cloud solutions.  

---

## Encryption Workflow

1. **First Use**:  
   - Set a **master password**.  
   - Master password is **hashed** and stored securely.  

2. **On Launch**:  
   - Verify the master password at every login.  

3. **Storing Credentials**:  
   - Each password is **encrypted** using **Fernet** from the `cryptography` library.  
   - Encrypted credentials are stored in the local database.  

4. **Decryption**:  
   - Passwords are only **decrypted on demand** when the user requests them.  
   - Decrypted values are **never stored in plain text**.  

---

## Core Features

- 🔑 **Master Password Gate**: One-time login at launch.  
- 🔒 **Password Encryption**: All credentials are encrypted in the database.  
- 🔍 **Search Functionality**: Find credentials by website or category.  
- 📋 **Clipboard Support**: Copy password securely to clipboard for quick use.  
- ➕ **Add / View / Edit / Delete** credentials easily.  

---

## Bonus Features

- 🔧 **Password Generator Tool**: Generate strong, random passwords.  
- ⏳ **Auto Logout**: Log out automatically after inactivity.  
- 📂 **Export Encrypted Backup**: Backup and restore encrypted database.  
- 📋 **Clipboard Integration**: Securely copy password values to clipboard.  
- 🖥 **GUI Support**:  
  - Tkinter  
  - PyQt  
  - Streamlit  
- 🏷 **Categorize / Tag Credentials**: Organize logins by tags or categories.  

---
