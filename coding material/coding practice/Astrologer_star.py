num=int(input("Enter the interger  : "))
a=int(input("Enter the Trur(1)/False(0): "))

if a==True:
    for i in range(1,num+1,):
        print('*'*i)
elif a==False:
    for i in range(num):
        print('*'*(num-i))        
