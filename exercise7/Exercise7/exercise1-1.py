from operations import *

a, b = (10, 20)

print("{} + {} = {}".format(a, b, sum(a, b)))
print("{} - {} = {}".format(a, b, subtract(a, b)))
print("{} * {} = {}".format(a, b, product(a, b)))
print("{} / {} = {}".format(a, b, division(a, b)))
