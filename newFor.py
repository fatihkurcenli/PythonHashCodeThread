import threading
import time
from hashlib import sha256
MAX_NONCE = 100000000000
MAX_HALF_NONCE = 50000000
number = 0


transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
blockNumber = 1
difficulty = 1
firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
buldum = False
lock = threading.Lock()


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine():
    global difficulty
    global blockNumber
    global firstHash
    global buldum
    prefix_str = '0' * difficulty
    time.sleep(2)
    buldum = False
    # print(f"Thread 1 fonksiyonu uzunluk değeri "+str(len(prefix_str)))
    while(buldum == False):
        for nonce in range(0, MAX_HALF_NONCE):
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
                mine2()
                break
    mine()


def mine2():
    global difficulty
    global blockNumber
    global firstHash
    global buldum
    prefix_str = '0' * difficulty
    time.sleep(2)
    buldum = False
    # print(f"Thread 1 fonksiyonu uzunluk değeri "+str(len(prefix_str)))
    while(buldum == False):
        for nonce in range(MAX_HALF_NONCE, MAX_NONCE):
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
                mine()
                lock.release()
                buldum = True
                mine()
                break
    mine2()


def mineFirst():
    global difficulty
    global blockNumber
    global firstHash
    global buldum
    prefix_str = '0' * difficulty
    buldum = True
    for nonce in range(MAX_NONCE):
        text = str(blockNumber) + transactions + firstHash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            firstHash = new_hash
            print(f"First init Project: {blockNumber}")
            print(f"Successfully mined.\nNonce:{nonce}")
            return new_hash
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == 'main':
    # mineFirst()
    t1 = threading.Thread(target=mine)
    t2 = threading.Thread(target=mine2)

# t3 = threading.Thread(target=mine3)
# t4 = threading.Thread(target=mine4)
# t5 = threading.Thread(target=mine5)
    t1.start()
    t2.start()

# def mine3():
#     global difficulty
#     global blockNumber
#     global firstHash
#     prefix_str = '0' * difficulty
#     # print(f"Thread 1 fonksiyonu uzunluk değeri "+str(len(prefix_str)))
#     for nonce in range(MAX_NONCE):
#         text = str(blockNumber) + transactions + firstHash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             if(firstHash.startswith(prefix_str) != new_hash.startswith(prefix_str)):
#                 lock.acquire()
#                 firstHash = new_hash
#                 difficulty += 1
#                 print(f"Block Number: {blockNumber}")
#                 blockNumber += 1
#                 #  total_time = str((time.time() - start))
#                 #  print(f"end mining. Mining took: {total_time} seconds")
#                 print(f"3 Thread1.Hash: {new_hash}")
#                 print(f"Successfully mined.\nNonce:{nonce}")
#                 lock.release()
#                 print(f"{difficulty}")
#                 mine3()
#                 break
#             else:
#                 break


# def mine4():
#     global difficulty
#     global blockNumber
#     global firstHash
#     prefix_str = '0' * difficulty
#     # print(f"Thread 1 fonksiyonu uzunluk değeri "+str(len(prefix_str)))
#     for nonce in range(MAX_NONCE):
#         text = str(blockNumber) + transactions + firstHash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             if(firstHash.startswith(prefix_str) != new_hash.startswith(prefix_str)):
#                 lock.acquire()
#                 firstHash = new_hash
#                 difficulty += 1
#                 print(f"Block Number: {blockNumber}")
#                 blockNumber += 1
#                 #  total_time = str((time.time() - start))
#                 #  print(f"end mining. Mining took: {total_time} seconds")
#                 print(f"4 Thread1.Hash: {new_hash}")
#                 print(f"Successfully mined.\nNonce:{nonce}")
#                 lock.release()
#                 print(f"{difficulty}")
#                 mine4()
#                 break
#             else:
#                 break

# def mine5():
#     global difficulty
#     global blockNumber
#     global firstHash
#     prefix_str = '0' * difficulty
#     # print(f"Thread 1 fonksiyonu uzunluk değeri "+str(len(prefix_str)))
#     for nonce in range(MAX_NONCE):
#         text = str(blockNumber) + transactions + firstHash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             if(firstHash.startswith(prefix_str) != new_hash.startswith(prefix_str)):
#                 lock.acquire()
#                 firstHash = new_hash
#                 difficulty += 1
#                 print(f"Block Number: {blockNumber}")
#                 blockNumber += 1
#                 #  total_time = str((time.time() - start))
#                 #  print(f"end mining. Mining took: {total_time} seconds")
#                 print(f"5 Thread1.Hash: {new_hash}")
#                 print(f"Successfully mined.\nNonce:{nonce}")
#                 lock.release()
#                 print(f"{difficulty}")
#                 mine5()
#                 break
#             else:
#                 break


t1 = threading.Thread(target=mine)
t2 = threading.Thread(target=mine2)
# t3 = threading.Thread(target=mine3)
# t4 = threading.Thread(target=mine4)
# t5 = threading.Thread(target=mine5)
t1.start()
t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
