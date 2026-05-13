# Lambda function that doubles a value
doubler = lambda n: n *2

# Testing the doubler function
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

#Lambda function that triples a value
tripler = lambda n: n*3

# Testing the tripler function
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# multiplier function
def multiplier (x):
    return lambda n: n * x

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))