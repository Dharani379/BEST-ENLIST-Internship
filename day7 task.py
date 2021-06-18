#Creating a function for getting input from userand doing folloeing atmatic operations
a= int(input("Enter the value:"))
b= int(input("Enter the value:"))
import math
def Dharani(a,b):
    c=a+b
    d=a-b
    x=a*b
    y=a/b
    return c,d,x,y


print(Dharani(a,b))

#Creating a function covid()'''2nd task'''
def covid(patient_name,body_temparature):
    if body_temparature<str(0):
        default = str(98)
        print("Patient name is:",patient_name,"Body temparature is:",default)
    else:
        print("Patient name is:",patient_name,"Body temparature is:",body_temparature)
covid("Mahanati","")
covid("Mahanati","99")
    
