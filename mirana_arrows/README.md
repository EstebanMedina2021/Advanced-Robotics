# Mirana's Archer Challenge

## Problem Statement

In the world of Mirana’s fantastic adventures, the brave archer found herself facing a great challenge. She has N arrows, each of which has a defined distance it can fly. Mirana is skilled with the bow and has extensive shooting experience, but she needs to know the maximum number of arrows she can release to avoid peril. Mirana can start releasing arrows from any index and take the next arrow from the list. She starts from the chosen index j and shoots arrow j to the distance Aj. After that, when the arrow reaches its target, she takes the next arrow with index j + 1 and shoots it to the distance Aj+1, and so on until the last arrow with index N. However, Mirana cannot take the next arrow until the current one reaches its target. However, there is a limitation: if the total distance the arrows fly exceeds K, Mirana will perish. Your task is to find the maximum number of arrows Mirana can release without risking her life.

## Inputs

- The first line contains two integers N and K, where N is the number of arrows and K is the maximum cumulative distance the arrows can fly.
- The next line contains N integers Ai representing the distances the arrows can fly.

## Outputs

- A single integer - the answer to the problem, the maximum number of arrows Mirana can release to avoid peril.

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ K ≤ 10^9
- 1 ≤ ∥Ai∥ ≤ 10^9

## Examples

### Sample 1:

Input:
3 3
1 2 3

Output:
2


## Usage

You can use this algorithm to determine the maximum number of arrows Mirana can release without exceeding the maximum cumulative distance allowed. To use it in your project, follow these steps:

1. Import the `max_arrows` function from the provided code.
2. Provide the values for `N`, `K`, and `Ai`.
3. Call `max_arrows(N, K, Ai)` to get the maximum number of arrows Mirana can release.

## Implementation Details

The algorithm to solve this problem is implemented in Python. It uses a sliding window approach to efficiently find the maximum number of arrows that can be released without exceeding the maximum cumulative distance K.

## Algorithm

The `max_arrows` function uses a sliding window approach to efficiently find the maximum number of arrows that can be released without exceeding the maximum cumulative distance `K`. Here's how it works:

1. **Initialize variables:**
   - `max_arrows_count` to keep track of the maximum number of arrows.
   - `current_distance` to track the cumulative distance of arrows released.
   - `left` and `right` pointers to maintain the sliding window.

2. **Iterate through the arrow distances using the `right` pointer:**
   - Add the distance of the current arrow to `current_distance`.

3. **While `current_distance` exceeds `K`:**
   - Increment the `left` pointer and subtract the distance of the arrow at the `left` position from `current_distance`.
   
   - This ensures that the cumulative distance does not exceed the maximum allowed.

4. **Update `max_arrows_count` with the maximum of its current value and the length of the sliding window (`right - left + 1`):**
   
   - This step keeps track of the maximum number of arrows that can be released without exceeding `K`.

5. **Repeat steps 2-4 until all arrows have been considered.**

6. **Return `max_arrows_count` as the result.**

This sliding window approach efficiently calculates the maximum number of arrows that can be released while maintaining Mirana's safety within the specified constraints.

## Contributing

Contributions to improve the code or add features are welcome! Please fork the repository, create a new branch, and submit a pull request. Ensure that your code is well-documented and follows good software development practices.

