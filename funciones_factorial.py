class Factorial:

	def __init__(self, num):
		self.num = num
	
	def __calcula(self, n):
		if (n==1):
			return n

		else:
			return n*self.__calcula(n-1)		

	def imprime(self):
		print(self.__calcula(self.num))

fact = Factorial(8)
fact.imprime()
#print(fact.__calcula(5))

