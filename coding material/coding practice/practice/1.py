import time

#Time complexity n**3
def sub_array1(arr,target):
    n=len(arr)
    for i in range (n):                 # n
        for j in range (n+1):           # n
            if sum(arr[i:j])==target:   # n
                return i,j
    return None,None


def sub_array2(arr,target):
    n=len(arr)
    for i in range(n):
        s=0
        for j in range(i,n+1):
            if s==target:
                return i,j
            elif s>target:
                break
            s+=arr[j]
    return None,None

#arr=[7,8,1,2,3,4,9,8]

def sub_array3(arr,target):
    n=len(arr)
    i,j,s=0,0,0

    while i<n and j<n+1:

        if s==target:
            return i,j
        elif s<target:
            s+=arr[j]
            j+=1
        elif s>target:
            s-=arr[i]
            i+=1
    return None,None                



if __name__=='__main__':

    start=time.time()


    test0={
        "input":{"arr":[7,8,1,2,3,4,2,7,8,6,7,1],'target':10},
        "output":(2,6)
    }

    test1={
        "input":{"arr":[1,2,3,4,2,7],'target':10},
        "output":(0,4)
    }
    test2={
        "input":{"arr":[7,8,1,2,3,4],'target':10},
        "output":(2,6)
    }
    test3={
        "input":{"arr":[],'target':10},
        "output":(None,None)

    }

    tests=[test0,test1,test2,test3]

    for i,test in enumerate(tests):
        result=sub_array3(**test["input"])
        print("Test Case #",i)
        print("Expexted output: ",test["output"])
        print("Actual output : ",result)
        print("Pass ",result==test["output"])
        print()

    print("Time required is : ",time.time()-start)    