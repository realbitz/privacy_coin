def create_cabbage(sender, reciver, amount):
    cabbage_data = sender, " sent ", amount " to ", reciver
    hashlib.sha256(cabbage_data.encode()).hexdigest()

    print("Cabbage Data: ", cabbage_data)

    target = '0' * zeros + '1' * (64 - zeros)
    nonce = 0
    while True:
        data = f"Cabbage network is the best{int(time.time())}{nonce}"
        result = hashlib.sha256(data.encode()).hexdigest()
        if result[:zeros] == target[:zeros]:
            return result
        nonce += 1
    
    while current_leaf != difficulty:
        current_leaf += 1
        print("Leaf; ", current_leaf, " hash; ", calculate_hash(current_leaf))