from datetime import datetime
import hashlib
import json


class Blockchain:
    """
    The previous_hash is set to 0 initially
    The nonce is set to 1 

    """

    def __init__(self):
        self.chain = []
        self.create_block(nonce=1, previous_hash='0')

    # return the block created.
    def create_block(self, nonce, previous_hash):
        return

    # return the new nonce value.
    def proof_of_work(self, previous_nonce):
        return

    # returns True if the chain is valid, False otherwise
    def is_chain_valid(self, chain):
        return

    """
    Helper methods: 

    get_chain(self): returns the entire chain with its length
    get_chain_len(self): returns the length of the chain 
    get_previous_block(self): returns the previous block in the chain
    hash_block(self, block): returns the hash of the given block 
    
    """

    def get_chain(self):
        response = {'chain': self.chain, 'length': len(self.chain)}
        return response

    def get_chain_len(self):
        return len(self.chain)

    def get_previous_block(self):
        return self.chain[-1]

    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()