from cryptography.fernet import Fernet

#Encrypt any data that goes through this function
def encrypt(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(data.encode())
    return encMessage

#Decrypt any data that goes through this function
def decrypt(data):
    decMessage = fernet.decrypt(data).decode()
    return decMessage
