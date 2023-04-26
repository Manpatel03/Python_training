name = input("Enter Your Name : ")
gender = input("Enter Gender : ")
age = int(input("Enter your Age : "))

product_name = input("Enter Product Name : ")
product_gram = int(input("Enter Product Gram : "))
print("current gold price (1 grm) : 5752")







goldprice = 5752
total_goldprice = goldprice*product_gram #345120
print("Total Gold Rate : ",total_goldprice)


making_charges = 845 # 1 gram
print("Making charges (1 gram) : 845")
total_making_charges = product_gram * making_charges
print("Total Making Charges : ",total_making_charges)

# Total Amaount
totalamount = total_goldprice + total_making_charges
print("Total Amount : ",totalamount)




if gender == "male" and age >65:
    
    if totalamount > 200000 and totalamount < 300000:
        discount_amount = (totalamount*20)/100
        
        print("DISCOUNT : 20%")
        
        
        total_Net_Amaount = totalamount - discount_amount
        print("Discount Amaount : ",discount_amount)
        print("Total Net Amount : ",total_Net_Amaount)
        
    elif totalamount > 300000 and totalamount < 500000:
        discount_amount = (totalamount*30)/100
        
        print("DISCOUNT : 30%")
        total_Net_Amaount = totalamount - discount_amount
        print("Discount Amaount : ",discount_amount)
        print("Total Net Amount : ",total_Net_Amaount)
        
    elif totalamount > 500000 :
        discount_amount = (totalamount*35)/100
        
        print("DISCOUNT : 35")
        total_Net_Amaount = totalamount - discount_amount
        print("Discount Amaount : ",discount_amount)
        print("Total Net Amount : ",total_Net_Amaount)
        
if gender == "male" and age <65:
        if totalamount > 200000 and totalamount < 300000:
            discount_amount = (totalamount*10)/100
            
            print("DISCOUNT : 10%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)
            
        elif totalamount > 300000 and totalamount < 500000:
            discount_amount = (totalamount*20)/100
        
            print("DISCOUNT : 20%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)
        
        elif totalamount > 500000 :
            discount_amount = (totalamount*25)/100
        
            print("DISCOUNT : 25%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)

else:
    #check condition female and age
    if gender == "female" and age >65:
        
        if totalamount > 200000 and totalamount < 300000:
            discount_amount = (totalamount*25)/100
            
            print("DISCOUNT : 25%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)
            
        elif totalamount > 300000 and totalamount < 500000:
            discount_amount = (totalamount*35)/100
            
            print("DISCOUNT : 35%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)
        
        elif totalamount > 500000 :
            discount_amount = (totalamount*40)/100
            
            print("DISCOUNT : 40%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)
        
    if gender == "female" and age <65:
        if totalamount > 200000 and totalamount < 300000:
            discount_amount = (totalamount*15)/100
                
            print("DISCOUNT : 15%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)
            
        elif totalamount > 300000 and totalamount < 500000:
            discount_amount = (totalamount*25)/100
            
            print("DISCOUNT : 25%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount) 
        
        elif totalamount > 500000 :
            discount_amount = (totalamount*30)/100
            
            print("DISCOUNT : 30%")
            total_Net_Amaount = totalamount - discount_amount
            print("Discount Amaount : ",discount_amount)
            print("Total Net Amount : ",total_Net_Amaount)