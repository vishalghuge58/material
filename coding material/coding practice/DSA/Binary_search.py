''' (Binery Serch Algorithem) The list of element should be sorted order then and the it will work'''
# log(n) Complexity

def Biner_serch(list1,element):
    
    start=0

    end=len(list1)-1

    mid=(start+end+1)//2

    while len(list1)>=1:
        if list1[mid]==element:

            return mid

        elif(list1[mid]>element):

            end=mid-1
        else:
            start=mid+1
    return -1

list_even=[0,2,4,6,8,10]

list_odd=[]

element=5

position=Biner_serch(list_odd,element)


if position==-1:
    print("The element is not present in list ")

else:
    print(f"The element is  present in list at {position} position")