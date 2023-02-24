import hashlib
import time

def generate_user_id():
    wallet_balance = "0"
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    user_key_prefix = hashlib.sha256((username + password).encode()).hexdigest()
    user_key = f"{user_key_prefix}_{wallet_balance}"

    with open("user_keys.txt", "a") as f:
        f.write(user_key + "\n")
    
    print("Your key: (remember it)", user_key)

def send():
    sender_key = input("Enter sender key: ")
    receiver_key = input("Enter receiver key: ")
    amount = int(input("Enter amount to send: "))

    with open("user_keys.txt", "r") as user_keys:
        keys = user_keys.readlines()

    sender_index = -1
    receiver_index = -1
    for i, key in enumerate(keys):
        if key.startswith(sender_key):
            sender_index = i
        elif key.startswith(receiver_key):
            receiver_index = i

        if sender_index != -1 and receiver_index != -1:
            break

    if sender_index == -1 or receiver_index == -1:
        print("Invalid sender or receiver key")
        return

    sender_key_parts = keys[sender_index].strip().split("_")
    receiver_key_parts = keys[receiver_index].strip().split("_")

    sender_balance = int(sender_key_parts[1])
    receiver_balance = int(receiver_key_parts[1])

    if sender_balance < amount:
        print("Error not enough funds")
        return

    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount

    sender_key_parts[1] = str(new_sender_balance)
    receiver_key_parts[1] = str(new_receiver_balance)

    keys[sender_index] = "_".join(sender_key_parts) + "\n"
    keys[receiver_index] = "_".join(receiver_key_parts) + "\n"

    with open("user_keys.txt", "w") as user_keys:
        user_keys.writelines(keys)

    print("Transaction successful!")

send()