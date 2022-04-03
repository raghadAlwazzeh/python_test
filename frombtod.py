#code to write a binary number in a decimal form
l=[]
i=input("Enter your binary number")
for j in i:
    j=int(j)
    l.append(j)
dicimal=0
h=len(l)-1
for m in l:
    dicimal=dicimal+((2**h)*m)
    h=h-1
print ("your dicimal number is:",dicimal)
