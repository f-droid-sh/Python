num1 = float(input("Dime un primer número --> "))
print("")
num2 = float(input("Dime un segundo numero --> "))
print ("")
num1 = num1%2
num2 = num2%2
if num1==0 and num2==0:
    print("Los dos numeros son pares")
elif num1==0:
    print("El primer numero es par")
elif num2==0:
    print("El segundo numero es par")
else
    print("Los numeros son impares")