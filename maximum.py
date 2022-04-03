#code finds the maximum number among many of what the user enters
try:
    i=int(input())
except:
    print("there is an error")
max1=i
while True:
    try:
        i=int(input())
    except:
        break
    if i>max1:
        max1=i
print (max1)
#code finds the minimum number among many of what the user enters
try:
    i=int(input())
except:
    print("there is an error")
min1=i
while True:
    try:
        i=int(input())
    except:
        break
    if i<min1:
        min1=i
print (min1)
#code finds the maximum number among these list's numbers
l=[12,34,98,67]
max1=l[0]
for i in l:
    if i>max1:
        max1=i
print(max1)
#code prints these list's elements while counting them
i=0
l=[12,34,50,98]
for h in l:
    i=i+1
    print(i,h)
#code finds the sum of these list's elements 
sum1=0
l=[12,34,50,98]
for h in l:
    sum1=sum1+h
print("the sum is",sum1)
#code finds the sum and the average of these list's elements 
count=0
sum1=0
l=[12,34,50,98]
for h in l:
    count=count+1
    sum1=sum1+h
print("the sum is",sum1)
print("the count is",count)
print("the average is",sum1/count)
#code finds the sum and the average of what the user enters 
try:
    i=int(input())
    count=1
except:
    print("something went wrong my dear ")
sum1=i
while True:
    try:
        i=int(input())
    except:
        break
    count=count+1
    sum1=sum1+i
print("the sum is",sum1)
print("the average is",sum1/count)



