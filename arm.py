# Armstrong Number

# n1=0
# t=1
# n=int(input("Enter Number = "))
# t=n
# for n in range(n1):
# 		a = n % 10
# 		n1 = n1+(a*a*a)
# 		n = n/10
# if(t==n1):
# 		print("Armstrong")
# else:
# 	print("Not Armstrong")



n=int(input("Enter Number = "))
n1=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if n1==sum:
    print("Arm")
else:
    print("Not")