# Roman to integer
# Se ingresa un numero en romano y te devuelve el int de eso

rom = input("Ingresar el numero romano correspondiente: ")
rom = rom.upper()
x = 1
resul = 0

for x in range(len(rom)):
    if rom[x] == 'I' and (rom[x+1] == 'V' or rom[x+1] == 'X'):
        if rom[x+1] == 'V':
            resul = resul + 4
        elif rom[x+1] == 'X':
            resul = resul + 9
    elif rom[x] == 'I':
        resul = resul + 1
    
    if rom[x] == 'V' and rom[x-1] != 'I':
        resul = resul + 5

    if rom[x] == 'X' and (rom[x+1] == 'L' or rom[x+1] == 'C'):
        if rom[x+1] == 'L':
            resul = resul + 40
        elif rom[x+1] == 'C':
            resul = resul + 90
    elif rom[x] == 'X':
        resul = resul + 1

    if rom[x] == 'L' and rom[x-1] != 'X':
        resul = resul + 50

    if rom[x] == 'C' and (rom[x+1] == 'D' or rom[x+1] == 'M'):
        if rom[x+1] == 'D':
            resul = resul + 400
        elif rom[x+1] == 'M':
            resul = resul + 900
    elif rom[x] == 'C':
        resul = resul + 100

    if rom[x] == 'D' and rom[x-1] != 'C':
        resul = resul + 500

    if rom[x] == 'M' and rom[x-1] != 'C':
        resul = resul + 1000

print(resul)