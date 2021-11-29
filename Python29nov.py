"""Python """
"""Functions """
# #Calci
# #Business Logic Layer
# import math
# import operator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
#
# #Presentation Layer
# ch=input("Enter Choice +, -, *, /, log:")
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# if(ch=="+"):
#     res=add(no1,no2)
#     print("Result:",res)
# elif(ch=="-"):
#     res=sub(no1,no2)
#     print("Result:",res)
# elif(ch=="*"):
#     res=operator.mul(no1,no2)
#     print("Result:",res)
# elif(ch=="/"):
#     res=div(no1,no2)
#     print("Result:",res)
# elif(ch=="log"):
#     res=math.log(no1,no2)
#     print("Result:",res)
# else:
#     print("Incorrect Choice")

"""Functions Second Phase
All Variables in Python are of ref type ie if we pass
one variable to another variable in Python then their
addresses are passed/copied but not their values.

In Python, functions calling is based on call by 
reference concept ie when we call a function then
following operation takes place ie
formal parameters = actual parameters so in Python
address of actual parameters are assigned to formal
parameters 

"""
# a=5     #5 is stored at 1000 then a will point to 1000
# b=a     #b will also start pointing to same location 1000
# print(a,b)
# print(id(a),id(b))

# def add(u,v):
#     # print(id(u))
#     s=u+v
#     print(id(s))
#     return s
#
# a,b=5,7
# # print(id(a))
# r=add(a,b) #u=a, v=b, r=s
# print(id(r))
# print(r)

"""All Variables defined inside functions are local
variables ie the scope of these variables is only inside
functions and these variables exists only till function
call executes. Once we come out of the functions, the
local variables of functions are automatically destroyed.

The Variables defined outside functions are global
variables and they can be accessed from both inside
 functions and outside functions.
"""


# #New Program
# def add(u,v):
#     s=u+v
#     return s
# a,b=5,7
# r=add(a,b) #u=a, v=b, r=s
# print(r)
# print(s)    #Error because s is a local variable

# #New Program: Not a better approach
# def add():
#     s=a+b
#     return s
# a,b=5,7
# r=add()
# print(r)

# #New Program
# a,b,c,d,e,f,g=2,3,4,5,6,7,8

"""All Variables in Python are of ref type ie if we 
assign one variable to another then their addresses
are copied ie RHS variables address is copied to LHS
variable.
Ideally in ref type variables if two variables are 
holding the same address then by changing one variable
as a whole using assignment operator other variable
should also get changed. But it not happens in Python,
because Python supports dynamic memory allocation ie
whenever we assign a new value to a variable, it is
stored at new location.

When variables are created in Python: Whenever we 
assign a new value to a variable and previous locations
for the same variables are destroyed by Garbage Collector
if those locations are not referred by any variable.

When Variables are created: The moment we assign a
new value to a variable, now if we assign a new value
to a variable inside function then also a new variable
will be created but new variables created inside 
functions are always local variables. Now if we have
both local and global variables with same name in a 
program then inside function local variables will be
used and outside functions global variables will be
used.

We can access global variables inside functions ie
we can read global variables inside functions but 
once we try to modify the value of global variables 
inside functions then new local variables are created.

Now if we want to change the value of global variables
inside functions and don't want to create new local
variables then we can use global keyword with variable
names.  
 
"""
# a=5
# a=666666666666666
# b=a
# a=7
# print(b)

# #New Program
# a=5     #a address 1000
# b=a     #b address 1000 All variables are of ref type
# a=6     #a address 2000
# print(b)
# b=a
# print(b)

# #New Program
# a=5
# print(id(a))
# b=a     #Ref type
# print(id(a),id(b))
# a=6
# print(id(a),id(b))

# #New Program
# a=5             #First Variable 1000 location
# print(id(a))
# a=6     #Second variable 2000 location and first variable
#         #of 1000 location destroyed by Garbage Collector
# print(id(a))

# #New Program
# def func1(a):
#     a=6         #New Variable : Local variable
#     print(a)
#
#
# a=5             #a address 1000
# print(a)        #a of 1000
# func1(a)
# print(a)


# #New Program
# def func1():
#     print(a)    #Global Variable
#     b=7         #Local Variable
#     print(b)    #Local Variable
# a,b=5,6             #a address 1000
# print(a)        #a of 1000
# func1()
# print(a)
# print(b)        #Global Variable

# #New Program
# def func1():
#     global a
#     a=6
#     print(a)
#
# a=5
# print(a)
# func1()
# print(a)

"""
Dynamic Memory Allocation : Memory Allocation at run
time.

C Lang: Compile Time Memory Allocation
Python: Run Time Memory Allocation/Dynamic Memory 

C Lang
int a,b ; Compile time variables creation
a=5;
b=a;    Call by Value

Python
a=5
a=6

Till now the functions we have studied are the
Required Argument Functions, in next phase after 
few classes we will study more types of functions. 

"""


