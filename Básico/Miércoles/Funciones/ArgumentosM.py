'''
def alfa(a,b,*args):
	print(a)
	print(b)
	print(c)
	#return()

print(alfa(1,2,3,4,5,6,7,8,9))
'''
def beta(a,b,**kwargs):
	print(a)
	print(b)
	print(kwargs)

print(beta(1,2,c=3,d=4,e=5))