try:
    a=int(input("enter the weight of clothes for washing"))
except:
    print("INVALID INPUT")
if a<=2000 and a>0:
    print("Time Estimated:",25,"min")
elif a>2000 and a<=4000:
    print("Time Estimated:",35,"min")
elif a>4000 and a<=7000:
    print("Time Estimated:",45,"min")
elif a==0:
    print("Time Estimated:",0,"min")
elif a>7000:
    print("OVERLOADED")

    
    

