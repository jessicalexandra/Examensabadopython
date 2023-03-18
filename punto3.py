cantidadnumeros=int(input("ingrese la cantidad de numeros: "))
multiplos2=0
multiplos3=0
cantidadmul2y3=0
for i in range(cantidadnumeros):
    numero=int(input("ingrese el numero: "))
    if numero%2==0:
        multiplos2+=1
        cantidadmul2y3+=1
    if numero%3==0:
        multiplos3+=1
        cantidadmul2y3+=1
print(f'la cantidad de multiplos de 2 son:{multiplos2}')
print(f'la cantidad de multiplos de 3 son:{multiplos3}')
print(f'la cantidad de multiplos de 2 y 3 fueron :{cantidadmul2y3}')
    
