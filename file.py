#code to read the text as a single string 
#1_variable1=open("the name of the txt file","r"for reading/"w" for writing)
Rad=open("lana1.txt","r")
#2_variable2=varible1.read()
lana=Rad.read()
#3_print(variable2[:the index of the character  that youu want the interpreter keeps printing util it reaches to ])
print(lana[:88])
#4_variable1.close()to close the open file
Rad.close()
print ("\n")
# we can also write the previous example like what will appear in the next line but we put variables to not get lost
print(open("lana1.txt","r").read()[:88])
Rad.close()
#code to print how many characters the txt file contains contains
#print(len(variable2))
print(len(lana))
print("\n")
# we can also do it like what shown in the next line
print(len(open("lana1.txt","r").read()))
print("\n")
#code in which we consider that every line is a sting (in this code the output will be ["the first line\n","the second line\n","the third line\n"]
Rad1=open("lana1.txt","r")
lana1=Rad1.readlines()
# [:number] this number can let us know when the interpreter will stop printing because it's gonna stop when it reaches to the character that has this number as a index
print(lana1[:2])
Rad1.close()
print("\n")
# we can also write this code like this
print((open("lana1.txt","r").readlines())[:2])
print("\n")
# code to know how many lines are in the txt file
print(len(open("lana1.txt","r").readlines()))
print("\n")
#code to not let any of " " or [] appears in the previous programm's output (the output here is gonna appear as lines saperated by empty lines)
Rad2=open("lana1.txt","r")
for t in Rad2.readlines()[:2]:
    print (t)
Rad2.close()
# code to solve empty lines' problem
Rad3=open("lana1.txt","r")
for i in Rad3.readlines()[:2]:
    print(i.strip())
print("\n")
Rad4=open("lana1.txt","r")
print ((Rad4.readlines())[:2])
print("\n")
