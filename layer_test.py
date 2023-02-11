import hashlib

def generate_hash_with_zeros(zeros):
    target = '0' * zeros + '1' * (64 - zeros)
    nonce = 0
    while True:
        data = f"asdasdasdasda{nonce}"
        result = hashlib.sha256(data.encode()).hexdigest()
        if result[:zeros] == target[:zeros]:
            return result
            break
        nonce += 1


generate_hash_with_zeros(2)

def create_cabbage():
    difficulty = input("Enter peeling difficultu: (6-7 recommended)")
    current_leaf = 0

    while current_leaf != difficulty:
        current_leaf+=1
        print("Leaf; ", current_leaf, " hash; ", generate_hash_with_zeros(current_leaf))


create_cabbage()