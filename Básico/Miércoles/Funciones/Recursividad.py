
'''
# 8! = 8x7x6x5x4x3x2x1
def factorial(num):
	if num<1:
		return 1 
	else:		
		return num*factorial(num-1)

a=int(input("De que numero quieres su facorial"))
print(factorial(a))
'''
def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

var=int(input("De que numero deseas conocer la serie de fibo: "))
print(fibo(var))