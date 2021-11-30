"""Python"""
"""Indexing and Slicing in Python

Indexing: If index goes out of range then IndexError
will be generated.

If iterator is having n elements then its +ve index will
start from 0 and will go till n-1. 
Now Python even supports negative indexing also
If iterator is having n elements then its -ve index will
start from -n and will go till -1. 

"""
#Indexing
# s="HITES"   #s index 0 to 4
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[4])

# #New Program
# s="HITES"   #Index 0 to 4
# print(s[8]) #IndexError

# #New Program
# s="HITES"   #Index 0 to 4, -5 to -1
# print(s[0])
# print(s[-5])
# print(s[-1])

# #New Program
# cus=["hitesh","Raj","manish","Shivam"]  #Index 0 to 3, -4 to -1
# print(cus[-1])
# n=len(cus)
# print(n)
# print(cus[n-1])

# #New Program
# L1=[2,3,4]
# L1[0]=88    #List is Mutable
# print(L1)

# #New Program
# L1=(2,3,4)
# L1[0]=88    #tuple is immutable
# print(L1)

"""Slicing: To access 0,1 or more elements from an
iterator.
s="Welcome"     #index 0 to 6

Complete Syntax: var_name[lower_bound:upper_bound:step_size]
1. Upper bound is discarded in Python in most of the places.
2. Step size is optional, Default Step size is always 1
3. If index (upper bound or lower bound) in slicing 
goes out of range then there won't be any error.
4. if we add step size in lower bound then values 
should move towards upper bound if it doesn't happen
 then we get the empty outputs 
5. In case lower and upper bounds are of different 
signs then firstly we need to convert them to common
sign (+ve, -ve)

If step size is +ve: 
1. Results always moves from left to right. In case 
of +ive step size, upper bound should always be 
bigger than lower bound
2. Default lower bound: 0
3. Default upper bound: n

If step size is -ve: 
1. Results always moves from right to left. ie in 
case of -ive step size, upper bound should always be
 smaller than lower bound
2. Default lower bound: -1
3. Default upper bound: -n-1

"""
# s="Welcome" #0 to 6
# print(s[1:5:1]) #s[1],s[2],s[3],s[4]
# print(s[1:6:2]) #s[1],s[3],s[5]
# print(s[1:4])   #s[1],s[2],s[3], s[1:4:1]

# #New Program
# s="Welcome" #index 0 to 6
# print(s[20:80:2])   #Empty String

# #New Program
# s="Welcome"
# print(s[:5])    #Default lower bound 0

# #New Program
# s="Welcome"
# print(s[2:])    #Default upper bound n
# print(s[2::1])  #Default upper bound n

# #New Program
# s="Welcome" #7 Elements, 0 to 6
# print(s)
# print(s[:])
# print(s[::])    #Default lower bound 0, upper bound n
#                 #Default step size 1

# #New Program: Print all elements at even indices
# s="Welcome" #index 0 to 6
# print(s[::2])  #s[0],s[2],s[4],s[6]

# #New Program
# s="Welcome"
# print(s[4:80])

# #New Program
# s="Welcome" #0 to 6
# print(s[4:80])      #s[4],s[5],s[6]

# #New Program
# s="Welcome" #0 to 6
# print(s[6:2])   #Step size=1, Empty String
# print(s[2:2])   #Empty String
# print(s[-6:-2]) #Step size=1, s[-6],s[-5],s[-4],s[-3]
# print(s[-2:-6])

# #New Program
# s="Welcome"
# print(s[-1:-4:-1])  #s[-1], s[-2], s[-3]
# print(s[-2:-6:-2])  #s[-2],s[-4]

# #New Program
# s="Welcome"
# print(s[-2:-3:-2])  #s[-2]
# print(s[-6:-2:-1])

# #New Program
# s="Welcome"
# print(s[1:4:-1])
# print(s[4:1:-1])    #s[4],s[3],s[2]


# #New Program
# s="Welcome"
# print(s[2:-2:1])    #s[2:5:1]

# #New Program
# s="Welcome"
# print(s[-2:2:1])    #s[5:2:1]

# #New Program
# s="Welcome"
# print(s[-2:2:-1])    #s[5:2:-1]

# #New Program
# s="Welcome"
# print(s[2:-2:-1])    #s[2:5:-1]


# """New Program"""
# "1. Check if a number is even or odd number"
# n=int(input("Enter Any Number:"))
# if(n%2==0):
#     print("The Number is Even")
# else:
#     print("The Number is Odd")

# #New Program
# s="Welcome" #Reverse this string: Amazon
# print(s[::-1])  #-1,-2,3,...-7









