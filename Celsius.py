Temp_Celsius = input(" What is the Temperature in Celsius? ") #Asks the user for Temperature in Celsius
float(Temp_Celsius)  #Converts to Float
print(Temp_Celsius)  #Prints Celcius Temperature


Temp_Fahrenheit = (((float(Temp_Celsius) * 9) / 5) + 32)            #Takes C and converts into F
print(" The temperature in Fahrenheit is " + str(Temp_Fahrenheit))  #Prints your temperature
