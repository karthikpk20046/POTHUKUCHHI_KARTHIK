def odd_up(n: int):
    ans = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            ans.append(i)
    print(', '.join(map(str, ans)))

# EXAMPLE
odd_up(11)

# OUTPUT: 1,3,5,7,9,11
