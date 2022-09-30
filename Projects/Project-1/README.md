# Blockchain Implementation

## Getting Started

### Setting Up

- Install python if you don't have it already

- All the import statements for the libraries that are needed are already in the codebase

- Start coding up your own blockchain!

## Description

A simple implementation of your own Blockchain!

Methods to Implement:

```
def create_block(self, nonce, previous_hash)
```

A block consists of:
'index' -> int,
'timestamp' -> str,
'nonce' -> int,
'previous_hash' -> int

create_block() creates a new block, appends it to the chain list, and returns the block.

The timestamp with be created with a call to:

```
datetime.now()
```

Keep in mind that this returns a type of 'datetime.datetime' while we want a string.

```
def proof_of_work(self, previous_nonce)
```

Our proof-of-work method needs to repeatedly increment a nonce until we have a hash operation with 4 leading 0s (Ex. 0000c3af42fc31...).

Once found, return the winning nonce.

The nonce should start at 1 everytime we do the proof for a block and increment from there.

The hash operation is defined as:

```
hash_operation = hashlib.sha256(str(new_nonce ** 2 - previous_nonce** 2).encode()).hexdigest()
```

```
def is_chain_valid(self, chain)
```

Our is_chain_valid function checks for the following:

- Check if each 'previous_hash' value is correct using one of the helper methods (hint: hash_block)
  - If the previous_hash is valid, then they should be equal
- check if each block's nonce is correct or not based on our proof_of_work method (hint: check if the hash operation maintains validity).
- Return True if the chain is valid, else False

Keep in mind: you are comparing two blocks at a time... be wary of how you loop so that you don't get IndexOutOfBounds Errors



#### Note: 
- DO NOT HARDCODE THE NONCES OR ANY OTHER VALUES 
- YOU WILL RECEIVE A 0 ON THE PROJECT IF YOU DO SO

### Submit:
- Submit a file of your code to ELMS named with with the following format: LastName-FirstName-p1.py
