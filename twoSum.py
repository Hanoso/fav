"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums) # 列表长度
        if l == 1:
            if target == nums[0]:
                return [0]
        if l == 2:
            if target in nums:
                return [nums[target].index]
            elif nums[0] + nums[1] == target:
                return [0,1]
        if l > 2 :
            i = 0
            while i < l:
                if i != l-1:
                    for m in nums[i+1:]:
                        if nums[i] + m == target:
                            if m in nums[:i+1]:
                                return [i,nums.index(m, nums.index(m)+1)]
                            else:
                                return [i,nums.index(m)]
                i += 1
        return None

nums = [2, 7, 11, 15]
# nums = [3, 2, 3, 4, 5, 8, 4]
target = 9
a = Solution()
out = a.twoSum(nums,target)
print('结果：',out)
