
def recursive_binary_search(number,target):
    if len(number) == 0:
        return False
    else:
        midpoint = len(number) // 2

        if number[midpoint] == target:
            return True
        else:
            if number[midpoint] < target:
                return recursive_binary_search(number[midpoint +1:],target) 
            else:
                return recursive_binary_search(number[:midpoint],target) 
            
def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 10)
verify(result)