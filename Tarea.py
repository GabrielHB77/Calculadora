numero1 = (int(input("Ingrese el numero 1: ")))
numero2 = (int(input("Ingrese el numero 2: ")))

suma = numero1+numero2

print("El resultado de la suma es: ",suma)

numero1 = (int(input("Ingrese el numero 1: ")))
numero2 = (int(input("Ingrese el numero 2: ")))

resta = numero1-numero2

print("El resultado de la resta es: ",resta)

numero1 = (int(input("Ingrese el numero 1: ")))
numero2 = (int(input("Ingrese el numero 2: ")))

multiplicacion = numero1*numero2

print("El resultado de la multiplicacion es: ",multiplicacion)

numero1 = (int(input("Ingrese el numero 1: ")))
numero2 = (int(input("Ingrese el numero 2: ")))

division = numero1/numero2

print("El resultado de la division es: ",division)\


numero = int(input("Ingrese un numero: "))

def numeroPrimo(numero):
    
    contador=0
    resultado=True

    for i in range (1, numero+1):
        if(numero/i==0):
            contador+=1
        if(contador>2):
            resultado=False
            break
        return resultado
if(numeroPrimo(numero)==True):
    print("El numero es primo")
else:
    print("El numero no es primo")



def invierteNumero(numero):

    numeroInvertido = 0

    while numero > 0:

        digito = numero % 10

        numeroInvertido *= 10

        numeroInvertido += digito

        numero //= 10

    return numeroInvertido

    

def esPalindromo(numero):

    numeroInvertido = invierteNumero(numero)

    return numero == numeroInvertido



numero=int(input("Ingrese un número: "))

numero = abs(numero)

if esPalindromo(numero):

    print("El número es palíndromo")

else:

    print("El número no es palíndromo")

