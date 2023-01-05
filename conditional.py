
i = int(input("Enter a number: "))

for i in range(i):
    if i == 0 : continue

    if i%3==0 and i%5==0:
        print("Hello World"+str(i))
    elif i%3==0:
        print("Hello")
    elif i%5==0:
        print("World")

greeting = "hello" if 5>6 else "hello there"
print(greeting)

choice = 2

match choice:
    case 0:
        print("case 0")
    case 1:
        print("case 1")
    case 2:
        print("case 2")
    case other:
        print("case other")
