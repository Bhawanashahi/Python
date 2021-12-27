#write a python program to convert atuple
tuple=('a','b','h','y','a','s')
j=''
for i in tuple:
    i=j+i
    print(i,end='')
    print()
    print(type(i))

    def converttuple(tup):
        #initlize an empty string
        str=''
        for item in tup:
            str=str+item
            return str

#driver code
tuple=('h','e','l','l','o','w','o','r')
str=converttuple(tuple)
print(str)