#write python program to create 
from copy import deepcopy
#create a tuple
tuplex = ("hello",5,[],)
print(tuplex)
#make a copy of a tuple using deepcopy()
tuplex_colon=deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)