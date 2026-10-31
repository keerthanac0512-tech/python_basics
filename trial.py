"""ast="malay"
pal =""
n=len(ast)
for i in range(len(ast)-1,-1,-1):
    pal = pal+ast[i]
print(pal)
a = int (input())
sum =0
for i in range(1,a):
   if(a%i == 0):
     sum += i
if sum == a:
   print(f"{a} is a perfect number")

stn = 'keera'
for i in range(len(stn)-1,-1,-1):
    print(stn[i],end="")


a = 'malayalam'
b =''
for i in range(len(a)-1,-1,-1):
    b += a[i]
if (a == b):
    print("palindrome")
else:
    print("not a palindrome")

sent = "adefrt&23452"
alp =0
val =0
spcl=0
for i in sent:
    if(i.isalpha()):
        alp += 1
    elif(i.isdigit()):
        val+=1
    else:
        spcl+=1
print(alp,val,spcl)"""

num = int(input("enter a value"))
while(num):
    print(num%10,end="")
    num =num//10
