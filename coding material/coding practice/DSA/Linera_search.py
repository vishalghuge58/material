'''this liner search algorithem is also called as brute force algorithem als'''
# O(n) Complexity

def linear_search(list1,element):

    # print("list1: ",list1)
    # print("elements: ",element)

    position=0    
    
    while len(list1)>=1:

        if list1[position]==element:
    
            return position

        position+=1


        if position==len(list1):
    
            return -1    
    return -1



list_even=[0,2,4,6,8,10]

list_odd=[]

element=5

position=linear_search(list_odd,element)


if position==-1:
    print("The element is not present in list ")
else:
    print(f"The element is  present in list at {position} position")


