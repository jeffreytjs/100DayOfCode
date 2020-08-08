# Day 26 - Problem 29

# Challenge
# Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# Sample Input: [-25, -10, -7, -3, 2, 4, 8, 10]
# Sample Output: [[-10, 2, 8], [-7, -3, 10]]


class Zero_Sum:
    def three_sum_zero(self, nums):
        nums = sorted(nums)
        result = []
        current = 0
        while (current < (len(nums) - 2)):
            next, rlimit = current + 1, len(nums) - 1
            while (next < rlimit):
                if ((nums[current] + nums[next] + nums[rlimit]) < 0):
                    next += 1
                elif ((nums[current] + nums[next] + nums[rlimit]) > 0):
                    rlimit -= 1
                else:
                    result.append([nums[current], nums[next], nums[rlimit]])
                    next, rlimit = next + 1, rlimit - 1
                    while (next < rlimit) and (nums[next] == nums[next - 1]):
                        next += 1
                    while (next < rlimit) and (nums[rlimit] == nums[rlimit + 1]):
                        rlimit -= 1
            current += 1
            while (current < (len(nums) - 2)) and (nums[current] == nums[current - 1]):
                current += 1
        return result


zero_sum = Zero_Sum()
print(zero_sum.three_sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))
print(zero_sum.three_sum_zero([-25, -10, -7, -3, 2, 4, 8, 10, 14, -4, 5, -20]))
