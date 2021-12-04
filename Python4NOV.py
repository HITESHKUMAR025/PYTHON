"Python"
# L1=[10,20,30,40]
# print(sum(L1))

"""Loops: 
To run set of statements repeatedly
Types of loops in Python
1. While Loop
2. For Loop
"""

# #New Program
# print("*")
# print("*")
# print("*")
# print("*")
# print("*")

"""
For Loop

Option 1: to use for loop directly on an iterator
for element in iterator:
    set of statements (suite)
Loop will run for n no of times where n is no of elements in
iterator
"""
# s="HITES"
# for e in s:
#     print(e)

# # #New Program
# L1=["HITES","Anil","Amit","Sonu"]
# for e in L1:
#     print(e)        #4 Times this statement will run

#New Program: Square of each element
"""To perform an operation on all the elements of an iterator
use 
for e in iterator:
    set of statements
"""
# #New Program
# L1=[3,5,6,8,12,9]
# for e in L1:
#     u=e*e       #u=e**2
#     print(u)

"""
To run set of statements for fixed no of times, we use for
loop using range iterator

for i in range(a,n,s):
    set of statements

1. range(a,n,s)
a: Lower Bound
n: Upper Bound (Upper bound is discarded here)
s: Step size

2. range(a,n)
a: Lower Bound
n: Upper Bound
s: Default step size: 1

3. range(n)
a: Lower Bound be default: 0
n: Upper Bound
s: Default step size: 1

"""
# #New Program
# for i in range(2,10,2):
#     print(i)


# #New Program
# for i in range(2,10):
#     print(i)

# #New Program
# for i in range(5):  #0, 4
#     print(i)

# #New Program
# for i in range(5):  #i:0 to 4
#     print("*")

# #New Program
# s="HITES"
# for e in s:
#     print(e)
#
# for i in range(5):
#     print(i)

# #New Program
# s="HITES"
# for e in s:
#     print(e)

# #New Program
# s=5
# for e in s: #Error: TypeError
#     print(e)

"""
for element in iterator:
    set of statements
"""

# #New Program
# for i in range(5):  #range(5): 0,1,2,3,4
#     print(i)
#     i+=2        #i=i+2: Interviewer is trying to confuse you

# #New Program
# for i in range(5):  #range(5): 0,1,2,3,4
#     i+=2
#     print(i)

# #New Program
# s="HITES"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])         #print(s[i])    #i=0,1,2,3,4

# #New Program
# s="HITES"
# for i in range(5):  #i=0,1,2,3,4
#     print(s[i])     #s[0],s[1],s[2],s[3],s[4]

# #New Program
# s="HITES"     #s=input("Enter Your Name:")
# for e in s:
#     print(e)

# #New Program
# s=input("Enter Your Name:") #s="Sonu"
# for i in range(len(s)):  #range(4): i=0,1,2,3
#     print(s[i])     #s[0],s[1],s[2],s[3]

# #New Program
# L1=[10,20,30,40,50,60,70,80,90]
# for i in range(0,len(L1),2):    #range(0,9,2)
#     print(L1[i])

"5:27 PM"

"""Assignment: Python is having 2.35 Lakhs+ libraries and
I will cover basic important libraries.
datetime is a library used in programming. 
Study it on your own.

I will teach around 3 to 4 projects including CMS. 
But I wish you guys in parallel, create at least 1 new
project on your own, surf on internet and create. If not
any new project then at least create a new management system
like student mgmt system, hr mgmt or other. 

"""

# #New Program
# s="HITES"
# for e in s:
#     print(e)
#
# s="HITES"
# for i in range(len(s)):
#     print(s[i])

# #New Program: Print Table of 2
# for i in range(1,11):
#     print(i*2)

# #New Program: Print Table of 2
# for i in range(2,21,2):
#     print(i)

# #New Program: Print Cube of 2 to 10. 2 cube, 3cube,...10 cube
# for i in range(2,11):
#     print(i**3)


