class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        indice=[]
        for x in nums:
            for y in nums:
                if x==target-y:
                    result.append(x)
        for y in result:
            z=nums.index(y)
            indice.append(z)
        return indice
       ##has issue when input[3,2,4],6 
class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        indice=[]
        for x in nums:
            for y in nums:
                if x==target-y and x!=y:
                    result.append(x)
        for y in result:
            z=nums.index(y)
            indice.append(z)
        return indice
