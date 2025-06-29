def recursive_binary_search(lst, target, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return None

    mid = (start + end) // 2

    if target == lst[mid]:
        return mid
    else:
        if target < lst[mid]:
            return recursive_binary_search(lst, target, start, mid-1)
        else:
            return recursive_binary_search(lst, target, mid+1, end)
        
def verify (index):
    if index is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in the list")

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = recursive_binary_search(lst, 6)
verify(result)

result = recursive_binary_search(lst, 10)
verify(result)


