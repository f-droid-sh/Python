import os
os.system ("cls")
print("")
print("1) Suma")
print("2) Resta")
print("3) Multiplicación")
print("4) División")
print("")
accion = int(input("Dime que acción quieres tomar --> "))
num1 = float(input("Primer número --> "))
print ("")
num2 = float(input("Segundo número --> "))
print ("")
if accion==1:
    suma=num1+num2
    print(f"El resultado de la suma es {suma}")
if accion==2:
    resta=num1-num2
    print(f"El resultado de la resta es {resta}")
if accion==3:
    multi=num1*num2
    print(f"El resultado de la multiplicación es {multi}")
if accion==4:
    divi=num1/num2
    print(f"El resultado de la división es {divi}")