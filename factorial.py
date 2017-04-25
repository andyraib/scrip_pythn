num=input("Ingrese un numero : ")
num=int(num)
def cuenta_regresiva(n):
    if n == 1:
           return n
    else:    
           return n*cuenta_regresiva(n-1)
        
print (cuenta_regresiva(num))
