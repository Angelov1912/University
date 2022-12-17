#Problem: Converting Celsius temperatures to fahrenheit temperatures

#Initialise a list with Celsius temperatures
celsius_temp = [22, 25, 32, 35, 40]

#Initialise an empty list for the converted fahrenheit temperatures
fahrenheit_temp = []

#Do the conversion
for celsius in celsius_temp:
    fahrenheit = celsius * 1.8 + 32
    fahrenheit_temp = fahrenheit_temp + [fahrenheit]

#Print the result
print("The temperatures in Fahrenheit are: ", fahrenheit_temp)
