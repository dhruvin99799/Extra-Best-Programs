n=int(input("Enter Number : "))
count=0
while n!=0:
    n=n//10
    count+=1
print("number of digit is : ",count)