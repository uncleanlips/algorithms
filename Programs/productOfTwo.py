x = 5
y = 3

# Recursive
def ProdectOfTwo(x, y):

    # This cuts down on the total number of recursive calls:
    if x < y:
        return ProdectOfTwo(y, x)
    if y == 0:
        return 0
    return x + ProdectOfTwo(x, y - 1)

print(x * y)
print(ProdectOfTwo(x, y))
