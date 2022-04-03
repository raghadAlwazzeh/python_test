u = int(input ("Enter the number of keys"))
i=0
j=0
l=[]
k=0
d={}
l1=[]
h=0
a=0
print ("Now enter the keys")
while i<u:
    key=input()
    l1.append(key)
    i=i+1
f = int(input ("Enter the number of values"))
print ("Now enter the values please")
while j<f:
    g=input()
    l.append(g)
    j=j+1
while h<u:
    if k<f:
        d[l1[h]]=l[k]
        k=k+1
        h=h+1
    else :
        d[l1[h]]="....."
        h=h+1
print(d)
