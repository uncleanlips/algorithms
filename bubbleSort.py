def bubbleSort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):

            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp

if __name__ == '__main__':
    arr = list(map(int, input('Enter elements: ').strip().split(' ')))
    bubbleSort(arr)
    print('Sorted array is : ', end='')
    for i in range(len(arr)):
        print(arr[i], end=' ')
