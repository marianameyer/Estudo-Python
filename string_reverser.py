# Function to Reverse a String

def reverse(s):

  length = len(s)  # Length of the string
  spaces = [' ']  # A list with space - we're not using split() here!
  words = []  # A empty list for saving the words
  i = 0  # A index

  while i < length:
    if s[i] not in spaces:  # If the character is not a space
      word_start = i  # The index where the word start

      while (i < length) and (s[i] not in spaces):  # While is a word
        i += 1  # Go to the next index

    i += 1

  return ''.join(reversed(s))  # Join the words (with reversed letters)

# Example
print(reverse('Python is the best of all!'))
