def multiple(nums):
    ans = {i: 0 for i in range(1, 10)}
    for num in nums:
        for i in range(1, 10):
            if num % i == 0:
                ans[i] += 1
    print(ans)

# EXAMPLE
input_= [1,2,8,9,12,46,76,82,15,20,30]
multiple(input_)

#  OUTPUT    {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
