input_str = "holyscripturesareable"

print(len(input_str))

# Iterative
def IterativeStrLen(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

print(IterativeStrLen(input_str))

# Recursive
def RecursiveStrLen(input_str):
    if input_str == '':
        return 0
    return 1 + RecursiveStrLen(input_str[1:])

if __name__ == '__main__':
    print(RecursiveStrLen(input_str))
