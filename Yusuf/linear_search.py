
def linear_search(number,target):
    
    for i in range(0, len(number)):
        if number[i] == target:
            return i
    return None

def verify (index):
    if index is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 10)
verify(result)

print("Program complete")
