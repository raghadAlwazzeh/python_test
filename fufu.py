# code to write a dicimal number in a binary form
l=[]
k=[]
i=int(input())
if i==0:
    print(0)
while True:
    if i==0:
        break
    l.append(i%2)
    i=i//2
y=len(l)-1
while y>=0:
    k.append(l[y])
    y=y-1
print (k)
