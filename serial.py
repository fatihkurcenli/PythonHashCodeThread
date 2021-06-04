import time
from hashlib import sha256
import threading
MAX_NONCE = 100000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Block Number: {blockNumber}")
            print(f"Successfully mined.\nNonce:{nonce}")
            return new_hash
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == 'main':
    transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
    blockNumber = 1
    difficulty = 1
    firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
    # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    start = time.time()
    print("start mining")
    for i in range(6):
        ##print(f"firsthash: {firstHash}")
        new_hash = mine(1, transactions, firstHash, difficulty)
        firstHash = new_hash
        if(new_hash):
            difficulty += 1
            blockNumber += 1
            total_time = str((time.time() - start))
            print(f"end mining. Mining took: {total_time} seconds")
            print(f"Hash: {new_hash}")
