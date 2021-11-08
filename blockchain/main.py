from hashlib import sha256
from time import time


class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        # Data can contain any information, for example, transactions.
        self.data = [] if data is None else data

    def get_hash(self):
        current_hash = sha256()

        current_hash.update(str(self.previous_hash).encode('utf-8'))
        current_hash.update(str(self.timestamp).encode('utf-8'))
        current_hash.update(str(self.data).encode('utf-8'))

        return current_hash.hexdigest()
