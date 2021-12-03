"""MultiThreading"""
"""
MultiTasking System: 
1. Multiprocessing: Bigger applications where different
applications do not share resources with each other.
2. Multithreading: Smaller programs where different
threads can share the resources. 
Thread is the smalles of unit of code that can be fetched
to CPU directly.

OS: Event Scheduling:
"""
# #Simple Sequential Execution
# def func1():
#     for i in range(10):
#         print("Func1:",i)
# def func2():
#     for i in range(10):
#         print("Func2:",i)
# func1()
# func2()

# #Multithreaded
# import threading    #MainThread
# def func1():
#     for i in range(100):
#         print("Func1:",i)
#
# def func2():
#     for i in range(100):
#         print("Func2:",i)
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# # func1()
# th1.start()     #2 Threads: th1 and mainthread
# th2.start()     # 2 or 3 threads
# for i in range(100):
#     print("Main Thread:",i)

# #New Program
# import threading
# def func1():
#     global u
#     for i in range(100):
#         u+=1
# def func2():
#     global v
#     for i in range(100):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print(u,v)

#
# #New Program
# import threading
# def func1():
#     global u
#     for i in range(1000):
#         u+=1
# def func2():
#     global v
#     for i in range(1000):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print(u,v)

# #New Program
# import threading
# def func1():
#     global u
#     for i in range(10000):
#         u+=1
# def func2():
#     global v
#     for i in range(10000):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print(u,v)



# #New Program
# import threading
# def func1():
#     global u
#     for i in range(100000):
#         u+=1
# def func2():
#     global v
#     for i in range(100000):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print(u,v)

# #New Program
# import threading
# def func1():
#     global u
#     for i in range(1000000):
#         u+=1
# def func2():
#     global v
#     for i in range(1000000):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print(u,v)

# #New Program
# import threading
# def func1():
#     global u
#     for i in range(1000000):
#         u+=1
# def func2():
#     global v
#     for i in range(1000000):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# while(th1.is_alive() or th2.is_alive()):
#     pass
# print(th1.is_alive())
# print(th2.is_alive())
# print(u,v)

# #New Program: join
# import threading
# def func1():
#     global u
#     for i in range(10000000):
#         u+=1
# def func2():
#     global v
#     for i in range(10000000):
#         v+=1
# u,v=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# th1.join()  #Only Joins with Main Thread
# print(th1.is_alive(),th2.is_alive())
# th2.join()
# print(th1.is_alive(),th2.is_alive())
# print(u,v)



# #New Program
# from tkinter import *
# import threading
# import time
# def moveWindow():
#     while(1):
#         global i
#         if(i==1000):
#             i=0
#         else:
#             i+=10
#         root.geometry(f"200x200+{i}+100")
#         time.sleep(0.1)
# i=0
# root=Tk()
# root.geometry("200x200+0+100")
# th1=threading.Thread(target=moveWindow)
# th1.start()
# root.mainloop()

