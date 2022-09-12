# Os
from multiprocessing import Process, Lock
import time
import os
def f(lock,id,sleepTime):
    lock.acquire()
    print("I'm P"+str(id)+" Process ID: "+str(os.getpid()))
    lock.release()
    time.sleep(sleepTime)   

if __name__ == '__main__':
    print("Main Process ID: "+str(os.getpid()))
    lock=Lock()
    p1=Process(target=f, args=(lock,1,3,))   
    p2=Process(target=f, args=(lock,2,5,))   
    start=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print("I am the main process, the two processes are done")
    print ("Time taken:- "+str(end-start)+"secs")   
