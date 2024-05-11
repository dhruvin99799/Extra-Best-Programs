unit = int(input("Enter your unit = "))

if unit<=50:
    r = unit*0.50
    
elif unit<=150:
    r = 25+(unit-50)*0.75

elif unit<=250:
    r = 100+(unit-150)*1.2

else:
    r = 220+(unit-250)*1.5



print(r)

