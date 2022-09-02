from functools import reduce

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

sum_lists = reduce(lambda x,y : x + y, nums1+nums2+nums3)

print(sum_lists)