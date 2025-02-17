#Factors of number
n=int(input("enter number:"))
for i in range(1,n):
    if(n%i==0):
        print(i)

#To do list 
a=[]
n=int(input("enter n :"))
for i in range(n):
    i=input(("Enter your task:"))
    a.append(i)
print(a)
