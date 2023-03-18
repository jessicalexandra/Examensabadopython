print("***ciclistas***")
print("1 ingrese registro del ciclista ")
print("2 mostrar registro  del ciclista")
print("3 editar el tiempo del ciclista ")
print("4 eliminar registro del cilista")
print("5 SALIR")
id=1
ciclistas=[]

option=10

while option!=5:
    option=int(input("ingrese la opcion elegida: "))
    ciclista={}
    if option==1:
        ciclista['codigo']=id
        ciclista['nombre']=(input("ingrese el nombre del ciclista: "))
        ciclista['edad']=int(input("ingrese la edad del ciclista: "))
        ciclista['pais']=(input("ingrese el pais del ciclista: "))
        ciclista['equipo']=(input("ingrese el equipo del ciclista: "))
        ciclista['tiempo']=int(input("ingrese el timpo del ciclista: "))
        ciclistas.append(ciclista)
        id=id+1
    if option==2:
        print(ciclistas)
    if option==3:
        buscar=int(input("ingrese el codigo que desea buscar: "))
        for ciclista in ciclistas:
            if ciclista['codigo']==buscar:
                ciclista['tiempo']=int(input("digita el nuevo tiempo: "))
                break
            else:
                print("nombre no encontrado")
    if option==4:
          buscar=int(input("ingrese el codigo que desea buscar: "))
          for ciclista in ciclistas:
            if ciclista['codigo']==buscar:
                ciclistas.remove(ciclista)
                print("ciclista eliminado")
                break
            else:
                print("ciclista no encontrado")
    if option==5:
        pass




