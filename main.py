import random

def fill():
	k1=[]
	k2=[]
	for i in range(10):
		k1.append(k2)
		k2.clear()
		for j in range(10):
			
			n=random.randint(-9,9)
			k2.append(n)
			
	return k1

def sum(m1,m2):
	if len(m1)!=len(m2) and len(m1[0])!=len(m2[0]):
		print('можно складывать только массивы одной размерности')
		exit()
	r1=[]
	r2=[]
	for i in range(len(m1)):
		r1.append(r2)
		r2.clear()
		for j in range(len(m1[i])):
			n=m1[i][j]+m2[i][j]
			r2.append(n)
	return r1
			
m1=fill()
m2=fill()
m3=sum(m1,m2)
print(m1)
print()
print(m2)
print()
print(m3)
