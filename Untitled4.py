


class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        class car1(car):
            def __init__(self,model):
                super().__init__(name,color,model)
                self.model=model
x=car1("sike","black","A4")
x.name
        


# In[27]:


def add():
    a=4
    b=4
    c=a+b
    print(c)
add()
    


# In[33]:


def odd():
    a=int(input("enter a number"))
    if a%2!=0:
        print("this number is odd")
    else:
        print("this number is not odd")
odd()


# In[34]:


def even():
    a=int(input("Enter a number"))
    if a%2==0:
        print("this number is even")
    else:
        print("this number not a even")
even()


# In[38]:


def add(a,b):
    result=a+b
    return result
#     print(result)
add(3,5)


# In[43]:


def swap(a,b):
    b,a=a,b
    print(a,b)
swap(3,8)
    


# In[ ]:




