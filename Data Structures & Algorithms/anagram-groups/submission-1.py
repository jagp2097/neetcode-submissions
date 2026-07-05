class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: list[str] = []

        while len(strs) > 0:
            str_first = strs.pop(0)
            sublist: list[str] = []
            sublist.append(str_first)

            for str_second in reversed(strs):    
                str_f = list(str_first.lower())
                str_s = list(str_second.lower())

                if not len(str_f) == len(str_s):
                    continue

                anagram_indicator = True

                for letter in str_f:
                    if not letter in str_s:
                        anagram_indicator = False
                        break
                    else:
                        str_s.remove(letter)
                
                if anagram_indicator:
                    sublist.append(str_second)
                    strs.remove(str_second)
            
            anagrams.append(sublist)
        
        return anagrams

                



