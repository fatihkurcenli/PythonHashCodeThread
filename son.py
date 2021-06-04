import logging
import threading
import time
from hashlib import sha256
MAX_NONCE = 100000000000
MAX_HALF_NONCE = 50000000
number = 0
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


def consumer(cond):
    global difficulty
    global blockNumber
    global firstHash
    global buldum
    prefix_str = '0' * difficulty
    time.sleep(2)
    buldum = False
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        # cond.wait()
        logging.debug('Resource is available to consumer')
        while(buldum == False):
            for nonce in range(0, MAX_HALF_NONCE):
                print(f"1- Thread Nonce Değeri: {nonce}")
                text = str(blockNumber) + transactions + firstHash + str(nonce)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    lock.acquire()
                    firstHash = new_hash
                    difficulty += 1
                    print(f"Block Number: {blockNumber}")
                    blockNumber += 1
                    #  total_time = str((time.time() - start))
                    #  print(f"end mining. Mining took: {total_time} seconds")
                    print(f"1 Thread1.Hash: {new_hash}")
                    print(f"Successfully mined.\nNonce:{nonce}")
                    lock.release()
                    buldum = True
                    cond.notifyAll()
                    producer(cond)
                    consumer(cond)

                    break


def producer(cond):
    global difficulty
    global blockNumber
    global firstHash
    global buldum
    prefix_str = '0' * difficulty
    time.sleep(2)
    buldum = False
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        while(buldum == False):
            for nonce in range(MAX_HALF_NONCE, MAX_NONCE):
                print(f"2- Thread Nonce Değeri: {nonce}")
                text = str(blockNumber) + transactions + firstHash + str(nonce)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    lock.acquire()
                    firstHash = new_hash
                    difficulty += 1
                    print(f"Block Number: {blockNumber}")
                    blockNumber += 1
                    #  total_time = str((time.time() - start))
                    #  print(f"end mining. Mining took: {total_time} seconds")
                    print(f"2 Thread1.Hash: {new_hash}")
                    print(f"Successfully mined.\nNonce:{nonce}")
                    lock.release()
                    buldum = True
                    cond.notifyAll()
                    consumer(cond)
                    producer(cond)

                    break


condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
# c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))
p.start()
time.sleep(2)
c1.start()
time.sleep(2)
# c2.start()
