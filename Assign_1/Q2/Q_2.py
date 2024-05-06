# i) Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# ii) Binary Search
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# iii) Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# iv) Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# v) Quick Sort
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Quick Sort:")
    quick_sort(arr, 0, n-1)
    print("Sorted array is:", arr)

    arr = [64, 25, 12, 22, 11]
    print("\nSelection Sort:")
    selection_sort(arr)
    print("Sorted array is:", arr)

    arr = [12, 11, 13, 5, 6, 7]
    print("\nMerge Sort:")
    merge_sort(arr)
    print("Sorted array is:", arr)

    arr = [2, 3, 4, 10, 40]
    x = 10
    print("\nBinary Search:")
    result = binary_search(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

    arr = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
    x = 'a'
    print("\nLinear Search:")
    print("Element found at index "+str(linear_search(arr,x)))

if __name__ == "__main__":
    main()