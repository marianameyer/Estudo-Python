# Given a string, are all characters unique?
# The function bellow will return True or False
# Using Built-in functions

# Creating the function
def unique(s):

  # Removing spaces
  s = s.replace(' ','')

  # If the length of the set is equal the length of the string s, s is unique
  return len(set(s)) == len(s)

# Example 1:
print(unique('a b cdf'))

# Example 2:
#print(unique('aa bv mheffou n n'))
