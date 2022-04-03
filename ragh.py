#def lana ():
#    print("I love you lana more than you know")
#    print("Every thing is gonna be fine")
#lana()
#print("I trust you so do not worry")
#x=max("hello lana")
#print(x)
#y=min("hello lana")
#print(y)
#print(max("12 34"))
#print(min("1 2 3"))
#def greet (k):
#    if k=="es":
#        print("hola")
#    elif k=="fr":
#        print("bonjour")
#    elif k=="it":
#        print("esultare")
#    else:
#        print("hello")
#greet(input("enter whatever you want for the first time: "))
#greet(input("enter whatever you want for the second time: "))
#greet(input("enter whatever you want for the third time: "))
#greet(input("enter whatever you want for the fourth time: "))
h=0
while True:
    i=input()
    if i =="done":
        break
    try:
        i=int(i)
    except:
        print("Please Enter a number not a string")
        continue
    if i==50:
        h=h+1
if h>0:
    print ("we found this number",h,"times")
