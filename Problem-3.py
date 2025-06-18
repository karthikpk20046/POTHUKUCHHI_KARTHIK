# Problem-3.py

def generate_odd_series_upto(n: int):
    result = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            result.append(i)
    print(', '.join(map(str, result)))

# Example usage:
generate_odd_series_upto(11)

# OUTPUT: 1,3,5,7,9,11
