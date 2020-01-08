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