def hash_function(data):
    return data + '*'

class Block:
    def __init__(self, data, hash, previous_hash):
        self.data = data
        self.hash = hash
        self.previous_hash = previous_hash

class Blockchain:
    def __init__(self):
        genesis = Block("genesis_data", "genesis_hash", "genesis_previous_hash")
        self.chain = [genesis]

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        hash = hash_function(data + previous_hash)
        block = Block(data, hash, previous_hash)
        self.chain.append(block)

our_blockchain = Blockchain()
our_blockchain.add_block("one")
our_blockchain.add_block("two")
our_blockchain.add_block("three")
our_blockchain.add_block("four")
our_blockchain.add_block("five")

for block in our_blockchain.chain:
    print(block.__dict__)
