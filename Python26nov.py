"""Python"""
"""
Data Types:

Single Element/Single Valued Data Types:
int     23,5000,20000000....
float   2.3, 5.0, 9.999999
complex 2+3j
bool    True, False
NoneType: None

Multi Element/Multi Valued Data Types/Iterators/
Sequence/Collection: 
str
list
tuple
dict
set
frozenset

str: Collection of Homogeneous data type ie character only

list: Collection of Heterogenous data type

str: To put characters inside quotes

Single Line String:
Single Quote
Double Quotes
Triple Quotes: Triple Single Quotes, Triple Double Quotes

Multi Line String
Triple Quotes: Triple Single Quotes, Triple Double Quotes

"""
#New Program
# x='Welcome to HITES'
# print(x)
# x="Welcome to HITES"
# print(x)
# x='''Welcome to HITES'''
# print(x)
# x="""Welcome to HITES"""
# print(x)

# #New Program
# x='''Welcome to HITES.
# An Award Winning Training Company'''
# print(x)
# x="""Welcome to HITES.
# An Award Winning Training Company"""
# print(x)

"""
x=5
x="5"
ASCII: American Standard Code for Information Interchange
A: 65
ASCII: 8 Bits: 00000000: 0.....11111111: 2 ** 8 - 1=255
256 Combinations: 0 to 255
A: 65           a: 97
B: 66           b: 98
C: 67           c: 99
D: 68           d: 100
.
.
Z: 90           z: 122

Python 3.9.7
In the year 2008, Python 2 moved to Python 3
Unicode Standard: 
16 Bit: 0 to 65535 

ord function: To convert a character to its unicode value

chr function: To convert a unicode value to corresponding character
"""
# #New Program
# x=5     #101
# print(type(x))
# x="5"   #
# print(type(x))

# #New Program
# print(ord("A"))
# print(ord("z"))
# print(ord("5"))
# print(ord("क"))
#
# print(chr(2325))

#New Program
# ch=input("Enter Any Capital Letter:")   #"D"
# ch=ord(ch)      #ch=68
# ch=ch+32        #ch=100
# ch=chr(ch)      #ch="d"
# print("The Character in Lower Case is:",ch)

"""
Data Types:
List_var=[Comma separated values/arguments] 
"""
# L1=[2,3,3.5,True,"HITES"]
# print(L1)

"""
Indexing and Slicing:
Indexing: To access particular single element of an
iterator/multi element data.

To access particular element: var_name[index]
If we pass any out of range index value in case of 
indexing then there will be IndexError
n elements: +ive index: 0 to n-1
n elements: -ive index: -n to -1

Slicing: To access set of elements from an iterator.
var_name[lower_bound:upper_bound]
Note: upper_bound is discarded in Python in most of 
the cases and in case of slicing it is discarded
Note: In case of slicing if index values ie upper bound
or lower bound values are out of range then there won't
be any error in the program
#In case of +ive step size, upper bound should always
be bigger than lower bound then only we will get elements
at the output else there will be empty value of same type

Extended format of slicing
var_name[Lower_bound:Upper_bound:step_size]
Note: Default step size is always 1

Note: In case of +ive step size, default lower bound
will be 0 and default upper bound will be n (ie 
elements till end will be retrieved)
"""
# s="CETPA"   #0 to 4: 5 Elements:
# print(s[0])
# print(s[1])
# print(s[4])

# #New Program
# L1=[22,33,44,55]
# print(L1[0])
# print(L1[2])

# #New Program
# s="HITES"   #index: 0 to 4
# print(s[5]) #IndexError

# #New Program
# s="HITES"   #5 Elements: index: 0 to 4, -5 to -1
# print(s[4])
# print(s[-1])
# print(s[0])
# print(s[-5])

# #New Program
# s="WELCOME" #index: 0 to 6
# print(s[1:4])   #ELC, ELCO: s[1],s[2],s[3]
# print(s[0:5])   #WELCO

# #New Program
# s="WELCOME" #Index 0 to 6
# print(s[2:8])   #LCOME, s[2],s[3],s[4],s[5],s[6]
# print(s[7])

# #New Program
# s="WELCOME"
# print(s[2:5000000])

# #New Program
# s="WELCOME"
# print(s[5:2])   #MOC, ME,


# #New Program
# s="WELCOME"
# x=s[5:2]
# print(type(x))
# print(s[5:2])   #MOC, ME,
# print(x)

# #New Program
# L1=[2,3,4,5]
# print(L1[2:2])  #Upper bound is discarded
# print(L1[4:2])  #Upper bound should be bigger

# #New Program
# s="WELCOME" #Index 0 to 6
# print(s[1:6])
# print(s[1:6:1]) #s[1], s[2], s[3], s[4], s[5]
# print(s[1:6:])
# print(s[1:6:2]) #s[1],s[3],s[5]
# print(s[1:7:2]) #s[1],s[3],s[5]
# print(s[1:6:3]) #s[1],s[4]

# #New Program
# s="WELCOME"
# print(s[1:6:2])     #s[1],s[3],s[5]
# print(s[:6:2])      #s[0],s[2],s[4]
# print(s[1::2])      #s[1],s[3],s[5], upper bound:7 discarded
# print(s[::2])       #s[0],s[2],s[4],s[6]

# #New Program
# L1=["Ram","HITES","Anil","Sonu","Lucky"]
# print(L1[::2])

# #New Program
# s="WELCOME"
# print(s[5:2:2])

# #New Program
# s="WELCOME"
# print(s)
# print(s[:])
# print(s[::])

# #New Program
# s="WELCOME"
# print(s[::2])
# print(s[1::2])















