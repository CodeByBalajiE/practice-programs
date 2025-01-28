#day1 coding task program 1
#add and sub of two num 
a=int(input("enter the first num")) #first num
b=int(input("enter the second num")) #second num
c=input("enter the operation") #operation
if c=="+": #addition
        result=a+b
        print(result)
elif c=="-": #subtraction
        result=a-b
        if result<0: #check if the result is negative 
            print(result*-1) #make it as positive
        else:
            print(result)
        
