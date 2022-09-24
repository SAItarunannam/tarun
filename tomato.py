t=int(input("enter the price of tomato:"))
if(t>50):
    t=t+(20/100*t)
    print(t)
elif(t<50):
    t=t+(40/100*t)
    print(t)
else:
    print("wrong price")