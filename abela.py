x = "abebe"
print(x[0])
print(x[-3])
#string slice

print(x[-3:-1])
print(x[::-1])
print(x.upper())
print(x.lower())
print(x.title())

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
print(' '.join(text))

number = 60
print("binary equivalent of number 60 is",bin(number))
print(oct(number))
print(hex(number))

x=14
if x % 7 ==0:
    print('even')
else:
    print('odd')   
    
x=20
if x%2==0:
    print('even')     
elif x%2!=0:
    print('odd')    
else:
    print('no number')   
    
    
y=int(input('Enter any number '))
if y%3==0:
    print("hello")   
elif y%5==0:
    print("world")    
else :
    y%5==0 and y%3==0
    print("hello world")  
 
 #match
x = int(input("please enter any number:"))
match x:
    case 2:
        print('two')
    case 3:
        print('four')    
    case _:
        print('other')    
        
for i in range(10,0):        
    print(i)



