import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# sum of 75 sample values 
print("Sum of 75 sample values:", sum(vals_sample))

# average of 75 sample values
print("AVG of 75 sample values:", statistics.mean(vals_sample))

# median of 75 sample values
print("Median of 75 sample values:", statistics.median(vals_sample))

print ("\n")
# superset of 200 values

print("Average of 200 values:", statistics.mean(vals_choices))

print("Median of 200 values:", statistics.median(vals_sample))

print("Mode of 200 values:", statistics.mode(vals_sample))

print("Standard Dev of 200 values:", statistics.variance(vals_choices))

print("\n")
# modeling a random circle
print("Modeling a random circle:")

area = pi * radius ** 2

print("Radius =", radius,
      "area=", math.ceil(area),
      "(rounded up to the nearest integer)")

print("Radius =", radius,
      "area =", math.ceil(area),
      "(rounded down to the nearest integer)")

