set = {1, 2, 3, 4, 5}
print(set)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a.union(set_b)
print(union)

print(set_a.intersection(set_b))

print(set_a.difference(set_b))

set.add(6)
print(set)

set.remove(1)
print(set)

