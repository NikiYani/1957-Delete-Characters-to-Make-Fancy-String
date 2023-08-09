class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        counter = 0
        currLetter = s[0]

        for i in range(1, len(s)) :
            if currLetter == s[i] :
                counter += 1
                if counter < 2 :
                    res += s[i]
                else :
                    continue
            else :
                currLetter = s[i]
                res += s[i]
                counter = 0

        return res