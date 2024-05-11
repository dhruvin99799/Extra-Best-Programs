a=10
b=200
c=30
d=40
if(a<b):
   if(a<c):
       if(a<d):
           print("A is Min")
       else:
           print("D is Min")
   elif(a<c):
           print("A is Min")
   else:
           print("C is Min")
elif(b<c):
   if(b<d):
       print("B is Min")
   else:
       print("D is Min")
elif(c<d):
       print("C is Min")
else:
       print("D is Min")
