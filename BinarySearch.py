def b_search(arr, key):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return - 1

if __name__ == "__main__":
    arr = [10, 20,30 ,40 ,50, 60, 70, 80]
    key = 75
    index = b_search(arr, key)
    print(index)
