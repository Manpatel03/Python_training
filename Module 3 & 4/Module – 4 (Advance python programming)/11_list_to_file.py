# Write a Python program to write a list to a file

name=["man","meet","harsh"]
fl=open("myfile.txt","w")
for i in name:
    fl.write("%s\n" % i)
content=open("myfile.txt")
print(content.read())