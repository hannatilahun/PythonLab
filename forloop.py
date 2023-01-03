n=int(input("Enter no. of variables:"))
for i in range(n):
    a = list(map(int, input().rstrip().split()))
for x in a:    
    if x%3==0:
         print("hello")
    elif x%3==0 and x%5==0:
        print("hello world")

    elif x%5==0:
        print("world")

    







   



    