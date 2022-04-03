# code to count how many letters of t and y are in the txt file
Rad = open("lana1.txt","r")
t_count = 0
y_count=0
txt = Rad.read()
for i in txt:
    if i=="t":
        t_count = t_count+1
    elif i=="y":
        y_count = y_count+1
print("t has appeared",t_count,"times")
print("y has appeared",y_count,"times")
Rad.close()#here we have to write this statement to be able to write another statements that belongs to the same file
txt1=(open("lana1.txt","r")).readlines()
for y in txt1:
    print (y.strip())
Rad.close()
# We also use dictionaries to count the letters in the txt file
Rad2=open("lana1.txt","r")
txt1=Rad2.read()
w={}
w["t"]=0
w["y"]=0
for h in txt1:
    if h == "t":
        w["t"]=w["t"]+1
    elif h == "y":
        w["y"]=w["y"]+1
print("t has appeared",w["t"],"times")
print("s has appeared",w["y"],"times")
Rad2.close()
# We also use dictionaries to count the letters in the txt file using this way
Rad3=open("lana1.txt","r")
txt2=Rad3.read()
w={}
w["t"]=0
w["y"]=0
for h in txt1:
    if h == "t":
        w[h]=w[h]+1
    elif h == "y":
        w[h]=w[h]+1
print("t has appeared",w["t"],"times")
print("y has appeared",w["y"],"times")
Rad3.close()
# what we wrote require adding 26 variables if we want to count all the letters that are in the txt file and that is what can be solved using dictionaries
Rad4=open ("lana1.txt","r")
w={}
for r in Rad4.read():
    if r not in w:
        w[r]=0
    w[r]=w[r]+1
print("t has appeared",w["t"],"times")
print ("y has appeared",w["y"],"times")
# We can count whatever we want from any string
d="lana loves radian alot "
w={}
for i in d:
    if i not in w:
        w[i]=0
    w[i]=w[i]+1
print ("l has appearsd",w["l"],"times")
print("r has appearsd",w["r"],"times")
# to sum up, we can now put a rule to count the letters
#1_we need a variable which is list or string and here we have to say that open("the name of the txt file","r").read() is a single string but txt file","r").readlines() is a list
#2_we need an empty dictionary
#3_we need a for loop to pass on all the string's characters
#4_we need an if statement which has this form
#if the same loop's variable not in the dictionary's name:
    #the dictionary's name[variable]=0
#the dictionary's name[variable]=the dictionary's name[variable]+1 (this statement is in the loop)
#################################################################################################################
#how we can count words that are in a string instead of letters (to solve this problem we have split function which turn the string into a list with strings as elements inside it
k="Lana knows verry well that she is not goona regrette this because she loves radian alot"
r=k.split()# this is the string
j={}
for t in r:
    if t not in j:
        j[t]=0
    j[t]=j[t]+1
for u in j:
    print(u,"has appeared",j[u])# this statement helps us to not determine a speacific word but instead of that we can know all the key's values


        
