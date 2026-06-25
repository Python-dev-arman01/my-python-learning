#=======================
#=====code1=======
def can(n):
	if n==1:
		return 1
	else:
		return can (n-1)*n
		
print(can(5))
#=======================
#=====code2=======
def can(n):
	if n==1:
		return 1
	else:
		return can (n-1)-n
		
print(can(5))
#=======================
#=====code3=======
def can(n):
	if n==0:
		return 
	print(n)	
	can (n-1)
		
print(can(5))
#=======================
#=====code4=======
def can(n):
	if n==1:
		return 1
	else:
		return can (n-1)+n
		
print(can(5))


