import hashlib
from time import time
import json


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transaction =[]

    def new_block(self,proof, previous_hash=None):
        # creates new block
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index':len(self.chain) +1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        #reset the current list of transactions
        self.current_transaction = []
        self.chain.append(block)
        return block

        
    def new_transaction(self,sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transaction.append[{
            'sender': sender,
            'reciepient': recipient,
            'amount': amount
        }]

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass