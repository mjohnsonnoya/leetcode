class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def string_to_dict(s):
            string_dict = {}
            for char in s:
                string_dict[ord(char)] = string_dict.get(ord(char), 0) + 1
            return string_dict
        
        s_dict = string_to_dict(s)
        t_dict = string_to_dict(t)

        return s_dict == t_dict
