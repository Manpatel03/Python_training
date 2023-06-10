"""
Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5

"""



num1 = int(input("enter number 1:")) #10
num2 = int(input("enter number 2")) #20

if  abs(num1-num2) == 10 or num1+num2 ==10:
    print("Difference is 10")
else:
    print("No Difference is 10")