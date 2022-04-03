nooooooode={}
j="0"
node1={"Left":-1,"Value":4,"Right":-1}
for i in node1:
    nooooooode[j]=node1[i]
    j=j+"0"
node2={"Left":-1,"Value":6,"Right":-1}
for k in node2:
    nooooooode[j]=node1[k]
    j=j+"0"
node3={"Left":node1,"Value":5,"Right":node2}
node4={"Left":-1,"Value":11,"Right":-1}
for m in node4:
    nooooooode[j]=node4[m]
    j=j+"0"
node5={"Left":-1,"Value":16,"Right":-1}
for t in node5:
    nooooooode[j]=node5[t]
    j=j+"0"
node6={"Left":node4,"Value":12,"Right":node5}
node7={"Left":node3,"Value":10,"Right":node6}
nooooooode["9"]=5
nooooooode["9"]=12
f=list(nooooooode.values())
l=f[0]
r=len(f)
for a in f:
    for c in f[:len(f)-r]:
        if c<=l:
            l=c
            print(l)
    r=r-1
print(f)
