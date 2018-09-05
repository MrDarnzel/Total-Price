price = input("How much does your item cost?") #Asks user the cost of item
tax = input("What is the sales tax rate?")     #Asks user the amount of tax

price1 = float(price)                          #Converts the price into a float
tax1 = float(tax)                              #Converts the tax into a float
tax_amount = (price1 * tax1)                   #Takes the amount of tax on that product

total_price = (tax_amount + price1)            #Adds the tax to the price of the product
print(total_price)                             #Print the total price
