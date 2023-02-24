def is_anagram(s1,s2):

    if len(s1)!=len(s2):

        return False
    
    count={}

    for char in s1:

        if char in count:

            count[char]+=1
        else:
            count[char]=1

    for char in s2:

        if char in count:
            
            count[char]-=1
        else:

            count[char]=1

    for k in count:

        if count[k]!=0:

            return False
    return True



s1="dog"
s2="god"

result=is_anagram(s1,s2)

print(result)

