#The binary search's code
l=[1,5,7,8,8,9,12]
start=0
h=0
i=int(input("Please enter the number"))
end=len(l)-1
while start<end:
    k=int((start+end)/2)
    mid=l[k]
    if i==mid:
        h=h+1
        break
    if i>mid:
        start=k+1
    if i<mid:
        end=k-1
if h>0:
    print ("The number has been found")
