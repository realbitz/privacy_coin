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