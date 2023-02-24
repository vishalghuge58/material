'''How To Find Factorial & No Of Trailing Zeros In A Factorial Of A Number In Python?'''



num=int(input("Enter the no. : "))
trailing_zeroes=0
i=5
while num//i!=0:
    trailing_zeroes+=int(num/i)
    i=i*5
print(" trailing zeroes are",trailing_zeroes)        




'''************************************************************************************************************************************************************************************************************************************************************************'''



def factorial(number):
    	
    	if number==0 or number==1:
    			return 1
		else:
    
			    return number * factorial(number-1)

def factorialTrailingZeroes(number):
	#fac = factorial(number)
	#print(fac)
	count = 0
	i = 5
	while (number//i !=0):
		count+= int(number/i)
		i = i*5
	return count
	#while (fac%10 ==0):
		#count = count+1
		#fac = fac/10
	#return count 

if __name__ == '__main__':
	number = int(input("Enter a number: \n"))
	#fac = factorial(number)
	#print(f'The factorial is {fac}')
	print(factorialTrailingZeroes(number))