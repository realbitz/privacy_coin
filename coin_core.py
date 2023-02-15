import hashlib
import random
import os

def update_user_key(key, new_key, priv_key):
    key_path = "/user_data/user_keys/" + priv_key + ".txt"
    key_exist = os.path.exists(key_path)
    with open("/userdata/private_keys.txt") as keys:
        content = keys.read()
        if priv_key in content & key_exist == True:
            f = open(key_path, "w")
            f.write(new_key)
            f.close()
        else:
            print("Wrong pivate key or user key")

def create_user_identification(username, password):
    wallet_balance = 0
    combined_data = username + " " + password + " "
    random_num = hash = random.getrandbits(128)
    private_key = hashlib.sha256(random_num.encode()).hexdigest()
    user_key = hashlib.sha256(combined_data.encode()).hexdigest()

    key_path = "/user_data/user_keys/" + priv_key + ".txt"
    f = open(key_path, "w")
    f.write(user_key)
    f.close()
    
    print("YOUR USER KEY IS: ", user_key)
    print("YOUR PRIVATE KEY IS: ", private_key)