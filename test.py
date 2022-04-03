#find the maximum, the minimum,the sum and the average of what the user enters and that's when he enters "done"
sum1=0
count=0
i= input ()
try:
    max1=int(i)
    min1=int(i)
    sum1=sm1+i
    count=count+1
except:        
    while True:
        if i=="done":
            break
        else:
            try:
                max1=int(i)
                min1=int(i)
                d=int(i)
                sum1=sum1+d
                count=count+1
                break
            except:
                print("Invalid input")
                i=input()
while True:
    if i== "done" :
        break
    i=input()
    try:
        d=int(i)
    except:
        if i=="done":
            break
        else: 
            print("Invalid input")
            continue
    sum1=sum1+d
    count=count+1
    if d<min1:
        min1=d
    elif d>max1:
        max1=d
try:
    print("Maximum is",max1)
    print("Minimum is",min1)
    print("Sum is",sum1)
    print("Average is",sum1/count)
except:
    print("There is no numbers")

