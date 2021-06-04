import threading
import time
from hashlib import sha256
MAX_NONCE = 100000000000

lock = threading.Lock()
transactionsForGlobal = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
difficulty = 1
hashCode = '0000000000000000000000000000000000000000000000000000000000000000'
blockNumber = 1


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mineForThread1():
    global transactionsForGlobal
    global difficulty
    global hashCode
    global blockNumber
    prefix_str = '0'*difficulty
    print(f"2-Thread prefix değeri -->{prefix_str}")
    # startTimeThread1 = time.time()
    for nonce in range(MAX_NONCE):
        text = str(blockNumber) + transactionsForGlobal + hashCode + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            # print(
            #     f"1'inci Thread Buldu -- !!Successfully mined.\n Nonce:{nonce}")
            lock.acquire()
            hashCode = new_hash
            difficulty += 1
            print(
                f"1'inci Thread Buldu -- !! Bulununa hash Code {hashCode}")
            # print(f"birinci dificulty -- > "+str(difficulty))
            blockNumber += 1
            #total_time_thread1 = str((time.time()-startTimeThread1))
            # print(total_time_thread1)
            lock.release()
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


def mineForThread2():
    global transactionsForGlobal
    global difficulty
    global hashCode
    global blockNumber
    prefix_str = '0'*(difficulty+1)
    print(f"2-Thread prefix değeri -->{prefix_str}")
    # startTimeThread1 = time.time()
    for nonce in range(MAX_NONCE):
        text = str(blockNumber) + transactionsForGlobal + hashCode + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            # print(
            #     f"1'inci Thread Buldu -- !!Successfully mined.\n Nonce:{nonce}")
            lock.acquire()
            hashCode = new_hash
            difficulty += 1
            print(
                f"2'inci Thread Buldu -- !! Bulununa hash Code {hashCode}")
            # print(f"birinci dificulty -- > "+str(difficulty))
            blockNumber += 1

            #total_time_thread1 = str((time.time()-startTimeThread1))
            # print(total_time_thread1)
            lock.release()

    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


t1 = threading.Thread(target=mineForThread1)
t2 = threading.Thread(target=mineForThread2)
t1.start()
t2.start()
t1.join()
t2.join()
