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

#Moving negative numbers to end

a = [1, -1, 5, 0, -8]
b = []
c=a
# Loop through each item in the list
for i in c:  # Use a copy of 'a' to avoid modification issues
    if i < 0:
        b.append(i)  # Move negative numbers to list b
        a.remove(i)  # Remove negative numbers from list a

print(a + b)  # Print positive numbers first, then negative ones
