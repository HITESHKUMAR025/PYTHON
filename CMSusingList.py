"""CMS"""
"""
Customer Management System: CMS

ERP: Entreprise Resource Planning
SAP Software 

Customer Management System: CMS
CRUD Operation: Create, Read, Update, Delete

Add Customer
Search Customer
Delete Customer
Modify Customer 


"""
#CMS
#BLL
idlist=[]       #Empty List
namelist=[]
agelist=[]
moblist=[]
def addCustomer(id,name,age,mob):
    idlist.append(id)       #idlist=[10,20,30...
    namelist.append(name)   #namelist=["hitesh","Anil","Amit"...
    agelist.append(age)     #agelist=[39,41,45...
    moblist.append(mob)     #moblist=[1234,2345,3456...
def searchCustomer(id):     #id=30
    i=idlist.index(id)      #i=2
    return i
def deleteCustomer(id):     #id=20
    i=idlist.index(id)      #i=1
    idlist.pop(i)
    namelist.pop(i)
    agelist.pop(i)
    moblist.pop(i)
def modifyCustomer(id,name,age,mob):    #id=30,name=Vishal..
    i=idlist.index(id)  #i=2
    namelist[i]=name
    agelist[i]=age
    moblist[i]=mob







#PL
print("Welcome to Pavan's CMS:")
def showCustomer(i):    #i=2
    print("Cust ID:",idlist[i],"Cust Name:",namelist[i],"Cust Age:",agelist[i],"Cust Mob:",moblist[i])
while(1):       #Infinte Loop,
    print("1 for Add Cust, 2 for Search Cust")
    print("3 for Delete Cust, 4 for Modify Cust")
    choice=input("Enter Choice 1 to 4:")
    if(choice=="1"):    #Add Customer
        id=input("Enter Cust ID:")          #id=10
        name = input("Enter Cust Name:")    #name="hitesh"
        age = input("Enter Cust Age:")      #age=39
        mob = input("Enter Cust Mob:")      #mob=1234
        addCustomer(id,name,age,mob)
        print("Customer Added Successfully")
    elif(choice=="2"): #Search Customer
        id=input("Enter Cust ID:")  #id=30
        i=searchCustomer(id)    #i=2
        showCustomer(i)
    elif(choice=="3"): #Delete Customer
        id=input("Enter Customer Id:")  #id=20
        deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="4"):
        id=input("Enter Customer ID:")  #id=30
        name=input("Enter Cust Updated Name:")  #hitesh
        age = input("Enter Cust Updated Age:")  #16
        mob = input("Enter Cust Updated Mob:")  #5555
        modifyCustomer(id,name,age,mob)
        print("Customer Modified Successfully")
    else:
        print("Incorrect Choice")




