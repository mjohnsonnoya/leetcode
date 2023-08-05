class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tdict = defaultdict(int)
        for c in t:
            tdict[c] += 1
        windowdict = defaultdict(int)
        neededchars = len(tdict)
        windowchars = 0
        min_len = float('inf')
        min_window = ""
        l,r = 0,0
        while r < len(s):
            windowdict[s[r]] += 1
            if s[r] in tdict and windowdict[s[r]] == tdict[s[r]]:
                windowchars += 1
            while l <= r and windowchars == neededchars:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                windowdict[s[l]] -= 1
                if s[l] in tdict and windowdict[s[l]] < tdict[s[l]]:
                    windowchars -= 1
                l+=1
            r +=1

        return min_window












        
        # r = len(s) - 1
        # while l <= r and ((s[l] not in tdict or s[r] not in tdict) or all(windowdict[c] >= tdict[c] for c in tdict)):
        #     while l <= r and (s[l] not in tdict or s[r] not in tdict):
        #         if s[l] not in tdict:
        #             windowdict[s[l]] -=1
        #             l += 1
        #         if s[r] not in tdict:
        #             windowdict[s[r]] -=1
        #             r -= 1
        #     while l <= r and all(windowdict[c] >= tdict[c] for c in tdict):
        #         if windowdict[s[l]] > tdict[s[l]]:
        #             windowdict[s[l]] -=1
        #             l += 1
        #         else:
        #             # print(s[l:r+1])
        #             windowdict[s[r]] -=1
        #             r -= 1
        # res = s[l:r + 1]
        # return res


        # tdict = defaultdict(int)
        # minimumwindowlen = 10**5
        # minimumwindow = ""
        # for letter in t:
        #     tdict[letter] += 1
        # for i in range(len(s)):
        #     for j in range(i+1,len(s) + 1):
        #         isvalid = True
        #         sdict = defaultdict(int)
        #         for k in s[i:j]:
        #             sdict[k] += 1
        #         for key, value in tdict.items():
        #             if sdict[key] < value:
        #                 isvalid = False
        #         if isvalid == True:
        #             if (j-i) < minimumwindowlen:
        #                 minimumwindowlen = j - i
        #                 minimumwindow = s[i:j]
        # return minimumwindow




