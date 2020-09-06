#1.without creating a class
"""
from threading import *

def demo():
    for i in range(1,6):
        print('thread',i)

t1=Thread(target=demo)#thread creation
t1.start() #task 1 to 6 ni vachhe j  pa6i j close thae jay
#t1.join() #badhi process pati gaya pa6i print thay....pela t1 j complete kare 
print('bye----------')

"""
#2.by extendin thread class

"""
while extanding the thread calss only run and init methods can
be overridden.other can't be overridden by child class
"""
"""
import threading
class child(threading.thread):
    def run(self):
        for i in range(1,6):
            print("hello child !",threading.current_thread().getname())

obj.child()
obj.start()
obj.join()
print("bye world !"),threading.current_thread().getname()
"""

#3. without extending thread class
"""
from threading import *
class parent():
    def fun(self):
        for i in range(1,6):
            print("hello world !")
obj=parent()
th1=Thread(target=obj.fun)
th1.start()
th1.join()
print("bye bye world !")
"""

#time comparision

import threading
import time

def fun1():
    for i in range(1,6):
        time.sleep(1)#sleep fuction time leta hae
        print(i)

def fun2():
    for i in range(1,6):
        time.sleep(1)#sleep fuction time leta hae
        print(i+100)

"""
start_time = time.time()
fun1()
fun2()
print(time.time() - start_time)
"""

# using thread
t=time.time()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()
tt=time.time()
print(tt-t)
