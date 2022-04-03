lista=[6,8,90,65,14]
print(lista.sort())
print (sorted(lista, reverse= True))
print(lista.reverse())
u=reversed(lista)
print (u)
j=0
while j < len(lista):
    for i in lista:
        if i <= lista[j]:
            h=i
            i=lista[j]
            j=h
    j=j+1
for u in lista:
    print(u)

lista=input("Please enter your list: ")
j=0
while j < len(lista.split()):
    for i in lista.split():
        i=int(i)
        if i <= int ((lista.split())[j]):
            h=i
            i=int ((lista.split())[j])
            j=h
    j=j+1
for u in lista:
    print(u)
