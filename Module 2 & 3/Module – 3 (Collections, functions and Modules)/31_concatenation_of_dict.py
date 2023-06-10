"""Write a Python script to concatenate following dictionaries to create a
new one."""
#first
d1 = {1:"Man",2:"Fean"}

d2 = {3:"abc",4:"xyz"}

d3 = {}
for d1 in (d1,d2) : d3.update(d1)

print(d1)
print(d2)
print(d3)

#second
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={}

dic1.update(dic2)#concentation of two dictionary
print(dic1)


#third method
dic1={1:"Man", 2:"Fean"}
dic2={3:"Marav", 4:"Meet"}
dic3={5:"Marut",6:"Harsh"}

dic4 = {}

for i in (dic1, dic2, dic3):
    for key, value in i.items():
        dic4[key] = value
print("dic1",dic1)
print("dic1",dic2)
print("dic1",dic3)
print("concentation of dic1,dic2,dic3 : ",dic4)

