def linear_search(lst, target):
    """Returns the index position of the target if found, else returns -1"""

    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in the list")

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = linear_search(lst, 6)
verify(result)

result = linear_search(lst, 12)
verify(result)

