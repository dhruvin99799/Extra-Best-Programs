# Palindrome Number
# s=0
# n=int(input("Enter Number = "))
# t1=n
# for n1 in range(n):
#     t = n%10
#     s = (s*10)+ t
#     n = n/10


# if(s==t1):
# 	print("Pali......")
# else:
#     print("Not Pali.....")


n=int(input("Enter Number = "))
rev=0
n1=n
while(n>0):
    rev=(rev*10)+n%10
    n=n//10
if (n1==rev):
    print("Palidrome")
else:
    print("Not")

