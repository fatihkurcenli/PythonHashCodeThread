import threading
import time
import threading
import time
from hashlib import sha256

MAX_NONCE = 100000000000
MAX_HALF_NONCE = 50000000

threadLock = threading.Lock()


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


class Example():
    def __init__(self, blockNumberGelen, transactionsGelen, firstHashGelen, difficultyGelen):
        self.blockNumber = blockNumberGelen
        self.transaction = transactionsGelen
        self.firstHash = firstHashGelen
        self.difficulty = difficultyGelen
        self.method_1()

    def method_1(self):

        def run(self):
            threading.Thread(target=function_a, args=(self,)).start()
            threading.Thread(target=function_b, args=(self,)).start()

        def function_a(self):
            for nonce in range(0, MAX_HALF_NONCE):
                prefix_str = '0' * self.difficulty
                text = str(self.blockNumber) + self.transaction + \
                    self.firstHash + str(nonce)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    threadLock.acquire()

                    print(f"1.Thread - Block Number: {self.blockNumber}")
                    self.firstHash = new_hash
                    self.difficulty += 1
                    self.blockNumber += 1
                    #  total_time = str((time.time() - start))
                    #  print(f"end mining. Mining took: {total_time} seconds")
                    print(f"1 Thread.Hash: {new_hash}")
                    print(f"Successfully mined.\nNonce:{nonce}")
                    print(f"-----------------------------------")

                    threadLock.release()
                    function_b(self)
                    break
            function_a(self)

        def function_b(self):
            for nonce in range(MAX_HALF_NONCE, MAX_NONCE):
                prefix_str = '0' * self.difficulty
                text = str(self.blockNumber) + self.transaction + \
                    self.firstHash + str(nonce)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    threadLock.acquire()

                    print(f"2.Thread - Block Number: {self.blockNumber}")
                    self.firstHash = new_hash
                    self.difficulty += 1
                    self.blockNumber += 1
                    #  total_time = str((time.time() - start))
                    #  print(f"end mining. Mining took: {total_time} seconds")
                    print(f"2 Thread.Hash: {new_hash}")
                    print(f"Successfully mined.\nNonce:{nonce}")
                    print(f"-----------------------------------")
                    threadLock.release()
                    function_a(self)
                    break
            function_b(self)

        run(self)


d = 1
b = 1
t = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
h = '0000000000000000000000000000000000000000000000000000000000000000'


Example(b, t, h, d)
