# Given an array, what is the most frequently occuring element?

# Function that reads a list and return the most frequent element
def most_freq(list):
  count = {}  # A dict that will reserve the frequencies
  max_count = 0  # The frequency of items
  max_item = None  # The most frequent item

  # Reading the list
  for i in list:
    if i not in count:  # If is not in the dict, create one
      count[i] = 1

    else:
      count[i] += 1  # If it's in the dict, add one

    if count[i] > max_count:
      max_count = count[i]
      max_item = i

  # Return the most frequent element
  return max_item

print(most_freq([1,3,3,3,2,1,1,1]))
