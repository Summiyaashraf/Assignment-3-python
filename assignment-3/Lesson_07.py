# Set Example
numbers = {1, 2, 3, 4}
numbers.add(5)  # Adding an element
print(f"Set: {numbers}")

# Frozenset Example (Immutable Set)
immutable_numbers = frozenset([1, 2, 3, 4])
print(f"Frozenset: {immutable_numbers}")

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Union: {set1 | set2}")         # Union
print(f"Intersection: {set1 & set2}")  # Intersection
