#write a python program to remove an itemfrom a set if it is present in the seet.
a={1,2,2,3,'hello','ok','python'}
if 'hello' in a:
    a.remove('hello')
    print(a)
else:
    print("not present")