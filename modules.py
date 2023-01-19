import math
import random
from pyreadline3 import Readline
#print(dir(math))
#print(dir(random))
pylist = []
#for i in range(50):
#    pylist[random.randint(0,9)] += 1

file  = open("file.txt","r")
readline = Readline()
print(file.readline())