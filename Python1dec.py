"Python Continue"
"""
List Methods:


A general term: Functions vs Methods

Functions: The functions defined outside
class are generally called functions.

Methods: The functions defined inside class
are generally called methods.
In class generally there are 2 types of
functions, static functions and instance
functions. Out of these 2 also, static
functions inside class are generally called
functions and instance functions inside
class are generally called methods.
Developers generally call the instance 
functions as the main property of OOPS. 


Syntax to call a function:
function_name(arguments)

Syntax to call a method
object_name.method_name(arguments)

len(iterator)   #Function
print(arguments) #Function

L1=[2,3,4]  #Object of List class
L1.append(55)


"""
# L1=[22,33.4,"HITES"]
# L1[0]=45
# print(L1)

"""Inside class we have multiple methods.
To call these methods the syntax is
list_object_name.method_name(arguments)
"""

# #New Program
# print("HITESH")
# L1=[22,33,44]
# L1.append(55)
# print(L1)

# #New Program
# s="HITES"   #Object of string class
# r=s.lower()
# print(r)

# #New Program
# L1=["ABC","HITES","PQR"]
# L2=L1.lower()   #Error
# print(L2)

"""Extend method always work on iterators"""
# #New Program
# L1=[22,33,44,55]
# L1.extend("HITES")
# print(L1)
# L1=[22,33,44,55]
# L1.append("HITES")
# print(L1)

# #New Program
# L1=[22,33,44,55]
# L2=[66,77,88]
# L1.extend(L2)
# print(L1)
# L1=[22,33,44,55]
# L1.append(L2)
# print(L1)

# #New Program
# L1=[22,33,44,55]
# L1.insert(2,35)
# print(L1)

# #New Program
# L1=[22,33,44,55]
# L1.extend((22,33,44,55,66,77))
# print(L1)

# #New Program
# L1=[22,33,44,55]
# u=L1.append(77)
# print(L1)
# print(u)
# s="HITES"
# r=s.lower()
# print(s)
# print(r)

# #New Program
# def func1():
#     pass
# u=func1()
# print(u)

# #New Program
# def myfunc(L):
#     L[1]=89     #L address 1000
#
# L1=[22,33,44]   #L1 address 1000
# myfunc(L1)  #L=L1, L address 1000
# print(L1)

# #New Program
# L1=[22,33,44]
# L1.pop()    #Default last element
# print(L1)

# #New Program
# L1=[22,33,44,55]
# L1.pop(1)   #1 index
# print(L1)

# #New Program
# L1=[22,33,44,55]
# L1.remove(44)       #Element
# print(L1)

# #New Program
# L1=[22,33,44,55]
# print(id(L1))
# L1.clear()
# print(L1)
# print(id(L1))

# #New Program
# L1=[22,33,44]   #Object of list class
# i=L1.index(33)
# print(i)
# print(L1)

# #New Program
# x=5
# x=7

# #New Program
# L1=[22,33,44]
# L1.reverse()
# print(L1)

# #New Program
# L1=[22,25,29,81,72,34,56,42,33]
# L1.sort()
# print(L1)

# #New Program
# L1=[22,25,29,81,72,34,56,42,33]
# L1.sort(reverse=True)
# print(L1)

# #New Program
# L1=[22,33,44,33,55]
# n=L1.count(33)
# print(n)

# #New Program
# L1=[22,33,44,33,55]
# n=L1.count(66)
# print(n)

# #New Program
# L1=[22,33,44,33,55]
# n=L1.count()
# print(n)

# #New Program
# L1=[22,33,44]
# print(len(L1))

# #New Program
# L1=[22,33,44]
# L2=L1.copy()    #L2=L1
# print(L1,L2)
# print(id(L1),id(L2))

# #New Program
# L1=[22,33,44]
# L2=L1.copy()
# L1.append(55)
# print(L2,L1)
#
# #New Program
# L1=[22,33,44]
# L2=L1       #L2 address of L1
# L1.append(55)
# print(L2,L1)



