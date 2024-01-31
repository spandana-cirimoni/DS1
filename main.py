import queue
from threading import Thread
from Process import Process

if __name__ == "__main__":
    message = {
     "p1":queue.Queue(4),
     "p2":queue.Queue(4),
     "p3":queue.Queue(4),
     "p4":queue.Queue(4)
    }
    p1 = Process("p1",0,message)
    p2 = Process("p2",0,message)
    p3 = Process("p3",0,message)
    p4 = Process("p4",0,message)
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()