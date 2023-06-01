
open("myfile.txt","a")
fl=open("myfile.txt","r+")

print(fl.read())

# --------|or|----------
#         v  v

# def file_read(fname):
#     txt = open(fname)
#     print(txt.read())
# file_read('read.txt')