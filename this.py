from hashlib import sha256
MAX_NONCE = 100000000000
import time
import threading

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
     prefix_str = '0'* difficulty
     for nonce in range(MAX_NONCE):
        
            text = str(blockNumber) + transactions + firstHash + str(nonce)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                lock.acquire()
                print(f"First hash:{firstHash}")
                firstHash = new_hash
                difficulty +=1
                print(f"Block Number: {blockNumber}")
                blockNumber +=1
               #  total_time = str((time.time() - start))
               #  print(f"end mining. Mining took: {total_time} seconds")
                print(f"1.Hash: {new_hash}")
               
                print(f"Successfully mined.\nNonce:{nonce}")
                lock.release()
                return new_hash
     raise BaseException(
         f"Couldn't find correct has after trying {MAX_NONCE} times")

def mine2():
     global difficulty
     global blockNumber
     global firstHash
     prefix_str = '0'* difficulty
     for nonce in range(MAX_NONCE):
     
            text = str(blockNumber) + transactions + firstHash + str(nonce)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                lock.acquire()
                print(f"First hash:{firstHash}")
                firstHash = new_hash
                difficulty +=1
                print(f"Block Number: {blockNumber}")
                blockNumber +=1
               #  total_time = str((time.time() - start))
               #  print(f"end mining. Mining took: {total_time} seconds")
                print(f"2.Hash: {new_hash}")
                
                print(f"Successfully mined.\nNonce:{nonce}")
                lock.release()
                return new_hash
     raise BaseException(
         f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__ == '__main__':
     
    print("start mining")
    for i in range(6):
        t1 = threading.Thread(target=mine)
        t2 = threading.Thread(target=mine2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

# from hashlib import sha256
# MAX_NONCE = 100000000000
# import time
# import threading

# def SHA256(text):
#     return sha256(text.encode("ascii")).hexdigest()

# def mine(block_number, transactions, previous_hash, prefix_zeros):
#     prefix_str = '0'*prefix_zeros
#     for nonce in range(MAX_NONCE):
#         text = str(block_number) + transactions + previous_hash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             print(f"Successfully mined.\n Nonce:{nonce}")
#             print(new_hash)
#             return new_hash
            
#     raise BaseException(
#         f"Couldn't find correct has after trying {MAX_NONCE} times")
# if __name__ == '__main__':
#     transactions = "Bize her yer Trabzon! Bolumun en yakisikli hocasi Ibrahim Hoca'dir"
#     difficulty = 1
#     firstHash = '0000000000000000000000000000000000000000000000000000000000000000'
#     # try changing this to higher number and you will see it will take more time for mining as difficulty increases
 
#     start = time.time()
#     print("start mining")
#     for i in range (6):
#         t1 = threading.Thread(target=mine(i,transactions,'0000000000000000000000000000000000000000000000000000000000000000', difficulty+i))
#         t1.start()
#         t2 = threading.Thread(target=mine(i+1,transactions,'0000000000000000000000000000000000000000000000000000000000000000', difficulty+(i+1)))
#         t2.start()