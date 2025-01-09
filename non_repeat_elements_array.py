# Take a string and return a lis of characters that never repeats

def non_repeating(s):

  # Removing spaces
  s = s.replace(' ','').lower()

  # Character count
  char_count = {}

  # A list of all uniques
  all_uniques = []

  # Filling the dict with the characters
  for c in s:
    if c in char_count:
      char_count[c] += 1
    else:
      char_count[c] = 1

  y = sorted(char_count.items(), key=lambda x: x[1])

  for item in y:
    if item[1] == y[0][1]:
      all_uniques.append(item)
  return all_uniques

# Example 1
print(non_repeating('I Apple Ape Peels'))
