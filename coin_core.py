import hashlib
import time

def generate_user_id():
    wallet_balance = "0"
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    username_n_password = username + password
    user_key_prefix = hashlib.sha256(username_n_password.encode()).hexdigest()
    user_key = user_key_prefix + "_" + wallet_balance

    f = open("user_keys.txt", "a")
    f.write(user_key)
    f.write("\n")
    f.close()
    
    print("Your key: (remember it)", user_key)

def send():
    sender_key = input("Enter sender key: ")
    reciver_key = input("Enter reciver key: ")
    amount = input("Enter amount to send: ")

    s = sender_key.split("_", 1)
    sender_balance = s[1]

    r = reciver_key.split("_", 1)
    reciver_balance = r[1]

    with open("user_keys.txt") as user_keys:
        keys = user_keys.read()

        if sender_key and reciver_key in keys:
            if amount > sender_balance:
                print("Error not enough funds")
            else:
                new_sender_balance = int(sender_balance) - int(amount)
                new_reciver_balance = int(reciver_balance) + int(amount)
                with open('user_keys.txt', 'r') as user_keys :
                    keys = user_keys.read()

                    replace_sender_key = keys.replace(sender_balance, str(new_sender_balance))
                    replace_reciver_key = keys.replace(reciver_balance, str(new_reciver_balance))

                with open('user_keys.txt', 'w') as file:
                    file.write(replace_sender_key)
                time.sleep(10)
                with open('user_keys.txt', 'w') as file:
                    file.write(replace_reciver_key)
        else:
            print("Invalid sender or reciver key")

send()