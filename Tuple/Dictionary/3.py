#WAP to print a dictionary where the key are numbers between 1 and 15 (both included)
#and the values arev square of keys
d=dict()
for x in range(1,16):
    d[x]=x**2
    print(d)