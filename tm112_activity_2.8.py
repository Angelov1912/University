#problem: Obtain temperatures that are outside the range


#Input: Initialise a list of daily temperatures in Celsius
daily_temperatures = [25, 27, 31, 33, 28, 29]

#Output: Initialise an empty list for the days with  temperatures outside the range
hot_days = []

for temperature in daily_temperatures:
    if temperature > 30:
        hot_days = hot_days + [temperature]

print("The hot days had the following temperatures: ", hot_days)
