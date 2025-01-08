# Given a string, are all characters unique?
# The function bellow will return True or False

# Creating the functio
def unique(s):

  # Removing spaces
  s = s.replace(' ','')
  # Creating an empty set
  characters = set()

  # Checking if the letter is in the set, if not, add to
  for letter in s:
    if letter in characters:
      return False
    else:
      characters.add(letter)
  return True

# Example 1:
print(unique('a b cdf'))

# Example 2:
#print(unique('aa bv mheffou n n'))
