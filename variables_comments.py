 # to write comments '#' is used in python  

#for multiline comments
""" we use more than two double quotes(known as doc string)"""

#types of variables are 4
""" to write variables we have three types 
camel case = keerthanaIsTheBest
pascal case = KeerthanaIsthebest
snake case = Keerthana_Is_the_best"""
#int
a =15
# float
b = 13.5
#str
c= "abcdef"
#bool
k = False
#complex
m= 5j


#string slicing
#a[start:stop:space]

#operators
#arithmetic operators
a+b
a-b
a*b
a/b
a//b
a**b

"""assignment operators
# =,+=,-+,*=,/+,//+"""

"""comparision operators
>,<,>=,<=,==,!="""

"""logical operators 
and,or,not"""

"""print(ord(a)) gives unique number value
print(chr(a)) gives actual value from number"""

#if else statements 
if (a>b):
    print("k")
else:
    print("m")


#if else ladder
if():
   print(" ")
elif():
    print()
else:
    print()
                         #FOR LOOP
n = int(input()) 
for i in range(1,n+1,1):
    print("Hello World")

n =10
for i in range(1,n+1,1):
    print(i)

n =10
for i in range(n,0,-1):
    print(i)

n =187
for i in range(1,11):
   # print(f"{n} * {i} = {n*i}")
    print(n,'*',i,'=', n*i)

n =50
sum =0
for i in range(1,n+1):
   # print(f"{n} * {i} = {n*i}")
   sum += i
print(sum)

n =3
sum =0
sum2 =0
for i in range(1,n+1):
   if(i%2 == 0):
      sum += i
   else:
      sum2 +=i
print(sum,sum2)

n =144
sum =0
for i in range(1,n+1):
   if(n%i== 0):
      sum += i
print(sum)


