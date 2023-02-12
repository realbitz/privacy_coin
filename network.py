from datetime import datetime
import time
import sys
import hashlib

cabbages = ["0"]
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

def calculate_hash(zeros):
    target = '0' * zeros + '1' * (64 - zeros)
    nonce = 0
    while True:
        data = f"Cabbage network is the best{int(time.time())}{nonce}"
        result = hashlib.sha256(data.encode()).hexdigest()
        if result[:zeros] == target[:zeros]:
            return result
        nonce += 1

def create_cabbage(data):
    difficulty = 4
    cabbage_number = 0
    current_leaf = 0
    cabbage_number+=1
    cabbage_id = data + " " + date_time

    cabbages.append(cabbage_id)
    prev_cabbage = cabbages[-2]

    print("Cabbage ID: ", cabbage_id)
    print("Cabbage Number: ", cabbage_number)
    print("Timestamp: ", datetime.now())
    while current_leaf != difficulty:
        current_leaf+=1
        print("Leaf; ", current_leaf, " hash; ", calculate_hash(current_leaf))
    print("Cabbage Completed")
    print("\n")

    if cabbage_id == cabbages[-1] and prev_cabbage == cabbages[-2]:
        print("Chain is valid \n")
    else:
        print("Chain is not valid \n")
        sys.exit()

def create_genisis_block():
    create_cabbage("Genisis Block")

def run_network():
    create_genisis_block()
    create_cabbage("Test transaction")
    
run_network()