import hashlib

def generate_user_id():
    wallet_balance = "0"
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    username_n_password = username + password
    user_key_prefix = hashlib.sha256(username_n_password.encode()).hexdigest()
    user_key = user_key_prefix + "_" + wallet_balance
    
    print(user_key)

def send():
    sender_key = input("Enter sender key: ")
    reciver_key = input("Enter reciver key: ")
    amount = input("Enter amount to send: ")

    res = sender_key.split("_", 1)
    sender_balance = res[1]

    with open("user_keys.txt") as user_keys:
        keys = user_keys.read()

        if sender_key and reciver_key in keys:
            if amount > sender_balance:
                print("Error not enough funds; ", sender_balance, " is smaller then ", amount)
            else:
                f = open("user_keys.txt"):
                f.wr
        else:
            print("Invalid sender or reciver key")

send()