

n = int(input("Enter Value :"))
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end="")
    k+=2
    print()