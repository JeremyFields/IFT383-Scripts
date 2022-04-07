# write a python script to compute the minimum, maximum and average value
# of the following list. Do not use loops or conditionals, use data structure
# functions from lecture

# create list with given numbers
numbers = [38, 120, 43, 2600, 1024, 768, 1920, 1080, 2560, 1440, 93, 32, 64]
# find minimum within the list
minimum = min(numbers)
# find maximum within the list
maximum = max(numbers)
# calculate the average by adding numbers / length of list (amount of numbers)
average = sum(numbers) / len(numbers)

# print the min, max, and average
print(("MIN = %i") % minimum)
print(("MAX = %i") % maximum)
print(("AVG = %.2f") % average)