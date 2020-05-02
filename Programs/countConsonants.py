input_str_1 = "abc de"
input_str_2 = "holyscripturesareable"

# Iterative
vowel = "aeiou"

def countConsonantsIterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count += 1
    return count

# Recursive
def countConsonantsRecursive(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1 + countConsonantsRecursive(input_str[1:])
    else:
        return countConsonantsRecursive(input_str[1:])

print(countConsonantsIterative(input_str_1))
print(countConsonantsIterative(input_str_2))
print(countConsonantsRecursive(input_str_1))
print(countConsonantsRecursive(input_str_2))
