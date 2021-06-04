import logging
import threading
import time
import sys
from hashlib import sha256
MAX_NONCE = 100000000000
MAX_HALF_NONCE = 50000000

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
blockNumber = 1
difficulty = 1
firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
buldum = False
lock = threading.Lock()


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def consumer(gelenCodeConsumer):

    sys.setrecursionlimit(1500)
    global difficulty
    global blockNumber
    prefix_str = '0' * difficulty
    for nonce in range(0, MAX_HALF_NONCE):
        # print(f"1- Thread Nonce Değeri: {nonce}")
        text = str(blockNumber) + transactions + gelenCodeConsumer + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):

            lock.acquire()
            difficulty += 1
            print(f"Block Number: {blockNumber}")
            blockNumber += 1
            #  total_time = str((time.time() - start))
            #  print(f"end mining. Mining took: {total_time} seconds")
            print(f"1 Thread1.Hash: {new_hash}")
            print(f"Successfully mined.\nNonce:{nonce}")
            lock.release()
            producer(new_hash)
            consumer(new_hash)
            break


def producer(gelenCodeProducer):

    sys.setrecursionlimit(1500)
    global difficulty
    global blockNumber
    prefix_str = '0' * difficulty
    for nonce in range(MAX_HALF_NONCE, MAX_NONCE):
        # print(f"2- Thread Nonce Değeri: {nonce}")
        text = str(blockNumber) + transactions + gelenCodeProducer + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            lock.acquire()
            difficulty += 1
            print(f"Block Number: {blockNumber}")
            blockNumber += 1
            #  total_time = str((time.time() - start))
            #  print(f"end mining. Mining took: {total_time} seconds")
            print(f"2 Thread1.Hash: {new_hash}")
            print(f"Successfully mined.\nNonce:{nonce}")
            lock.release()
            producer(new_hash)
            consumer(new_hash)
            break


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Block Number: {blockNumber}")
            print(f"Successfully mined.\nNonce:{nonce}")
            print(f"Successfully hashCode.\nHashCode:{new_hash}")
            return new_hash
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


new_hash = mine(1, transactions, firstHash, difficulty)
firstHash = new_hash
difficulty += 1
blockNumber += 1

time.sleep(5)


#condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(firstHash,))
# c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(firstHash,))

time.sleep(2)
c1.start()
time.sleep(2)
p.start()
# c2.start()
