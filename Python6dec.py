"""Python: """
"""Regular Expression/RE/re/RegEx: 
re is called a world's tiny language which provide
support to different languages ie different languages
supports re and have inbuilt libraries/packages for re.

re is used to create sequence of characters/special 
characters through which we find strings or sub strings
from another string. 
"""
# import re
# s="""abc def mnnnnna123 9898123456 98 9910675291 pqr vikas
#  jjjjjjjjjjjjjjjj 8888234567
#  """
# p="\d{10}"
# print(re.findall(p,s))

"""
Even Python official documentation says re is difficult.

"""


"""
Metacharacters: Used to create different patterns
Metacharacters in re: 
^ $ . * + ? {} [] () | \
"""
# import re
# s="welcome to india. google is No. 1 Company."
# p="india"
# res=re.findall(p,s)
# print(res)

#New  Program


"""
Character Class: []
If we pass any character or collection of characters in 
character class then those characters are searched individually
It means ORing of characters inside character class.

[collection of characters] : Individual characters will be searched
[a-z]: all individual small letters a to z will be searched
[A-Z]: all individual capital letters A to Z will be searched
[0-9]:  all individual numbers will be searched
[a-zA-Z]: All individual English alphabets
[a-zA-Z0-9_]: All alphanumeric including _
[^a-z]: All individual characters other than a to z.
[^0-9]: All individual characters other than numbers 

"""
# import re
# s="welcome to india."
# p=r"[abpqrstAP]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="welcome to india."
# p=r"[a-z]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="india. abc_*^@"
# p=r"[a-zA-Z0-9_*]"
# res=re.findall(p,s)
# print(res)

"""Metacharacter \: \ is used to remove the special
meaning of a metacharacter. or even we can use character
class for same purpose []
Rest we can create different patterns using \
[0-9]: \d: Individual numbers
[^0-9]: \D: all individual characters other than numbers
[a-zA-Z0-9_]: \w: All individual alphanumeric characters
[^a-zA-Z0-9_]: \W: All individual characters other than
                alphanumeric characters
 

"""
# import re
# s="hits*.@123 abc*."
# p="."     #Incorrect Pattern as . is a metacharacter
# res=re.findall(p,s)
# print(res)


# #New Program
# import re
# s="hites*.@123 abc*."
# p="\."
# res=re.findall(p,s)
# print(res)


# #New Program
# import re
# s="hites*.@123 abc*."
# p="[.]"
# res=re.findall(p,s)
# print(res)

"There is no negative marking in our class"

# #New Program
# import re
# s="hites*.@123 abc*."
# p="[^a-z]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc 123 89#$ nnnn78"
# p=r"[0-9]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc 123 89#$ nnnn78"
# p=r"\d"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc 123 89#$ nnabcnn78"
# p=r"abc"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc 7 123 89#$ nnabcnn78"
# p=r"\d\d"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc 7 123 89#$ nnabcnn78"
# p=r"[0-9][0-9]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc 7 123 89#$ nnabcnn78 7777755555 1234567890"
# p=r"\d\d\d\d\d\d\d\d\d\d"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc pqr dddd efgh ddLg ab*C DDe 12L"
# p="\w\w\w"
# res=re.findall(p,s)
# print(res)

"""Quantity Class {}
{m}: Exact m continuous characters
{m,n}: Any no of characters between m to n
{m,}: min m characters max no limit
{,n}: min no limit and max n characters
"""

# import re
# s="9999956565 12 abc vikas 9996767675"
# p=r"\d{10}"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="99999 12 abc 3333456abc 1234 vikas 9996767675"
# p=r"\d{5,10}"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="99999 12 abc 3333456abc 1234 vikas 9996767675"
# p=r"\d{5,}"
# res=re.findall(p,s)
# print(res)

"""Some meta characters for quantity matching
*: Search 0 or more occurrence 
+: Search 1 or more occurrence
?: Search 0 or 1 occurrence

"""
# #New Program
# import re
# s="abc de pqr 123 *&abc ##234"
# p=r"[a-z]+"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc de ABpqr 123 *&abc ##234"
# p=r"\w+"
# res=re.findall(p,s)
# print(res)


# #New Program
# import re
# s="abc@abc pqr $ mno@def gh@pqrst"
# p=r"[a-z]{3}@[a-z]{3}"
# res=re.findall(p,s)
# print(res)


# #New Program
# import re
# s="abc@abc pqr $ mno@def gh@pqrst"
# p=r"[a-z]+@[a-z]+"
# res=re.findall(p,s)
# print(res)


# #New Program: ab007@abc.com
# import re
# s="vikas123@cetpa.com a@.com vk@99acres.in bb@c.com,"
# p=r"\w+@\w+[.]\w+"
# res=re.findall(p,s)
# print(res)

# #New Program
# import urllib.request
# import re
# f = urllib.request.urlopen("http://genetixbiotech.com/contact/")
# # print(type(f))
# data=f.read()
# # print(type(data))
# # print(data)
# s=str(data)
# pEmail=r"\w+@\w+\.\w+"
# resEmail=re.findall(pEmail,s)
# print(resEmail)
# pMob=r"\d{10}"
# resMob=re.findall(pMob,s)
# print(resMob)

"""BeautifulSoup: Best Library for Web Scrapping"""

"""Location Matching Meta Characters: 
^: Starting of String
$: End of String
"""
# import re
# s="india is no 1 company. google is Best"
# p="^india"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="google is no 1  company. india is Best india"
# p="google$"
# res=re.findall(p,s)
# print(res)

"""Other Meta Characters
. : Search all individual characters other than new line

"""
# import re
# s="abc google\n &^$123# .  ,,,,"
# p=r"."
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="abc google\n &^$123# .  ,,,,CETPA"
# p=r"google"
# res=re.findall(p,s)
# print(res)

"""Other Meta Characters
| : Oring of patterns

"""
# import re
# s="google abc pqr hitesh ABCCCC"
# p="goole|abc"
# res=re.findall(p,s)
# print(res)

"""
()
"""
# #New Program
# import re
# s="98_ abc 6788_  8976 123_"
# p="(\d+)_"
# res=re.findall(p,s)
# print(res)


# #New Program
# import re
# s="abc def ab @12 ghi"
# p="[a-z]{3}"
# res=re.split(p,s)
# print(res)

# #New Program
# import re
# s="abc def ab @12 ghi"
# p="[a-z]{3}"
# res=re.split(p,s)
# print(res)











