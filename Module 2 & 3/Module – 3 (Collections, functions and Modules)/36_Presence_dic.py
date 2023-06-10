"""How Do You Check The Presence Of A Key In A Dictionary?"""

dict = {1:"man",2:"meet",3:"harsh",4:"marav"}
n= int(input("please enter key number : "))

if n in dict.keys():
    print("true")
else:
    print("false")