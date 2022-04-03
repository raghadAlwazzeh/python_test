# to build up a function (def function's name ():.......)
def love():
    print("Lana loves Ali alot")
love() # when we want to run what we put inside the function
# here we are gonna show you some examples for functions with parameters
# the first one
def hello(o):
    print("hello "+o)
    print ("it was such an amazing thing to talk with you")
hello(input("Who are you? "))
# the second one
def sum_average(a,b,c,d):
    sum1=a+b+c+d
    average=sum1/4
    print ("Sum: ",sum1)
    print ("Average: ",average)
sum_average(int(input("first number: ")),int(input("second number: ")),int(input("third number: ")),int(input("fourth number: ")))
# when we use * then number after a variable that its type is a string we repeat the string until we get our entered number of the string variable
k="Ali Al_radwan is such an amazing and handsome person "
o=int(input("Please enter the times that you want us to repeat your sentence "))
print(k*o)
# the output of the next statement is Lana Ali
print("Lana{}".format(" Ali"))
# the output of the next statement is Lana loves Ali alot
print("Lana{} Ali{}".format(" loves"," alot"))
# so we can day that .format() function comes after string variable that contains {} and what the function does is replacing its parameter with {} taking in count the order  
# if the the function doesn't have the return statement then the function will have return None statement in a hidden way
def square1(k):
    r=k*k
    return r
f=square1(6)
print (f)# the output is gonna be 36
# if we write print instead of return in the previous example then the output will be 36 (because when we wrote variable f, we run what was in yhe function)None
# no thing will be run from the function's statements after the interpreter does the first return
def silly(x,y):
    sum1=x+y
    return sum1
    avg=(x+y)/2
    return avg
print (silly (1,2))# here the output is 3
# to let the interpreter show the average we write the programme as next
def silly(x,y):
    sum1=x+y
    avg=(x+y)/2
    return sum1,avg
print (silly (1,2))# here the output is gonna be 3 1.5
# the next shows code in which the interpreter print True if any word from a list of words has more 5 characters and print false otherwise (we used function in our code)
def check(lista):
    for i in lista:
        if len(i)>5:
            return True
    return False
print(check(input ("Please enter whatever you want")))
# We are gonna give examples about the dfinition's range
def r(o):
    s=o*o
    return s
print (r(s))# here we are gonna get an error telling us that s is not defined because it is only like that inside the function
# in the next code y is a global variale because it was defined out of the function's range
def r(x):
    s=y+1
    return s
y=4
print (r(7))# the output is gonna be 5
def r(x):
    s=y+1
    y=x*x
    return s
y=4 
print (r(7))# when we define y inside the function then we are not gonna take its value out that range so hee we are gonna get an error telling us that we have to put the y's statement before the s's statement
# if we write the y's statement before the s's statement then the output is gonna be 50 not taking what we put inside y out of the function's range 
