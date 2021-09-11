from multiprocessing import Process
import random
import time
import concurrent.futures
import string
import math
import colorama
import os



def randDecrypter(func, password=None, address=None):
    if func == 1:
   
        print(address, "engaged ")
        
        guess = ''
        while guess != password:
            time.sleep(0.05)
            guess = random.choices(chars, k=len(password))
            #addressDict[address] = guess
            print(str(address) + ":\t" + str(guess) + " " )
            #print(f"{address}:  {addressDict[address]}\n" for address in addresses)
            if guess == list(password):
                print("your password is:", "".join(guess))
                #addressDict[address] = guess
                #finished[i] == True
                
                break
        return guess
'''
    elif func == 2:
        print("function 2 engaged")
        while True:
            count = 0
            print(finished)
            for i in addresses:
                if finished[i] == True:
                    count += 1
            if count == 4:
                print(addressDict, "is finished")
                break
            print(addressDict)

'''
def checker(var):
    print(var.submit())


if __name__ == "__main__":
    chars = string.ascii_lowercase
    chars = list(chars)
    passwords = [random.sample(chars, 4) for _ in range(4)]


    print("passwords:" + str(passwords))
    guess = ""

    count = 0
    label = "1234567890" + string.ascii_lowercase
    addresses = ["".join(random.sample(label, 6)) for _ in range(4)]
    nums = [1, 1, 1, 1]
    addressDict = {}
    finished = {}
    for i in addresses:
        addressDict[i] = ""
    for i in addresses:
        finished[i] = False


    with concurrent.futures.ThreadPoolExecutor() as executor:
        a = executor.submit(randDecrypter, nums[0], passwords[0], addresses[0])
        b = executor.submit(checker, a)

    
            
    
    
        