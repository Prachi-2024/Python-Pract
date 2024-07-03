# Python program showing
# how MRO works

class A:
	def __init__(self,name,lname):
		self.name=name
		self.lastname=lname
		print(" In class A")
		print(name,lname)
		
	def rk(self):
		print(" In class B", self.name)
		
	def pk(self):
		self.rk()
		
class B(A):
	def rk(self):
		print(" In class B")
class C(A):
	def rk(self):
		print("In class C")

# classes ordering
class D(B, C):
	pass
	
# r = D()
# r.rk()
a=A("prachi","shah")
a.rk()