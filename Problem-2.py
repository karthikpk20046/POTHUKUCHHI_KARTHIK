def odd(n: int):
    ans = []
    for i in range(n):
        ans.append(2 * i + 1)
    print(', '.join(map(str, ans)))

# Example
odd(5)

# OUTPUT: 1,3,5,7,9
