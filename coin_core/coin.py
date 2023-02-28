import hashlib
import time

def create_wallet(username, password):
    wallet_balance = "0"
    user_key_prefix = hashlib.sha256((username + password).encode()).decode()
    user_key = user_key_prefix + wallet_balance
    private_key = hashlib.sha256(user_key.encode()).decode()

    print("Your user key: ", user_key)
    print("Your private key: ", private_key)

    f = open("userdata.txt", "a")
    f.write(user_key + "." + private_key + "\n")
    f.close()

def send(sender_key, sender_private_key, receiver_key, amount):
    with open("userdata.txt") as file:
        contents = file.readlines()

    sender_index = -1
    receiver_index = -1
    for i, line in enumerate(contents):
        user_key, private_key = line.strip().split(".")
        if sender_key == user_key and sender_private_key == private_key:
            sender_index = i
        elif receiver_key == user_key:
            receiver_index = i

    if sender_index == -1 or receiver_index == -1:
        print("Invalid data either: (sender key, sender priv key or receiver key)")
        return

    sender_user_key, sender_private_key = contents[sender_index].strip().split(".")
    receiver_user_key, receiver_private_key = contents[receiver_index].strip().split(".")

    sender_balance = int(sender_user_key.split("_")[1])
    receiver_balance = int(receiver_user_key.split("_")[1])

    if amount > sender_balance:
        print("Not enough balance")
        return

    sender_balance -= amount
    receiver_balance += amount

    new_sender_user_key = f"{sender_user_key.split('_')[0]}_{sender_balance}"
    new_receiver_user_key = f"{receiver_user_key.split('_')[0]}_{receiver_balance}"

    new_sender_key = new_sender_user_key + sender_private_key
    new_receiver_key = new_receiver_user_key + receiver_private_key

    contents[sender_index] = new_sender_key + "\n"
    contents[receiver_index] = new_receiver_key + "\n"

    with open("userdata.txt", "w") as file:
        file.writelines(contents)

    print("Transaction successful")

def mine(miner_key):
    difficulty = "00"
    nonce = 0
    
    with open("userdata.txt") as file:
        contents = file.read()
        if miner_key in contents:
            while True:
                current_time = int(time.time())
                message = str(nonce) + str(current_time)
                hash_result = hashlib.sha256(message.encode('utf-8')).hexdigest()
                if hash_result[:2] == "000":
                    print("Hash found: " + hash_result)
                    send("MASTERNODE_10000", "masternodeprivkey", miner_key, 1)
                    print("REWARD RECIVED")
                nonce += 1
        else:
            print("Invalid Miner key")