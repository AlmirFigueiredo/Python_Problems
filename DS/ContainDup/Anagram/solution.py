t = 'nagaram'
s = 'anagram'
def is_anagram(t,s):
    t = t.lower()
    s = s.lower()
    if len(t)!= len(s):
        return False
    else:
        t_list = list(t)
        s_list = list(s)
        t_list.sort()
        s_list.sort()
        if t_list == s_list:
            return True
        else:
            return False
print(is_anagram(t, s))
    
    