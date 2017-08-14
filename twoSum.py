class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        indice=[]
        for x in nums:
            numsnew=nums*1
            numsnew.remove(x)
            for y in numsnew:
                if x==target-y:
                    result.append(x)
        resultnew=list(set(result))
        for z in resultnew:         
            ind=[i for i,a in enumerate(nums) if a==z]
            indice.append(ind)
        return indice
    #previously have issue with input[3,2,4],6 [3,3],6
    
