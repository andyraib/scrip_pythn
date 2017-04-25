class Number:
    def __init__(self, number):
        self.number = number
        self.factorial = self.__factorial()

    def __str__(self):
        return str(self.number)

    def __factorial(self):
        num = 1
        number = self.number
        while number >= 1:
            num = num * number
            number = number - 1
        return num

    @property
    def as_dict(self):
        return self.__dict__

    def get_factorial(self):
        print("The factorial of {} is {}".format(
            self.number, self.__factorial()))

    def calculator(self, operation, another_number):

        try:
            another_number = float(another_number)
        except ValueError:
            print("That's not a number!")

        if(operation == 'times'):
                return self.number * another_number
       
	elif(operation == 'plus'):
                return self.number + another_number
        
	elif(operation =='divide'):
                return self.number / another_number
        
	elif(operation == 'minus'):
                return self.number - another_number
        else:
                print("No es un operador valido")


num = Number(10)
print(num.calculator('times',10))

