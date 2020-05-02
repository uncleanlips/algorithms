input_str_1 = 'holyscripturesareAble'
input_str_2 = "holyScripturesreable"
input_str_3 = 'holyscripturesareable'

# Iterative
def findUppercaseIterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"

# Recursive
def findUppercaseRecursive(input_str, idx = 0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
    return findUppercaseRecursive(input_str, idx+1)

if __name__ == '__main__':
    print(findUppercaseIterative(input_str_1))
    print(findUppercaseIterative(input_str_2))
    print(findUppercaseIterative(input_str_3))

    print(findUppercaseRecursive(input_str_1))
    print(findUppercaseRecursive(input_str_2))
    print(findUppercaseRecursive(input_str_3))
