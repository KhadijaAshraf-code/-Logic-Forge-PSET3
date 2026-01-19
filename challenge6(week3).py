def find_repeated_identifier(nums):
    freq = {}
    n = len(nums) // 2

    for x in nums:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == n:
            return x




