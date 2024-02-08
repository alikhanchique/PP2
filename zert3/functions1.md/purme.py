from itertools import permutations

def print_permutations(user_string):
    perms = [''.join(p) for p in permutations (user_string)]
    for perm in perms:
        print(perm)

user_input = input("  ")
print_permutations(user_input)