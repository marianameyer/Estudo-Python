# Function that returns an array of elements that are common to two different arrays.
# The result is a sorted array (ascending order).

# Example: arr1 = [1,3,4,6,7,9] and arr2 = [1,2,4,5,9,10]. The result is
# arr_r = [1,4,9]

def commom_elements(arr1,arr2):

  # Defining the index of the arrays
  p1 = 0
  p2 = 0

  # Ordered array with commom elements
  result = []

  # The loop will works throught the arrays
  while p1 < len(arr1) and p2 < len(arr2):

    # When the elements are common: add to result array and move on
    if arr1[p1] == arr2[p2]:
      result.append(arr1[p1])
      p1 += 1
      p2 += 2

    # When elements are different
    elif arr1[p1] > arr2[p2]:
      p2 += 1

    else:
      p1 += 1

  return result

# Example:
arr1 = [1,3,4,6,7,9]
arr2 = [1,2,4,5,9,10]

print(commom_elements(arr1,arr2))
