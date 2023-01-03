
def sum():
    print("hello every one this is our firest python lab class")
    
    a,b,c=5,7,8
    d=a+b+c
    print(c)
    x,y,z="orang","banna","chery"
    print(x)
    print(y)
    print(z)
    x=y=z="orang"
    print(x)
    print(y)
    print(z)

    a="hanna"
    b=23
    c=453.645
    print ("my name is {1} and i am  {0} years old ".format(a,b,c))
    print(f"")


sum()


A="ABEBE"
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
print(A[0])

print(A[-1])
print(A[-2])
print(A[-3])
print(A[-4])
print(A[:4])
print(A[-1:-4])
print(A[::-1])
x="hello,word"
print(x.split(","))

y=int(input("please enter number"))

if y%3==0:
    print("hello")
elif y%5==0:
    print("world")
elif y%3==0 and y%5==0:
    print("hello world")
  

y=int(input("please enter number"))
match y :
   case 2 :
    print("two")
   case 4:
     print("four")
   case _:
     print("other")
      

for i in range(1,10):
    print(i)
