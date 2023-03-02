import hashlib
import time

def create_wallet(username, password):
    wallet_balance = "0"
    wallet_address_prefix = hashlib.sha256((username + password).encode()).hexdigest()
    wallet_address = wallet_address_prefix + "_" + wallet_balance

    print("Your wallet address: ", wallet_address)

    f = open("userdata.txt", "a")
    f.write(wallet_address + "\n")
    f.close()

def send(sender_address, receiver_address, amount):
    with open("userdata.txt") as keys:
        content = keys.read()
        if sender_address and receiver_address in content:
            sender_balance = int(sender_address.split("_")[1])
            if amount <= sender_balance:

                sender_balance -= amount
                receiver_balance = int(receiver_address.split("_")[1])
                receiver_balance += amount

                sender_address = sender_address.split("_")[0] + "_" + str(sender_balance)
                receiver_address = receiver_address.split("_")[0] + "_" + str(receiver_balance)

                print("Transaction successful.")

                content = content.replace(sender_address.split("_")[0] + "_" + str(sender_balance + amount), sender_address)
                content = content.replace(receiver_address.split("_")[0] + "_" + str(receiver_balance - amount), receiver_address)

                with open("userdata.txt", "w") as keys:
                    keys.write(content)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid wallet addresses.")

def mine(miner_key):
    target_prefix = '0' * 5
    reward = 1
    while True:
        message = str(time.time()).encode()
        sha256_hash = hashlib.sha256(message).hexdigest()

        if sha256_hash.startswith(target_prefix):
            print("Hash: " + sha256_hash)

            with open("userdata.txt") as keys:
                content = keys.read()
                addresses = content.strip().split('\n')
                index = addresses.index(miner_key)

                balance = int(addresses[index].split('_')[1])
                new_balance = balance + reward
                new_address = addresses[index].split('_')[0] + '_' + str(new_balance)
                addresses[index] = new_address

                content = '\n'.join(addresses)

            with open("userdata.txt", "w") as keys:
                keys.write(content)
            print("REWARD GRANTED:", reward)

            miner_key = new_address

            

mine("22d324416d6c2513dca5b6e69d50eac29777a11f9be42d877704741474756ffc_0")