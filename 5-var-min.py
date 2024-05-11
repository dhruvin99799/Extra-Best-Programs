a=10
b=20
c=30
d=40
e=50
if(a<b):
    if(a<c):
        if(a<d):
            if(a<e):
                print("A is Min")
            else:
                print("E is Min")
        elif(a<d):
            print("A is Min")
        else:
            print("D is Min")
    elif(a<c):
            print("A is Min")
    else:
            print("C is Min")
elif(b<c):
    if(b<d):
        if(b<e):
            print("B is Min")
        else:
            print("E is Min")
    elif(b<d):
            print("B is Min")
    else:
            print("D is Min")
elif(c<d):
    if(c<e):
        print("C is Min")
    else:
        print("E is Min")
elif(d<e):
    print("D is Min")
else:
    print("E is Min")