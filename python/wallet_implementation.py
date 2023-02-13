import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.wallets = {}

        # create genesis block
        self.add_block(previous_hash='')

    def add_block(self, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
        }
        block['hash'] = self.hash(block)
        self.chain.append(block)
        self.pending_transactions = []

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

    def create_wallet(self, wallet_id):
        self.wallets[wallet_id] = 0

    def get_wallet_balance(self, wallet_id):
        if wallet_id not in self.wallets:
            return None
        balance = self.wallets[wallet_id]
        for block in self.chain:
            for tx in block['transactions']:
                if tx['sender'] == wallet_id:
                    balance -= tx['amount']
                if tx['recipient'] == wallet_id:
                    balance += tx['amount']
        return balance

    def send(self, sender, recipient, amount):
        if sender not in self.wallets:
            return False
        if self.wallets[sender] < amount:
            return False
        self.add_transaction(sender, recipient, amount)
        self.wallets[sender] -= amount
        self.wallets[recipient] += amount
        return True

# create blockchain and wallets
bc = Blockchain()
bc.create_wallet('Alice')
bc.create_wallet('Bob')

# check initial balances
print('Alice balance:', bc.get_wallet_balance('Alice'))
print('Bob balance:', bc.get_wallet_balance('Bob'))

# transfer funds from Alice to Bob
bc.send('Alice', 'Bob', 10)

# check new balances
print('Alice balance:', bc.get_wallet_balance('Alice'))
print('Bob balance:', bc.get_wallet_balance('Bob'))