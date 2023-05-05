# Ingresa una lista de numeros y un objetivo, el programa debe encontrar la suma de numeros que logre ese objetivo
# Esto anda perfecto lo unico q habria q sumar es una etapa de validaciones para q no ingrese pelotudeces q no sean numeros, pero anda cheto :)
numeros = []
resul = []

print("Ingresa la lista de los numeros, cuando quieras dejar de ingrsar pone un *\n")
a = -1
x = 0
y = 1
flag = 0
while (numeros == [] or numeros[a] != '*'):
    print ("Ingrese el numero de posicion ",a+1,":")
    numeros.append(input())
    a = a + 1
numeros.pop()
print(numeros)

obj = input("Ingrese el objetivo que desee: ")

for x in range(len(numeros)):
    if(flag != 1):
        for y in range(len(numeros)):
            if (int(numeros[x]) + int(numeros[y]) == int(obj)):
                flag = 1
                resul.append(x)
                resul.append(y)
                break

if flag == 1:
    print("Existe una solucion valida y es ",resul)
elif flag == 0:
    print("No existe una solucion valida")
