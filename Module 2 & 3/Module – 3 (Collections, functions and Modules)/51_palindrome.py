input_str=input("enter string :")
reverse_str=""
for i in input_str:
    reverse_str=i+reverse_str
    
print("reverse string :",reverse_str)
if input_str==reverse_str:
    print(input_str,"is Palindrom")
else:
    print(input_str,'is not Palindrom')


# s="madam"
# r=""
# for i in s:
#     r=i+r
# print(r)
# if s==r:
#     print("p")
# else:
#     print("np")