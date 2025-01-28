"""Hash Set

- Hash Set does not allow duplicate values.
- Sets in Python are unordered, because the elements are stored based on their hash values, not 
by their order of insertion.
- Sets use hashing to provide fast lookups, insertions, and deletions.
- Hash Set are Mutable. You can add or remove elements after creating the set.
- Sets can only store hashable elements, like numbers, strings, and tuples (not lists or dictionaries)."""

mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(mySet)