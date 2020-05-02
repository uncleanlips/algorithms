def nextNumber(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

if __name__ == '__main__':
    s = '1'
    n = int(input('How many sequences: '))
    for i in range(n - 1):
        s = nextNumber(s)
        print(s)
