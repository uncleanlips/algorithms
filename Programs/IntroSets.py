def average(array):
    length = len(set(array))
    result = 0
    for i in set(array):
        result += i
    return result / length


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)