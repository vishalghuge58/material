'''Find the armstrong  three digit numbers like 153=1**3+5**3+3**3  between '''

# number that is the sum of its own digits each raised to the power of the number of digits.





# for num in range(100,1000):
#     low = num%10
#     mid=num//10%10
#     high=num//100

#     if num==low**3 + mid**3 + high**3:
#         print(num)


       

'''The following Python program determines whether the integer entered is a Narcissistic / Armstrong number or not.'''


def no_of_digits(num):
    i = 0
    while num > 0:
        num //= 10
        i+=1

    return i

def required_sum(num):
    i = no_of_digits(num)
    s = 0
    
    while num > 0:
        digit = num % 10
        num //= 10
        s += pow(digit, i)
        
    return s


num = int(input("Enter number:"))
s = required_sum(num)
     
if s == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")







# num = int(input("Enter a number:"))
# order = len(str(num))  #153 >> 3          
# sum = 0                        
# temp = num              #num = 153

# while(temp>0):   
#     digit = temp%10   #153%10 >> 3    
#     sum += digit**order   #3**3 >> 27   + 125 + 1          
#     temp //= 10           #153 //10 >> 15 
    
# if(num==sum):
#     print(num,"is an Armstrong number")
# else:
#     print(num,"is not an Armstrong number")