a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.symmetric_difference(b))
#or
print(a^b)

#
A = {10, 20}
B = {10, 20, 30, 40}

print(A.issubset(B))


a = {10, 20, 30, 40}
b = {10, 20}

print(a.issuperset(B))


a = {10, 20}
b = {30, 40}

print(a.isdisjoint(B))