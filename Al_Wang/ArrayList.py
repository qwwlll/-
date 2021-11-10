###leetcode 15 sum of the three numbers
### sort 加双指针
class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        num.sort()
        n = len(num)
        res = []
        if n < 3:
            return []
        for a in range(n-2):
            if a > 0 and num[a] == num[a-1]: ## 去重
                continue
            target = 0 - num[a] ### num1 + num2 + num3 ==0 的问题转化成 num2 + num3 = - num1
            c = n - 1 ## 第二指针在尾部
            for b in range (a+1, n-1 ):
                if b > a + 1 and num[b] == num[b-1]: ## 去重
                    continue
                while b < c and num[b] + num[c] > target:
                    c = c - 1 ## 第二指针往前移动
                if b == c :
                    break
                if num[c] + num[b] == target:
                    res.append([num[a], num[b], num[c]])
        return res

###leetcode 169  MajorityNumber
### 暴力解法 （大数量集时超时） O(n^2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_lt = []
        count = 0
        for i in range(n):
            for j in range (n):
                if nums[i] == nums[j]:
                    count = count + 1
            count_lt.append(count)
            count = 0
        return nums[count_lt.index(max(count_lt))]

###other way: O(1)
##多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。排序的时候，中间数一定是众数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

###leetcode 41 missing postive number
### hash table used.