#write a python script to concatenate following the dictionaries to create a new one
#sample dictionary:dic1={1:10, 2:20} dic2={3:30, 4:40} dic3{5:50, 6:60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(dic1,':',dic2,':',dic3,)
dic1.update(dic2)
dic1.update(dic3)
