'''
P
Py
Pyt
Pyth
Pytho
Python'''


# v="Python"

# for i in range(len(v)):
#     print(v[:i+1])



'''
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1'''

# k=6
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(k,end=" ")

#     k-=1
#     print()    


'''
*
* *
* * *
* * * *
* * * * *
'''

# num=5

# for i in range(1,num+1):
#     print("* "*i)


'''
        *
      * *
    * * *
  * * * *
* * * * * 

'''

# def pattrn(num):

#     for i in range(1,num+1):
#         for j in range(num-i):
#             print(" ",end=" ")
#         for k in range(i):
#             print("* ",end="")    
#         print()    

# num=5
# pattrn(num)


'''
    *    
   * *
  * * *
 * * * *
* * * * *  '''

# def pattrn(num):
    
#     for i in range(1,num+1):
#         for j in range(num-i):
#             print(" ",end="")
#         for k in  range(i):
#             print("*",end=" ")
#         print()

# num=5
# pattrn(num)



'''
* * * * * * * * * 

  * * * * * * *

    * * * * *

      * * *

        *
       '''
# def pater1(num):
#     k=0
#     for i in range(num,0,-1):
#         if i%2!=0:
#             for m in range(k):
#                 print(" ",end=" ")
#             k+=1    
#             for j in range(i):
#                 print("* ",end="")
#             print("\n")

# num=9
# pater1(num)     
#        

'''
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1
128 64 32 16 8 4 2 1'''

# for i in range(8):
#     a=2**i
#     while a%2==0:
#         print(a,end=" ")
#         a=a//2
#     print("1")         



'''
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
'''

# for i in range(1,8):
#       for j in range(1,i+1):
#             print(i*j,end=" ")
#       print()      
            
      
'''
        1 
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''

# def pattrn(num):
#   for i in range(1,num+1):
#       a=1
#       for j in range(num-i):
#         print(" ",end=" ")
#       for k in range(i):
#         print(a,end=" ")
#         a+=1    
#       print()    

# num=5
# pattrn(num)

'''
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
'''

# for i in range(1,6):
#       for j in range(1,6):
#             if i>j:
#                   print(i,end=" ")
#             else:
#               print(i,end=" ")
#               i+=1
#       print()              
      
      
'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''

# def Odd_no(num):
#       a=1
#       for i in range(1,num):
#             for j in range(i):
#                   print(a,end=" ")
#             a+=2
#             print()      
            
# num=5
# Odd_no(num+1)


'''
6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

# def pattern(num):
#       for i in range(num,0,-1):
#             for j in range(i,0,-1):
#               print(j,end=" ")
#             print()  

# num=6
# pattern(num)              


'''
1
2 3 4
5 6 7 8 9
'''

# def pattern1(num):
#       a=1
#       for i in range(1,num+1):
#             while True:
#                   if a==i**2: 
#                     print(a)
#                     a+=1
#                     break
#                   print(a,end=" ")
#                   a+=1                        
# num=3
# pattern1(num)


'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''                

# def pattern2(num):
#       # print("0",end=" ")
#       for i in range(num,0,-1):
#             for j in range(i+1):
#                   print(j,end=" ")
#             print()      
                
# num=5
# pattern2(num)



'''
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

# def pattern3(num):
#       for i in range(num+1,0,-1):
#             for j in range(i):
#                   print(i,end=" ")
#             print()

# num=5
# pattern3(num)            

'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''

# def patter5(num):
#       for i in range(1,num+1):
#             for j in range(num+1-i):
#                   print(i,end=" ")
#             print()

# num=5
# patter5(num)                

'''

A
A B
A B C
A B C D
A B C D E
'''  

# def patten6(num):
#   for i in range(num+1):
#         var=65
#         for j in range(i):
#               print(chr(var),end=" ")
#               var+=1
#         print()      

# num=5
# patten6(num)

'''
K
K K
K K K
K K K K
K K K K K
'''
# def patten6(num,var):
#   for i in range(num+1):
#         for j in range(i):
#               print(chr(var),end=" ")
#         print()      

# num=5
# var=ord("K")
# patten6(num,var)


'''
A
B C
D E F
G H I J
K L M N O
'''

# def patten6(num,var):
#   for i in range(num+1):
#         for j in range(i+1):
#               print(chr(var),end=" ")
#               var+=1
#         print()      

# num=5
# var=ord("A")
# patten6(num,var)


'''
A 
B B
C C C
D D D D
E E E E E
'''

# def patten6(num,var):
#   for i in range(num+1):
#         for j in range(i+1):
#               print(chr(var),end=" ")
#         print()
#         var+=1      

# num=5
# var=ord("A")
# patten6(num,var)


'''
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
'''
            
def pascal_tringle(num):
    a=[[] for i in range(num)]

    for i in range(num):
        for j in range(i+1):
            if j<i:
                if j==0:
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])

            elif(i==j):
                a[i].append(1)
    return a

num=5
var=pascal_tringle(num)

for i in var:
    for k in range(num-len(i)):
        print(" ",end="")
    for j in i:
        print(f"{j}",end=" ")
    print() 
    
