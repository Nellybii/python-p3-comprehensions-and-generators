one_to_three = range(1,4)

# A list comprehension uses square brackets
squared_lc = [n ** 2 for n in one_to_three]

# A generator expression uses parentheses
squared_ge = (n ** 2 for n in one_to_three)
for n in squared_lc:
    print(n)

for n in squared_ge:
    print(n)
print(squared_lc)
print(squared_ge)