shop ={}
main = """

        1.manager
        2.customer
        3.exit
        """
print(main)  

status = True
while status :
    ch = int(input("enter ch : "))
    if  ch == 1 :
        food = """

                1)fruit Details
                2)fruit  all Details
                3)exit
            """
        print(food)
            
        choice =  int(input("Enter your choice : "))
        print("-----------------------------------")  
        if choice == 1:
            fruit = {}
            print("fruit details")
            print("-----------------------------------")    
            fr = True
            while fr:
                fruit_name = input("Enter fruit name : ")
                fruit_price = input("Enter fruit price : ")
                fruit_quantity = input("Enter fruit quantity : ")
                print("-----------------------------------")  
                        
                fruit['name'] = fruit_name
                fruit['price'] = fruit_price
                fruit[''] = fruit_quantity
                        
                shop[fruit_name] = fruit
                print(shop)       

                print("-----------------------------------")
                n = input("do you want to y or yes : ")
                if n == "y" or n =="yes":
                    fr = True
                else:
                    fr = False
                    
        elif choice == 2:
            for i,j in shop.items():
                print(i)
                for k , v in fruit.items():
                    print(k,"=",v)
                      
    elif ch ==2:
        print("customer")
        
        
    
    elif ch ==3:
        print("exit")
        status = False