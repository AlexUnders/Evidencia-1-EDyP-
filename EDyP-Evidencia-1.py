from collections import namedtuple

separador = "*" * 80
inventario_ventas = {} #Diccionario que contendrá todos los tickets
Detalle_venta = namedtuple("Detalle_venta", "descripcion cant_pzs precio_venta subtotal")

while True:
    print(separador)
    print("Menú principal\n")
    print("1. Registrar una venta.\n")
    print("2. Consultar una venta.\n")
    print("3. Salir\n")
    
    print(separador)
    respuesta = int(input("Escribe el número con la opción que deseas realizar: \n"))
    print(separador)
    
    if respuesta == 1:
        print("Registrar una venta.\n")
        ticket = [] #Inicialización del ticket (lista) sin elementos 
        while True: #Validar que el folio no se repita
            folio = int(input("Folio: "))
            if folio in inventario_ventas.keys():
                print('Esta folio de venta ya existe, porfavor ingresa otro diferente.\n')
            else:
                break
        
        fecha = input("Fecha (DD/MM/YYYY): ")
        ticket.append(fecha)
        total = 0
        
        while True:
            descripcion = input("Descripción de la llanta: ")
            cant_pzs = int(input("Cantidad de llantas que se vendieron: "))
            precio_venta = float(input("Precio de venta: "))
            
            subtotal = cant_pzs * precio_venta
            
            venta_en_turno = Detalle_venta(descripcion, cant_pzs, precio_venta, subtotal)
            ticket.append(venta_en_turno) #Agregar toda la venta registrada al ticket (lista)

            total += subtotal
            print(separador)
            print(f"Subtotal de la venta: {subtotal}")
            print(f"IVA aplicable: {subtotal*0.16}")
            print(f"Monto total de la venta después de impuestos: {subtotal*1.16}")
            print(separador)
            
            seguir_registrando = int(input("¿Seguir registrando ventas? Si=1, No=0: "))
            if seguir_registrando == 1:
                pass
            else:
                print(separador)
                print(f"Monto total de ticket: {total}")
                print(f"IVA aplicable: {total*0.16}")
                print(f"Monto total del ticket después de impuestos: {total*1.16}")
                ticket.insert(0, (total*1.16)) #Pasar a la posición 1 del ticket (lista anidada)
                ticket.insert(1, (total*0.16))
                
                #Agregar el ticket al diccionario de las ventas (tickets)
                inventario_ventas[folio] = ticket
                break
            
    elif respuesta == 2:
        folio_consulta = int(input("Escriba el folio a consultar: "))
        print(separador)
        
        if folio_consulta in inventario_ventas.keys():
            print(f"Folio del ticket: {folio_consulta}\n")
            print(f'Fecha: {inventario_ventas[folio_consulta][2]}')
            print(f'{"Cant pzs":<5} | {"Descripcion":<10} | {"Precio venta":<15} | {"Total":<20} \n')
            for elemento in inventario_ventas[folio_consulta][3:]:
                print(f"{elemento.cant_pzs:<8} | {elemento.descripcion:<11} | ${elemento.precio_venta:<14} | ${elemento.subtotal:<20}")
            print(separador)
            print(f"IVA (16%): {(inventario_ventas[folio_consulta][1])}")
            print(f'Total de la venta: {inventario_ventas[folio_consulta][0]}')
    elif respuesta == 3:
        break
    else:
        print("Respuesta no válida.")
            
            
            
            
        
