from tkinter import *
import time
import random
import string
from PIL import Image, ImageTk
import os
import threading
import math
from multiprocessing import Process
import concurrent.futures
alphabet = string.ascii_letters


root = Tk()
root.geometry("500x400")
root.title("Decryption Visualizer")
options = [2, 3, 4, 5, 6, 7, 8]

class cryptoGUI:
    
    def __init__(self, master):
        
        self.master = master
        self.frame = Frame(self.master, height = "500", width = "400")
        self.frame.pack()

        self.labelvar1 = StringVar(master)
        self.labelvar1.set("--[****]--")
        self.labelvar2 = StringVar(master)
        self.labelvar2.set("--[****]--")
        self.label1 = Label(self.frame, text= self.labelvar1.get(), fg = "red")
        self.label1.grid(row=0, column=0)
        self.victory1 = False
        self.victory2 = False

        self.tkVar = StringVar(master)
        self.tkVar.set(options[2])
        self.label2 = Label(self.frame, text= self.labelvar2.get(), fg= "blue")
        self.label2.grid(row=0, column=1)
        self.length = 4
        self.menu = OptionMenu(self.frame, self.tkVar, *options)
        self.menu.grid(row=1 , column=1)

        self.logo = Image.open("decrypt_logo.png")
        self.logo = self.logo.resize((50,50))
        #self.tkLogo = ImageTk.PhotoImage(self.logo)
        #self.imageLabel = Label(self.frame, image = self.tkLogo)
        #self.imageLabel.image = self.tkLogo
        #self.imageLabel.grid(row = 2, column = 3)
        #self.button = Button(self.frame, text= "Overused Joke?", bg = "blue", command = self.shutdown)
        #self.button.grid(row= 1, column = 2)

        self.button2 = Button(master, text= "let's go eh", bg = "green", command = self.changeUp)
        self.button2.place(y="0", x="0")

        self.randomVar = StringVar(master)
        self.randomVar.set("".join(random.sample(alphabet, 4)))
        
        self.randomLabel = Label(self.frame, text = "--[" + str(self.randomVar.get()) + "]--" , fg = "purple")
        self.randomLabel.grid(row=1, column= 4)
        self.randomButton = Button(self.frame, text= "Randomize the code?", bg = "blue", command = self.changeCode)
        self.randomButton.grid(row=1, column=5)
        

    def changeUp(self):
        with concurrent.futures.ProcessPoolExecutor() as p:
            p.submit(randDecrypter(self))
            p.submit(randDecrypter2(self))
            
        '''
        while self.victory1 != True or self.victory2 != True:
            #time.sleep(0.05)
            self.labelvar1.set("".join(random.sample(alphabet, self.length)))
            self.labelvar2.set("".join(random.sample(alphabet, self.length)))
            self.label1.configure(text = "--[" + str(self.labelvar1.get()) + "]--")
            self.label2.configure(text = "--[" + str(self.labelvar2.get()) + "]--")
            self.frame.update_idletasks()
            if str(self.labelvar1.get()) == str(self.randomVar.get()) or str(self.labelvar2.get()) == str(self.randomVar.get()):
                print("Victory")
                self.victory1 = True
                break
                #TODO: Problem is that the loop isn't catching the win condition
                '''
            
    



    def changeCode(self):
        num = int(self.tkVar.get())
        if self.length != num:
            self.length = num
        
        self.randomVar.set("".join(random.sample(alphabet, num)))
        self.randomLabel.configure(text= "--[" + str(self.randomVar.get()) + "]--")
        self.frame.update_idletasks()



    def shutdown(self):
        self.master.destroy()
def randDecrypter(self):
        
        self.guess = ""
        start = time.time()
        count = 0
        while self.labelvar1.get() != self.randomVar.get():
            self.labelvar1.set("".join(random.sample(alphabet, self.length)))
            self.label1.configure(text = "--[" + str(self.labelvar1.get() ) + "]--")
            self.frame.update_idletasks()
            if str(self.labelvar1.get()) == str(self.randomVar.get()):
                print("randDecrypter")
                self.victory1 = True 
                break
            if self.victory2:
                break
            time.sleep(0.05)

def randDecrypter2(self):
        self.guess = ""
        start = time.time()
        count = 0
        while self.labelvar2.get() != self.randomVar.get():
            self.labelvar2.set("".join(random.sample(alphabet, self.length)))
            self.label2.configure(text = "--[" + str(self.labelvar2.get() ) + "]--")
            self.frame.update_idletasks()
            if str(self.labelvar2.get()) == str(self.randomVar.get()):
                print("randDecrypter2")
                self.victory2 = True 
                break
            if self.victory1:
                break
            time.sleep(0.05)

        '''
            print("<==========" + str(guess) + "==========>")
            if guess == list(password):
                print("your password is:", "".join(guess))
                print("your total amount of attempts is:", count)
                end = time.time()
                break
            count += 1 '''


if __name__ == "__main__":
    if os.getcwd != r"C:\Users\thega\OneDrive\WF_OneDrive\ENG-PROJECT2-CRYPTO-COMPARE":
        os.chdir(r"C:\Users\thega\OneDrive\WF_OneDrive\ENG-PROJECT2-CRYPTO-COMPARE")
    gooey = cryptoGUI(root)
    root.mainloop()