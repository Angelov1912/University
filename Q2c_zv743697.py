#Problem: Convert binary to decimal
#Input: The binary code correspondin to PI(K7544593)
binary_digits = [1, 1, 0, 0, 1, 1]
#Input: Powers of two for converting to decimal
weightings = [32, 16, 8, 4, 2, 1]
#Output: The converted binary code in decimal values
decimal_values = []

for i in range(len(weightings)):
    if binary_digits[i] > 0:
        decimal = weightings[i]
        decimal_values = decimal_values + [decimal]

print(decimal_values)
#Set the aggregator to 0
converted = 0
for values in decimal_values:
    converted = converted + values

print(converted)
