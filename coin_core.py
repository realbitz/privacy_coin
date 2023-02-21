import hashlib

def generate_user_id():
    wallet_balance = "0"
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    username_n_password = username + password
    user_key_prefix = hashlib.sha256(username_n_password.encode()).hexdigest()
    user_key = user_key_prefix + "_" + wallet_balance

    f = open("userkeys.txt")
    f.write(user_key)
    f.write("\n")
    f.close()
    
    print("Your key: (remember it)", user_key)

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
                new_balance = int(sender_balance) - amount
                with open('user_keys.txt', 'r') as user_keys :
                    keys = user_keys.read()

                    filedata = filedata.replace(sender_balance, new_balace)

                with open('user_keys.txt', 'w') as file:
                    file.write(filedata)
        else:
            print("Invalid sender or reciver key")

generate_user_id()