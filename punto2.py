cuentas=[]

for i in range(3):
    cuenta={}
    cuenta['numero']=int(input("ingrese la cuenta: "))
    cuenta['saldo']=int(input("ingrese el saldo cuenta: "))
    cuentas.append(cuenta)
for i in range(len(cuentas)-1,-1,-1):
    print(cuentas[i],end="")