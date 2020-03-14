import sys

s1 = str(sys.argv[1])
s2 = str(sys.argv[2])

def Mapping(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(set(s1)) != len(set(s2)):
        return False
    hash = {}
    for i in range(len(s1)):
        if s1[i] not in hash:
            hash[s1[i]] = s2[i]
        else:
            if hash[s1[i]] != s2[i]:
                return False
    return True

print(Mapping(s1,s2))
