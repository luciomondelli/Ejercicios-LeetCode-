# Valor Absoluto
# Ingresa una lista de numeros, te devuelve un 0 si ingresaste un 0 o si no ingresaste numeros, 1 si el producto de la lista es positivo y 
# 2 si el producto es negativo


numeros = []
cant_num = int(input("Ingrese la cantidad de numeros que va a ingresar: "))
i=0
producto = 1
while i < cant_num:
    print(f"Ingrese el numero",i+1,":")
    numeros.append(int(input()))
    producto = producto * numeros[i]
    i = i+1
if cant_num == 1 or cant_num == 0:
    if producto == 0:
        print("0")
else:
    if producto > 0:
        print("1")
    else:
        print("2")
    