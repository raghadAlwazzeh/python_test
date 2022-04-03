#xx=12
#yy=4
#zz=45
#aa=17
#uu=34
#uu=uu%3
#xx=xx+36
#yy=yy*8
#zz=zz/1000
#aa=aa**2
#print (xx)
#print (yy)
#print (zz/100)
#print (aa)
#print (uu)
#ggg="hello"+" "+"lana"
#print (ggg)
#print ("lana"+" "+"is "+"such "+"a "+"great "+"girl!")
#print (type(ggg))
#print (str(zz))
#print (int(10/2))
#print (int(9/2))
#print(float(xx))
#roz="123"
#print(type(roz))
#lan=int(roz)
#lan=lan+1
#print(lan)
#m=input("Who are you?")
#print("welcome",m)
#print("welcome"+m)
#def addtwo(a,b):
#    return a+b
#print(addtwo(int(input("Enter the first number")),int(input("Enter the second number"))))
#x=5
#while x>0:
#    print(x)
#    x=x-1
#print("blestoff")
#print(x)


#code repeats writing what the user enered till entering "done"
#while True:
#    x=input("> ")
#    if x=="done":
#        break
#    print (x)
#print("Done!")

#while True:
#    x=input("> ")
#    if x[0]=="#":
#        continue
#    if x=="done":
#        break
#    print(x)
#print("Done")

#for i in [5,4,3,2,1]:
#    print(i)


#friends=["lana","sally","raghad","rozet"]
#for friend in friends:
#    print("happy new year",friend)
#print("happyb new year",friends)
lana=open("lana1.txt","r")
print(lana.readlines()[:2])
lana.close()
print("\n")
file = open("lana1.txt","r")
lines = file.readlines()
print(len(lines))
for l in lines[:2]:
    print(l)
file.close()
print("\n")
Rad1=open("lana1.txt","r")
for h in Rad1.readlines()[:2]:
    print(h.strip())
Rad1.close()
print("\n")
Rad = open ("lana1.txt","r")
roz = Rad.read()
print(len(roz))
print(roz[:67])
Rad.close()
print("\n")
eng2sp={}
eng2sp["one"]="uno"
eng2sp["two"]="dos"
eng2sp["three"]="tres"
print(eng2sp)

lana12={'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(lana12)

names={"Ali":"Al_radwan","Lana":"Al_wazzeh"}
print(names)
lana123=names["Ali"]
print(lana123)
print(names["Lana"])
#######
USA={"gold":33,"silver":17,"bronze":12}
print(USA,"\n")
USA1={}
USA1["gold"]=33
USA1["silver"]=17
USA1["bronze"]=12
print(USA1)

