"""Write a Python script to concatenate following dictionaries to create a
new one."""

dic1={1:"man", 2:"meet"}
dic2={3:"het", 4:"harsh"}
dic3={5:"marut",6:"marav"}

dic4 = {}
for i in (dic1, dic2, dic3):
    for key, value in i.items():
        dic4[key] = value 
print("dic1",dic1)
print("dic1",dic2)
print("dic1",dic3)
print("concentation of dic1,dic2,dic3 : ",dic4)

