c=int(input("entere the number: "))
d=bin(c)
count=0
list1=""
for i in d:
    if i=='1':
        count+=1
    else:
        list1+=str(count)
        int(count)
        count=0
print(d)        
print(list1)
print("maximum, the consective 1's  ocuure are : ",max(list1))   






