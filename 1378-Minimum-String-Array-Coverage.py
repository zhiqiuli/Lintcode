def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        if not tagList:
            return 0
        if not allTags or len(tagList) > len(allTags):
            return -1
        
        n = len(allTags)
        tagList = set(tagList)
        # no repeat in tagList
        cnt = {}
        
        left, right = 0, 0
        min_l = sys.maxsize
        
        for left in range(n):
            while right < n and len(cnt) < len(tagList):
                tag = allTags[right]
                
                if tag in tagList:
                    if tag not in cnt:
                        cnt[tag] = 0
                    cnt[tag] += 1
                    
                right += 1
            
            if len(cnt) == len(tagList):
                min_l = min(min_l, right - left)
        
            del_tag = allTags[left]
            
            if del_tag in cnt:
                cnt[del_tag] -= 1
                if cnt[del_tag] == 0:
                    del cnt[del_tag]
        
        return min_l if min_l != sys.maxsize else -1
