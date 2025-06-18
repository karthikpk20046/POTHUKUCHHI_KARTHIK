def generate_odd_series(n: int):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    print(', '.join(map(str, result)))

# Example
generate_odd_series(5)
