def ejemplo (param1,param2):
	print (param1)
	return param2

def ejemplo2 (param1="hola",param2=5):
	print(param1)
	return param2 

def ejemplo3 (*args): #conjunto de tuplas o argumentos
	print (args)


def ejemplo4(**kwargs): #Regresas los valores de un diccionario de datos
	print(kwargs)


class MyClass:

	def __init__ (self):
		self.name = name

	def my_method(self):
		return self.name

	def _my_private_method(self): ##Si se desea tener un metodo privado, se pone con un '_' al inicio
		print("im private")

class MyChildClass(MyClass):
	pass
