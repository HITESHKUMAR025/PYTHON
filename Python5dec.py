"Python"
"""Generators"""

# L1=list(range(1,11))
# print(L1)

# #New Program
# L1=[1,2,3,4,5,6,7,8,9,10]
# for e in L1:
#     print(e)

"""Generators are created using functions which are
having pre implemented __iter__ and __next__ method.
These methods are automatically implemented.
Each generator is having a yield keyword in it.

If yield is there in function then it becomes 
generator type. generator holds the state of the
function/variables till it is not completely executed.
"""
#New Program
def func1():
    pass
# def generate1():
#     yield 1
#     yield 2
#     yield 3
#
# print(type(func1()))
# print(type(generate1()))
# for i in generate1():
#     print(i)


# #New Program
# def generate1():
#     for i in range(5):
#         yield i
#
# for j in generate1():
#     print(j)

# #New Program:
# def myEvenRange(start,stop):
#     if(start%2==1):
#         start+=1
#     for i in range(start,stop,2):
#         yield i
# for i in myEvenRange(3,10): #4,6,8
#     print(i)

# #New Program:
# def myEvenRange(start,stop):
#     if(start%2==1):
#         start+=1
#     for i in range(start,stop,2):
#         yield i
# # for i in myEvenRange(3,10): #4,6,8
# #     print(i)
# obj=myEvenRange(3,10)
# iter=obj.__iter__()
# e=iter.__next__()
# print(e)
# e=iter.__next__()
# print(e)
# e=iter.__next__()
# print(e)
# # e=iter.__next__()
# # print(e)


