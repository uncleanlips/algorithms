# Linear Search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

# Iterative Binary Search
def binarySearchIterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Recursive Binary Search
def binarySearchRecursive(arr, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return binarySearchRecursive(arr, target, low, mid - 1)
        else:
            return binarySearchRecursive(arr, target, mid + 1, high)

if __name__ == '__main__':
    arr = list(map(int, input('Enter a sorted array: ').strip().split(' ')))
    target = int(input('Enter target element: '))
    print(binarySearchIterative(arr, target))
    print(binarySearchRecursive(arr, target, 0, len(arr) - 1))
