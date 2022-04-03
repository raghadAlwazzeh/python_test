#code to know if what the user enters is a number or a string
x=input("Enter whatever you want: ")
try:
    y=int(x)
except:
    y=-1
if y>0:
    print("It is a number")
else:
    print("It is a string")
