import threading
import time
from hashlib import sha256
MAX_NONCE = 100000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


class myThread(threading.Thread):
    # def __init__(self, threadId, hashname, nounce):
    def __init__(self, block_number, transactions, previous_hash, prefix_zeros):
        threading.Thread.__init__(self)
        self.block_number = block_number
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.prefix_zeros = prefix_zeros

    def run(self):
        print("Starting: " + self.previous_hash + "\n")
        threadLock.acquire()
        # print_time(self.name, 1, self.count)
        print(self.transactions)
        threadLock.release()
        print("Exiting: " + self.previous_hash + "\n")


# class myThread2(threading.Thread):
#     def __init__(self, block_number, transactions, previous_hash, prefix_zeros):
#         threading.Thread.__init__(self)
#         self.block_number = block_number
#         self.transactions = transactions
#         self.previous_hash = previous_hash
#         self.prefix_zeros = prefix_zeros

#     def run(self):
#         print("Start" + " thread start" + self.previous_hash + "\n")
#         threadLock.acquire()
#         self.prefix_zeros += 1
#         print(self.prefix_zeros)
#         threadLock.release()
#         # print_time(self.name, 1, self.count)
#         print("Exiting: " + self.previous_hash + "\n")


# def print_time(name, delay, count):
#     while count:
#         time.sleep(delay)
#         print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
#         count -= 1

transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
difficulty = 1
firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
threadLock = threading.Lock()

thread1 = myThread(1, transactions, firstHash, difficulty)
thread2 = myThread2(1, transactions, firstHash, difficulty)

thread1.start()
thread2.start()
thread1.join()
thread2.join()


# def SHA256(text):
#     return sha256(text.encode("ascii")).hexdigest()


# def mineForThread1(block_number, transactions, previous_hash, prefix_zeros, lock):
#     prefix_str = '0'*prefix_zeros
#     difficulty = 1
#     for nonce in range(MAX_NONCE):
#         text = str(block_number) + transactions + previous_hash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             print(f"Successfully mined.\n Nonce:{nonce}")
#             lock.acquire()
#             firstHash = new_hash
#             difficulty += 1
#             lock.release()
#             print(firstHash)
#             return new_hash
#     raise BaseException(
#         f"Couldn't find correct has after trying {MAX_NONCE} times")


# def mineForThread2(block_number, transactions, previous_hash, prefix_zeros, lock):
#     prefix_str = '0'*prefix_zeros
#     difficulty = 1
#     for nonce in range(MAX_NONCE):
#         text = str(block_number) + transactions + previous_hash + str(nonce)
#         new_hash2 = SHA256(text)
#         if new_hash2.startswith(prefix_str):
#             print(f"Successfully mined.\n Nonce:{nonce}")
#             lock.acquire()
#             firstHash = new_hash2
#             difficulty += 1
#             lock.release()
#             print(firstHash)
#             return new_hash2
#     raise BaseException(
#         f"Couldn't find correct has after trying {MAX_NONCE} times")


# if __name__ == '__main__':
#     transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
#     difficulty = 1
#     firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
#     lock = threading.Lock()

#     start = time.time()
#     print("start mining")
#     t1 = threading.Thread(target=mineForThread1(
#         1, transactions, firstHash, difficulty, lock=lock), args=(lock,))
#     t2 = threading.Thread(target=mineForThread1(
#         1, transactions, firstHash, difficulty, lock=lock), args=(lock,))
#     t1.start()
#     t2.start()
# for i in range(4):
#     new_hash = mineForThread1(
#         difficulty, transactions, firstHash, difficulty)
#     firstHash = new_hash
#     if(new_hash):
#         difficulty += 1
#         total_time = str((time.time() - start))
#         print(f"end mining. Mining took: {total_time} seconds")
#         print(f"Hash: {new_hash}")

# for i in range(15):
#     t1 = threading.Thread(target=mine(
#         1, transactions, '0000000000000000000000000000000000000000000000000000000000000000', difficulty+1))
#     t1.start()
#     t2 = threading.Thread(target=mine(
#         2, transactions, '0000000000000000000000000000000000000000000000000000000000000000', difficulty+2))
#     t2.start()

# import time
# start = time.time()
# new_hash = mine(
#     1, transactions, '0000000000000000000000000000000000000000000000000000000000000000', difficulty)
# total_time = str((time.time() - start))


# from hashlib import sha256
# import time
# MAX_NONCE = 100000000000


# def SHA256(text):
#     return sha256(text.encode("ascii")).hexdigest()


# def mine(block_number, transactions, previous_hash, prefix_zeros):
#     prefix_str = '0'*prefix_zeros
#     for nonce in range(MAX_NONCE):
#         text = str(block_number) + transactions + previous_hash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
#             # print(new_hash)
#             return new_hash

#     raise BaseException(
#         f"Couldn't find correct has after trying {MAX_NONCE} times")


# if __name__ == '__main__':
#     transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
#     startBeginStr = '0000000000000000000000000000000000000000000000000000000000000000'
#     difficulty = 1  # try changing this to higher number and you will see it will take more time for mining as difficulty increases
#     start = time.time()
#     print("start mining")
#     for i in range(7):
#         print(startBeginStr)
#         new_hash = mine(
#             1, transactions, startBeginStr, difficulty)
#         print(new_hash)
#         if (len(new_hash) == 64):
#             startBeginStr = new_hash
#             difficulty += 1
#             print(str((time.time()-start)))
#             start = time.time()

#     total_time = str((time.time() - start))
#     print(f"end mining. Mining took: {total_time} seconds")
#     print(new_hash)
