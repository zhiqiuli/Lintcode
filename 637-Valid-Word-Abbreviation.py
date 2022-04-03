class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        p = 0
        res = []
        while p < len(abbr):
            if abbr[p].isalpha():
                res.append(abbr[p])
                p += 1
                continue
            else:
                curr = ''
                while p < len(abbr) and abbr[p].isdigit():
                    # take care of case
                    # 'a' and '01'
                    if not curr and abbr[p] == '0':
                        return False
                    curr += abbr[p]
                    p += 1
                res.append(int(curr))
        
        # generate a list like ['i', 12, 'i', 'z', 4, 'n']
        index = 0
        for c in res:
            if type(c) is str:
                if c != word[index]:
                    return False
                index += 1
            else:
                index += c

        # number of abbr shoud always match original word
        return index == len(word)
