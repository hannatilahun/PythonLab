pylist = [1,2,3,4,5,6,7,8,9]
pytuple = (1,)
nopytuple = (1)
pydict = {1:"qwerty","hi":"taye"}
pydict2 = {"numbers :" : pylist}
pylist.insert(3,44)
del pylist[0]

#print(type(pytuple))
#print(type(nopytuple))
#print(*pylist)

pyset = {2,3,5,6,8,3,4,4,4,2,2,2,3,3,1,1,1}
pyset1 = {11,22,33,44,44,33,55,66,77}
pyset = pyset.union(pyset1)

def fun(a, b, c, d):
    print(a, b, c, d)
 
my_list = [1, 2, 3, 4]

fun(*my_list)

#python dictionary
print(pydict.get("hi"))
print(pydict[1])
print(pydict2["numbers :"])
print("this is set: "+ str(pyset))