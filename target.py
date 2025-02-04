# Target a number

arr = [2,4,5,5,5,5,5,7,9,9]
target1 = 5
target2 = 3
target3 = 9

def first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return[start, i]
    return[-1, -1]

print(first_and_last(arr, target3))