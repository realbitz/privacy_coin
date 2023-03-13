import hashlib
import random
import time

def miner():
    miner_key = input("Enter your wallet address: ")
    reward = 1

    with open("/blockchain_files/userdata.txt/") as m_keys:
        content = m_keys.read()

        if miner_key in content:
            while True:
                start_time = time.time()
                
                random_string = str(random.getrandbits(256))
                sha_hash = hashlib.sha256(random_string.encode()).hexdigest()
                if sha_hash[:4] == "0000":
                    end_time = time.time()
                    hashrate = 1 / (end_time - start_time)
                    
                    if hashrate >= 10**9:
                        hashrate_str = "{:.2f} GH/s".format(hashrate / 10**9)
                    elif hashrate >= 10**6:
                        hashrate_str = "{:.2f} MH/s".format(hashrate / 10**6)
                    elif hashrate >= 10**3:
                        hashrate_str = "{:.2f} KH/s".format(hashrate / 10**3)
                    else:
                        hashrate_str = "{:.2f} H/s".format(hashrate)
                        
                    print("[CPU]", " Mined Hash: ", sha_hash, " Hashrate: ", hashrate_str)
                    
                    with open("/blockchain_files/userdata.txt/") as keys:
                        content = keys.read()
                        addresses = content.strip().split('\n')
                        index = addresses.index(miner_key)
        
                        balance = int(addresses[index].split('_')[1])
                        new_balance = balance + reward
                        new_address = addresses[index].split('_')[0] + '_' + str(new_balance)
                        addresses[index] = new_address
        
                        content = '\n'.join(addresses)
        
                    with open("/blockchain_files/userdata.txt/", "w") as keys:
                        keys.write(content)
                        
                    miner_key = new_address
            
        else:
            print("Invalid miner key")


while True:
    try:
        miner()
    except KeyboardInterrupt:
        print('Mining stopped by user')
        break
    
miner()