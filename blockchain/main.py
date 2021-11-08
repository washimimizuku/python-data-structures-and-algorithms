from hashlib import sha256
from time import time


class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.hash = self.get_hash()
        self.previous_hash = None
        self.nonce = 0

    def get_hash(self):
        new_hash = sha256()

        new_hash.update(str(self.previous_hash).encode('utf-8'))
        new_hash.update(str(self.timestamp).encode('utf-8'))
        new_hash.update(str(self.data).encode('utf-8'))
        new_hash.update(str(self.nonce).encode('utf'))

        return new_hash.hexdigest()

    def mine(self, difficulty):
        # Basically, it loops until our hash starts with
        # the string 0...000 with length of <difficulty>.
        while self.hash[:difficulty] != '0' * difficulty:
            # We increase our nonce so that we can get a whole different hash.
            self.nonce += 1
            # Update our new hash with the new nonce value.
            self.hash = self.get_hash()


class Blockchain:

    def __init__(self):
        # This property will contain all the blocks
        self.chain = [Block(str(int(time())))]
        self.difficulty = 1

    def get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, block):
        # Since we are adding a new block, previous_hash will be the hash of the old latest block
        block.previous_hash = self.get_last_block().hash
        # Since now previous_hash has a value, we must reset the block's hash
        block.hash = block.get_hash()
        block.mine(self.difficulty)

        self.chain.append(block)

    def is_valid(self):
        # Iterate over the chain, we need to set i to 1 because there is nothing before the
        # genesis block, so we start at the second block.
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check validation
            if (current_block.hash != current_block.get_hash() or previous_block.hash != current_block.previous_hash):
                return False

        return True
