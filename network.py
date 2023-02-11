from datetime import datetime
import sys
import hashlib

hashes = ["0"]
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

def return_hashes():
    return hashes

def add_block(data):
    transaction_number = 0
    
    transaction_number+=1
    transaction_data = data + date_time
    hash_object = hashlib.sha256(transaction_data.encode())
    block_hash = hash_object.hexdigest()
    hashes.append(block_hash)
    prev_hash = hashes[-2]

    print("Transaction ID: ", transaction_data)
    print("Transaction Number: ", transaction_number)
    print("Timestamp: ", datetime.now())
    print("Hash: ", block_hash)
    print("Previous Hash: ", prev_hash)
    print("\n")
    
    if block_hash == hashes[-1] and prev_hash == hashes[-2]:
        print("Chain is valid \n")
    else:
        print("Chain is not valid \n")
        sys.exit()

def create_genisis_block():
    add_block("Genisis Block")

def run_network():
    create_genisis_block()
    add_block("Harl to max 1")
    
run_network()