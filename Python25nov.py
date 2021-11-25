"""Python"""
""""""

"""
"""

"""Indexing/Slicing in Python"""
# s="HITESH"   #index: 0 t0 4
# print(s[0])
# print(s[3])

# #New Program
# s="HITESH"   #index: 0 t0 4
# print(s[7]) #If index out of range then Error

# #New Program
# s="WELCOME"   #index: 0 t0 6
# print(s[1:6:2])     #s[1],s[3],s[5]

# #New Program
# s="WELCOME"   #index: 0 t0 6
# print(s[:6:])

# #New Program
# s="WELCOME"   #index: 0 t0 6
# print(s[9:22:3])    #Slicing if index out of range then no error


"""
First Thing First:
1. Default Step Size always 1.
2. If upper bound and lower bound are of different
signs then firstly bring them to a common sign

+ve Step Size: 
1. Default lower bound: 0    Default Upper Bound: n
2. Upper Bound > Lower Bound Else Empty Value


-ive step size
1. Default Lower Bound: -1    
Default Upper Bound=-n-1=First Element will be retrieved
2. Upper Bound < Lower Bound Else Empty Value

Summary
+ive Step Size: Output will be retrieved only in case
when we travel from left to right ie upper index is 
bigger: Forward Movement

-ive Step Size: Output will be retrieved only in case
when we travel from right to left ie upper index is 
smaller. Backward Movement: Reverse

Final Summary: After adding step size in lower bound
if we are approaching towards upper bound then we 
will get output.  
"""

# s="WELCOME"
# print(s[-2:-6])     #Step size: +ive, Upper Bound>Lower Bound

# #New Program
# s="WELCOME" #0 to 6 or -7 to -1
# print(s[-2:-6:-1])     #s[-2], s[-3], s[-4], s[-5]

"""There is no Negative Marking in our Class. 
Be Confident
"""
# #New Program
# s="WELCOME" #0 to 6 or -7 to -1
# print(s[:-6:-1])   #s[-1:-6:-1]

# #New Program
# s="WELCOME" #0 to 6 or -7 to -1
# print(s[-3::-1])   #s[-3:-8:-1]

# #New Program
# s="WELCOME" #0 to 6 or -7 to -1
# print(s[::-1])   #s[-1:-8:-1]

# #New Program
# popu=[23,34,45,56,78,89,99,110,120]
# popu_des=popu[::-1]
# print(popu_des)

# #New Program
# s="WELCOME" #index 0 to 6, -7 to -1
# # print(s[-5:4:-1])   #s[2:4:-1]: Common sign
# print(s[-2:1:-1])     #s[5:1:-1]: s[5],s[4],s[3],s[2]
# print(s[-2:1:-1])     #s[-2:-6:-1]: s[-2],s[-3],s[-4],s[-5]


# #New Program
# s="WELCOME"
# print(s[2:6])   #Moving from Left to Right
# print(s[6:2])
# print(s[-2:-6])

# #New Program
# s="WELCOME"
# print(s[2:6:-1])   #s[2],s[1]
# print(s[6:2:-1])
# print(s[-2:-6:-1])  #s[-2],s[-3]

# #New Program
# s="WELCOME"
# print(s[-33:-3000:-3])

# #New Program
# L1=["RAM","ANIL","VIKAS","SONU"]
# print(L1[-1])
# L1[-1]="SONU PRAKASH"
# print(L1[-1])


"""Operators: 7 Wonders of World
1. Arithmetic Operators: 7
2. Logical Operators
3. Conditional Operators
4. Bitwise Operators
5. Assignment Operators: 
6. Identity Operators
7. Membership Operators
"""

"""
Arithmetic Operators:
+      : Addition
-       : Subtraction
*       : Multiplication
/       : Division
%       : Modulus: Remainder
**      : Power
//      : Floor Division: Nearest Smaller Quotient as
                          Whole No  
"""
# #New Program
# a,b=5,7
# print(a+b,a-b)

# #New Program
# a,b=4,2
# r=a/b
# print(r)

# #New Program
# a,b=7,3
# print(a%b)

# #New Program
# a,b=5,4
# print(a**b)  #a to the power b

# #New Program
# a,b=5,4
# print(a//b)     #1.25 ie varying between 1 and 2
# a,b=5,-4        #-1.25 ie varying between -1 and -2
# print(a//b)

#New Program
"""Conditional Operators:
==      Equals to
!=      Not Equals to
>       Greater Than
<       Less Than
>=      Greater Than equals to
<=      Less than equals to
Returns True or False

"""
# New Program
# a,b=5,7
# s=a==b
# print(s)

# # New Program
# a,b=5,7
# print(a<=b)


"""Logical Operators
and:    #If both inputs are True then only Output True         
        Else Output False     
or      #If any one of the inputs is True then output
        is True
not     #Reverse the Input: If input True then output
        #False

Generally used with Conditions.
"""

# #New Program
# a,b=2,3
# s=a==2 and b==3     #True and True
# print(s)

# #New Program
# a,b=2,3
# print(a>3 or b<=3)  #False or True


"""
Assignment Operators:
"""










