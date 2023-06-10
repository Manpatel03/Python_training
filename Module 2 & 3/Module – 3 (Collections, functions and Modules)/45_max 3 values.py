"""Write a Python program to find the highest 3 values in a dictionary """

dict = {"a":123,"b":121,"c":13,"d":12,"e":3,"f":2}

dic1 = sorted(dict.values())

print("Dictionary Short: ",dic1)

print("Highest 3 Values : ",dic1[-3:])
