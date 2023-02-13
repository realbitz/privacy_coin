import hashlib
import datetime

class Cabbage:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha = hashlib.sha256(data.encode()).hexdigest()
        return sha

class Blockchain:
    difficulty = 4

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Cabbage("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Cabbage(data, previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print()

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Transaction 1")
    blockchain.add_block("Transaction 2")
    blockchain.print_chain()
