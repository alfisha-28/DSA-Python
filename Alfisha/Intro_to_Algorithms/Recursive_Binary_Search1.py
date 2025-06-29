def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2

        if lst[midpoint] == target:
            return True
        elif lst[midpoint] < target:
            return recursive_binary_search(lst[midpoint + 1:], target)
        else:
            return recursive_binary_search(lst[:midpoint], target)

def verify(found):
    if found:
        print("Target is found in the list")
    else:
        print("Target is not found in the list")

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = recursive_binary_search(lst, 6)
verify(result)

result = recursive_binary_search(lst, 10)
verify(result)
