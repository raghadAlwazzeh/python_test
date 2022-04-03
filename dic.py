# to build an empty dictionary
# the dictionary's name={}
dic={}
# to add key_value's pairs to that dictionary ( We can add evem when the dictionary has some key_value's pairs inside it before)
#the dictionary's name["the key's name"]="the value's name" (we put these coutations in case that the variable's type is sting)
dic["one"]="1"
dic["two"]="2"
print(dic,"\n")
# the value's type can be different from the key's one
dic1={}
dic1["one"]=1
dic1["two"]=2 
dic1[5]=3 # the key is not only string
print(dic1,"\n")
# to print a key's value (print(the dictionary's name["the key's name"])( the output is 1)
print(dic1["one"],"\n")
# to delete a key_value's pair from a dictionary (del the dictionary's name[the key value])
del dic1[5]
print(dic1)
# to change a vlue we can write (the dictionary's name[the key value]=the new value)
dic2={"Lana":"Al_wazzeh","Ali":"Al_radwan","Sally":"Al_wazzah","Raghad":"Al_wazz"}
dic2["Sally"]="Al_wazzeh"
dic2["Raghad"]=dic2["Raghad"]+"eh"
dic2["Rozet"]="Al_wazzeh"
print (dic2)
print(len(dic2),"\n")# to print how many key_value's pairs are in the dictionary
# to not let any of " " or {} appears in the output of dictionary's printing (We use for and the dictionary's name.keys())
dic3={"apple":450,"orange":67,"pear":98,"banana":90}
for k in dic3.keys():
    print(k)# the output is gonna be
    #apple
    #orange
    #pear
    #banana
print("\n")
# the part will have the same output of ### 
dic4={"apple":450,"orange":67,"pear":98,"banana":90}
for k in dic4.keys():
    print(k,":",dic4[k])
h=list (dic4.keys())# We can also write h=list(dic4.keys())[:2] and the output is gonna be (['apple', 'orange']) 
print(h,"\n")
print(list(dic4.values())[:3])# there is a list for values too
print (list(dic4.items())[:3])#to print both the keys and values as pairs in a list which has this form [(key,value),(key,value).....]
# there is another way to print keys without using .keys()
sa={"apple":450,"orange":67,"pear":98,"banana":90}
for k in sa:
    print (k)
# the same output of the next code's one
dic4={"apple":450,"orange":67,"pear":98,"banana":90}
for k in dic4.keys():
    print(k)
###
dic4={"apple":450,"orange":67,"pear":98,"banana":90}
for k in dic4:
    print(k,":",dic4[k])
# in the next code we are gonna learn how to know if there is a key that we want to know about existence, is really in the dictionary or not
dic4={"apple":450,"orange":67,"pear":98,"banana":90}
print("banana" in dic4)#the output is gonna be True
print("car" in dic4)#the output is gonna be False
if "banana" in dic4:
    print(dic4["banana"])
else:
    print ("There is no banana")
# the dictionary's name[key]= the dictionary's name.get(key) but the second one has more flexibility than the first one while dealing with key that doesn't exist in the dictionary
print (dic4.get("car"))# here the output is gonna be None (that's why it has more flexibility I mean no error warning is gonna appear)
print (dic4.get("car",0))# this statement means that
       #if "car" in dic4:
       #    print(dic4["car"])
       #else :
       #    print(0)
# // to get an integer number after division / to get a float one
# we can know the number of the characters in any string by using len(the name of the string)function
# in the next code we are gonna see how we can change the dictionary's values by changing in another object
dic5={"apple":450,"orange":67,"pear":98,"banana":90}
dic6=dic5
print(dic6 is dic5)#here the output is gonna be True saying that dic5 and dic5 now are the same object
dic6["banana"]=88
print(dic5["banana"])
