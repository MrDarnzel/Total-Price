Temp_Celcius = input(" What is the Temperature in Celcius? ") #Asks the user for Temperature in Celcius
float(Temp_Celcius)  #Converts to Float
print(Temp_Celcius)  #Prints Celcius Temperature


Temp_Fahrenheit = (((float(Temp_Celcius) * 9) / 5) + 32)            #Takes C and converts into F
print(" The temperature in Fahrenheit is " + str(Temp_Fahrenheit))  #Prints your temperature
