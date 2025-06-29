def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def verify (index):
    if index is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in the list")

result = binary_search(lst, 6)
verify(result)

result = binary_search(lst, 10)
verify(result)


