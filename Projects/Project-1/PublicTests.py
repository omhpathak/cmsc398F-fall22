from blockchain import Blockchain
import unittest

# DO NOT CHANGE


class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_block(self):
        blockchain = Blockchain()
        genesis = blockchain.chain[0]

        self.assertEqual(genesis, blockchain.get_previous_block())
        self.assertEqual(
            list(genesis.keys()), ['index', 'timestamp', 'nonce', 'previous_hash'])
        self.assertEqual(blockchain.get_chain_len(), 1)

        return

    def test_validity(self):
        blockchain = Blockchain()

        # adding 3 blocks
        self.mine_block(blockchain)
        self.mine_block(blockchain)
        self.mine_block(blockchain)

        self.assertTrue(blockchain.is_chain_valid(blockchain.chain))

        return

    def test_nonce(self):
        blockchain = Blockchain()

        # adding 3 blocks
        self.mine_block(blockchain)
        self.mine_block(blockchain)
        self.mine_block(blockchain)

        nonces = [1, 533, 45293, 21391]
        for i in range(blockchain.get_chain_len()):
            self.assertEqual(blockchain.chain[i]['nonce'], nonces[i])

        return

    def mine_block(self, blockchain):
        # getting info for new block from prev block
        previous_block = blockchain.get_previous_block()
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        previous_hash = blockchain.hash_block(previous_block)

        # creating new block
        block = blockchain.create_block(nonce, previous_hash)
        response = {'message': 'Congratulations, you just mined a block!',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'nonce': block['nonce'],
                    'previous_hash': block['previous_hash']}
        return response


if __name__ == "__main__":
    unittest.main()