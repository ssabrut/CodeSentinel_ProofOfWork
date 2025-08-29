import random
import hashlib
import time
from typing import Any


class Block:
    def __init__(self, index: int, data: Any, previous_hash: str) -> None:
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        encoded_block_string = block_string.encode()
        sha256 = hashlib.sha256()
        sha256.update(encoded_block_string)
        return sha256.hexdigest()

    def mine(self) -> None:
        difficulty = random.randint(3, 5)
        target = "0" * difficulty

        start_time = time.perf_counter()
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Block {self.index} Mined! Time Taken: {elapsed_time:.2f} s, Difficulty: {difficulty} Nonce: {self.nonce} - Hash: {self.hash}")

    def __repr__(self) -> str:
        return f"""Block(Index: {self.index}, Timestamp: {self.timestamp}, Data: {self.data}, Hash: {self.hash}, Nonce: {self.nonce}, Previous Hash: {self.previous_hash})"""


if __name__ == "__main__":
    difficulty = 5
    genesis_block = Block(
        index=0,
        data="Genesis Block",
        previous_hash="0000000000000000000000000000000000000000000000000000000000000000",
    )

    genesis_block.mine()
    print(genesis_block)
