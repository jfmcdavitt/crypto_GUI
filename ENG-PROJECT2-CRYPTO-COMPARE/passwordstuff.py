import random
import pyautogui
import string
import time
import math
#chars = "abcdefghijklmnopqrstuvwxyz"
chars = string.ascii_lowercase
chars = list(chars)
print(chars)
password = pyautogui.password("Enter a password"  )
guess = ""
start = time.time()
count = 0
def randDecrypter():
    while guess != password:
        guess = random.choices(chars, k=len(password))

        print("<==========" + str(guess) + "==========>")
        if guess == list(password):
            print("your password is:", "".join(guess))
            print("your total amount of attempts is:", count)
            end = time.time()
            return end
            break
        count += 1
end = randDecrypter()
result = math.trunc(end - start)
print("Total amount of minutes:", result / 60)