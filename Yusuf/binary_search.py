
def binary_search(number,target):
    first = 0
    #number 0
    last = len(number) - 1
    # length is 9 (1-10 but is array) and subtracting one means last is 8

    while first <= last:
        midpoint = (first + last)//2
        # first + last will be 8 and divide by 2 will be 4 

        if number[midpoint] == target: #index of number[4] is 5 according to the input we have given
            return midpoint
        elif number[midpoint] < target: #if target is greater than 5 then assigning first as 6 means first =  midpoint +1
            first = midpoint +1
        else:
            last = midpoint - 1 #if target is less than 5 then assigning last as 4 means last =  midpoint - 1
    
    return None

def verify (index):
    if index is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 10)
verify(result)

print("Program complete")
