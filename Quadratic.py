import math  #Imports math functions

a = input(" Coefficient of a? ")    #Asks user for Coefficient of a
b = input(" Coefficient of b? ")    #Asks user for Coefficient of b
c = input(" Coefficient of c? ")    #Asks user for Coefficient of c

print(" a = " + str(a), " b = " +  str(b), " c = " + str(c)) #Prints all Coefficients

#Quadratic Formula = ((-b) + ((square root of b^2 - 4ac)/2a)

d = ((int(b) * int(b)) - 4 * int(a) * int(c))   #Solves inside of Square Root
print(d)    #Prints answer

print( ( math.sqrt(d) - int(b) ) / 2 * int(a))  #Squares d and solves rest of equation
