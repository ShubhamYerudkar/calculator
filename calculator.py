n1=int(input("enter operand1: "))
n2=int(input("enter operand2: "))
print("1)addition \n 2)subtraction \n 3)multiplication \n 4)division")
c=int(input("enter mode of calculation: "))
if c==1:
    print("Addition: ",int(n1+n2))
elif c==2:
    print("Subtraction: ",int(n1-n2))
elif c==3:
    print("Multiplication: ",int(n1*n2))
elif c==4 :
    print("Division: ",int(n1/n2))
else :
    print("please choose correct option")
