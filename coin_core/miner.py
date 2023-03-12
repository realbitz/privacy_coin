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