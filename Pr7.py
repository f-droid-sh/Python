num1 = float(input("Numero1 -> "))
print("")
num2 = float(input("Numero2 -> "))
print("")
num3 = float(input("Numero3 -> "))
print("")
if num1>=num2 and num1>=num3:
    print(f"El numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"El numero mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print(f"El numero mayor es {num3}")