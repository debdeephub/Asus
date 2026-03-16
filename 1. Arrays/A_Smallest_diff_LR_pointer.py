class Solution:
    def small(self,aOne,aTwo):
        aOne.sort()
        aTwo.sort()
        idxOne,idxTwo = 0,0
        smallest = float('inf')
        smallestPair = []
        while idxOne < len(aOne) and idxTwo < len(aTwo):
            firstNum = aOne[idxOne]
            secondNum=aTwo[idxTwo]
            diff = abs(firstNum - secondNum)
            if firstNum == secondNum:
                return 0
            elif firstNum < secondNum:
                idxOne+=1
            elif firstNum > secondNum:
                idxTwo+=1
            if smallest > diff:
                smallest = diff
                smallestPair = [firstNum,secondNum]

        return smallestPair

aOne = [-1,5,10,20,28,3]
aTwo = [26,134,135,15,17]
print(Solution().small(aOne,aTwo))
