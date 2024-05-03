class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)
        ans = s = 0
        for x in satisfaction:
            s += x
            if s <= 0:
                break
            ans += s
        self.ans = ans

if __name__ == '__main__':
    s = [-1,-8,0,5,-9]
    ss = [4,3,2]
    sss = [-1,-4,-5]

    print(Solution.maxSatisfaction(s))
    print(Solution.maxSatisfaction(ss))
    print(Solution.maxSatisfaction(sss))
