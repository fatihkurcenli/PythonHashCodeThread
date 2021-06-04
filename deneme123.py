import threading
import time
from hashlib import sha256
MAX_NONCE = 100000000000

transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
blockNumber = 1
difficulty = 1
firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
lock = threading.Lock()


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine():
    global difficulty
    global blockNumber
    global firstHash
    prefix_str = '0' * difficulty
    for nonce in range(MAX_NONCE):

        text = str(blockNumber) + transactions + firstHash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            lock.acquire()
            print(f"First hash:{firstHash}")
            firstHash = new_hash
            difficulty += 1
            print(f"Block Number: {blockNumber}")
            blockNumber += 1
           #  total_time = str((time.time() - start))
           #  print(f"end mining. Mining took: {total_time} seconds")
            print(f"1.Hash: {new_hash}")

            print(f"Successfully mined.\nNonce:{nonce}")
            lock.release()
            mine()
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


def mine2():
    global difficulty
    global blockNumber
    global firstHash
    prefix_str = '0' * difficulty
    for nonce in range(MAX_NONCE):

        text = str(blockNumber) + transactions + firstHash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            lock.acquire()
            print(f"First hash:{firstHash}")
            firstHash = new_hash
            difficulty += 1
            print(f"Block Number: {blockNumber}")
            blockNumber += 1
           #  total_time = str((time.time() - start))
           #  print(f"end mining. Mining took: {total_time} seconds")
            print(f"2.Hash: {new_hash}")

            print(f"Successfully mined.\nNonce:{nonce}")
            lock.release()
            mine2()
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


def mine3():
    global difficulty
    global blockNumber
    global firstHash
    prefix_str = '0' * difficulty
    for nonce in range(MAX_NONCE):

        text = str(blockNumber) + transactions + firstHash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            lock.acquire()
            print(f"First hash:{firstHash}")
            firstHash = new_hash
            difficulty += 1
            print(f"Block Number: {blockNumber}")
            blockNumber += 1
           #  total_time = str((time.time() - start))
           #  print(f"end mining. Mining took: {total_time} seconds")
            print(f"3.Hash: {new_hash}")

            print(f"Successfully mined.\nNonce:{nonce}")
            lock.release()
            mine3()
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


def mine4():
    global difficulty
    global blockNumber
    global firstHash
    prefix_str = '0' * difficulty
    for nonce in range(MAX_NONCE):

        text = str(blockNumber) + transactions + firstHash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            lock.acquire()
            print(f"First hash:{firstHash}")
            firstHash = new_hash
            difficulty += 1
            print(f"Block Number: {blockNumber}")
            blockNumber += 1
           #  total_time = str((time.time() - start))
           #  print(f"end mining. Mining took: {total_time} seconds")
            print(f"4.Hash: {new_hash}")

            print(f"Successfully mined.\nNonce:{nonce}")
            lock.release()
            mine4()
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == '__main__':

    print("start mining")

    t1 = threading.Thread(target=mine)
    t2 = threading.Thread(target=mine2)
    t3 = threading.Thread(target=mine3)
    t4 = threading.Thread(target=mine4)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
