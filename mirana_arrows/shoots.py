def max_arrows(n, k, arrows):
    """
    The max_arrows function uses a sliding window approach to efficiently find the maximum number of arrows that can be released without exceeding the maximum cumulative distance K. Here's how it works:
    """
    max_arrows_count = 0
    current_distance = 0
    left = 0

    for right in range(n):
        current_distance += arrows[right]

        while current_distance > k:
            current_distance -= arrows[left]
            left += 1

        max_arrows_count = max(max_arrows_count, right - left + 1)

    return max_arrows_count
