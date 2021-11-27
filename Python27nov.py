"""Python Operators Continue"""
"""
Arithmetic Operators
Logical Operators
Conditional Operators
Bitwise Operators
Assignment Operators
Membership Operators
Identity Operators
"""

"""
Bitwise Operators:
&: Bitwise AND : If both inputs are 1 then output 1 else
                 Output 0   
|: Bitwise OR   : If any of the input 1 then output 1 else
                  output 0
~: Bitwise NOT  : Inverse of Input. 
^: Bitwise XOR  : If both the inputs are same then output
                  0 else output 1  
<<: Bitwise Shift Left: All bits will be shifted towards
                        left and LSBs will be filled by
                        0.
                        s=a<<b then a will be shifted 
                        towards left by b times.                        
>>: Bitwise Right Shift: All bits will be shifted towards
                        right and MSBs will be filled by
                        MSB.

a,b=5,3     #  a= 0101, b= 0011
s= a & b    #  b= 0011
print(s)    #  s= 0001  ie s=1

"""
# #New Program
# a,b=5,3
# s= a & b
# print(s)

# #New Program
# a,b=5,3
# s= a | b
# print(s)

"""There is No Negative Marking in Our Class.
No Practise No Learning
"""
# #New Program
# a,b=5,2     #a=00000101, b= 2
# s=a << b    # First 00001010,
# print(s)    #Second 00010100: 20

"""
Assignment Operators: 13 in Nos 
=   Equals to: 
+=  s+=a    then s=s+a  i+=1 ie i=i+1
-=  s-=a   then s=s-a
*=  s*=a  then s=s*a
/=  s/=a  then s=s/a
%=  s%=a  then s=s%a    
**= s**=a  then s=s**a
//=  s//=a  then s=s//a
&=  s&=a  then s=s&a
|=  s|=a  then s=s|a
^=  s^=a  then s=s^a
<<= s<<=a  then s=s<<a
>>= s>>=a  then s=s>>a

"""
# #New Program
# a,b=5,2
# b+=a        #b=b+a
# print(b)

# #New Program
# a,b=5,2
# b**=a        #b=b**a  ie 2 power 5
# print(b)

# #New Program
# a,b=5,3
# b&=a        #b=b&a
# print(b)

"""Membership Operators: To check whether an element
belongs to a iterator or not.
in                       
not in
Return True or False
"""
# s="HITES"
# a="T"
# r=a in s
# print(r)

# #New Program
# s="HITES"
# a="T"
# r=a not in s
# print(r)

# #New Program
# s="HITES"
# print("HI" in "HITES")

# #New Program
# L1=["India","America","Japan"]
# print("China" in L1)

"""BSMach13920213M3968005"""

"""Identity Operators: Check whether the variables/data
is holding the same memory location or not 
is
is not
"""
# a=[23,45,67,88]
# b=[23,45,67,88]
# print(id(a))
# print(id(b))
# a=5
# b=5
# print(id(a))
# print(id(b))
# a="HITES"
# b="hites"
# print(id(a))
# print(id(b))

# #New Program
# a=[22,33,55,45]
# b=a #Always
# print(id(a))
# print(id(b))
# a=5
# b=a
# print(id(a))
# print(id(b))


# #New Program
# a=5
# b=a
# print(a is b)   #
# print(a==b)

# #New Program
# a=[2,3,4]
# b=[2,3,4]
# print(a is b)
# print(a==b)

"""
Conditional Statements:
if
elif    : else if
else

Indentation: 
If we have any sub statement inside a statement then
internal statements will be indented statements.

The main statement is called a heading which is 
terminated by colon :, and all internal statements
are collectivly called suite 
All the sub statements of a suite are indented statements
means all the sub statements will be at a fixed space
or gap wrto heading
"""
# #New Program
# a=5
# b=a

# #New Program
# a=2325 #Always Run
# if(a==2325):        #Heading
#     print("Correct")    #Suite First Statement
#     print("Welcome")    #Suite Second Statement
#     print("Open")    #Suite Third Statement
# print("Program Complete")

# #New Program
# a=int(input("Enter The Code:")) #
# if(a==7):
#     print("Code is Correct")
#     print("You are Welcome")
# else:
#     print("Code is Incorrect")
#     print("You are not allowed to Enter")


# #New Program
# a=int(input("Enter The Code:")) #
# if(a==7):
#     print("Code is Correct")
#     print("You are Welcome")
# else:
#   print("Code is Incorrect")
#   print("You are not allowed to Enter")

# #New Program
#   a=5   #Error
# print(a)

# #New Program
# a=3
# if(a==5):
#     print("Hello")
# elif(a==6):
#     print("Welcome")
# elif(a==7):
#     print("HITES")
# elif(a>7):
#     print("ABCD")
# else:
#     print("PQRS")

# #New Program
# day=input("Enter Day:")
# if(day=="Sunday"):
#     print("Its Holiday, Take Rest")
# elif(day=="Saturday"):
#     print("Its Holiday, Go for Shopping")
# elif(day=="Friday"):
#     print("Its Holiday, Go for Movie")
# else:
#     print("Its Working Day, Go to US")






