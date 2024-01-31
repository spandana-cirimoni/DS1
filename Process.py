import threading
import queue
import random
from threading import Thread

class Process(threading.Thread):
    def __init__(self,ID,counter,message):
        Thread.__init__(self)
        self.ID = ID
        self.counter = counter
        self.message = message

    def run(self):
        while True:
            print("{} is running successfully".format(self.ID))
            random_generated = {'p1', 'p2', 'p3', 'p4'}
            selected_process = random.choice(tuple(random_generated))
            if(selected_process==self.ID):
                self.counter+=1
                print("Internal Event: ",self.ID," Timestamp:",self.counter,"\n")
            elif(self.message[self.ID].empty()):
                self.message[self.ID].put("Hello World")
                self.counter+=1
                print("{}".format(self.ID),"sent message to {}.".format(selected_process)," Timestamp:",self.counter,"\n")
            else:
                self.message[self.ID].get()
                self.counter+=1
                print("{}".format(self.ID),"received a message from {}.".format(selected_process)," Timestamp:",self.counter,"\n")