# Manipulating whitespace using different methods and functions.
name = "     kuwabara nodoka     "
print(name)

name = "     kuwabara\tnodaka     "
print(name)

name = "     kuwabara\nnodaka     "
print(name)

name = "     kuwabara\n\tnodaka     "
print(name)

name = "     kuwabara nodaka     "
print(name.lstrip())
print(name.rstrip())
print(name.strip())