# Python Blockchain with Proof of Work

This project demonstrates how to build a basic blockchain in Python, featuring a Proof of Work (PoW) consensus mechanism to secure the chain. It generates wallets, adds transactions to blocks, mines those blocks to ensure validity, verifies the chain's integrity, and demonstrates how tampering is detected.

## Features

-   **Block & Blockchain Structure**: Implements fundamental block and chain architecture.
-   **SHA-256 Hashing**: Uses SHA-256 for cryptographic hashing to secure block data.
-   **Proof of Work (PoW)**: Requires computational work ("mining") to add new blocks, preventing malicious additions.
-   **Dynamic Difficulty**: The mining difficulty is randomly adjusted for each new block to simulate network changes.
-   **Wallet Generation**: Creates basic cryptographic wallets with private keys, public keys, and addresses.
-   **Chain Integrity Verification**: Includes a function to check if the blockchain has been tampered with.

## Requirements

-   **Block Structure**: Each block contains:
    -   `index`
    -   `timestamp`
    -   `data` (e.g., transactions)
    -   `previous_hash`
    -   `hash`
    -   `nonce` (a value found during mining)
-   **Mining Mechanism**: A function to perform Proof of Work by finding a hash that meets a specific difficulty target.
-   **Add Blocks**: A function to add new, mined blocks to the chain.
-   **Testing**: The `main.py` script adds sample data, prints the full blockchain, and demonstrates the security of the chain by attempting to tamper with it.

[//]: # (How to Run the Code)

## Prerequisites

-   Python 3.10 or higher
-   Install the required `cryptography` package.

You can install the package using pip:

```bash
pip install cryptography
```

How to Run
* Clone or download this repository.

* Open a terminal in the project directory.

Run the main script to see the blockchain in action:
```bash
python main.py
```