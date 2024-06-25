import os

def fGrabar_Datos():
    while True:
        print("Ingrese tipo de Vehiculo\n1) Automóvil\n2) Camión\n3) Camioneta\n4) Moto")
        try:
            vTipo = int(input("Ingrese opcion numerica del tipo de vehiculo : "))
        except :
            vTipo = 0
        if vTipo < 0 or vTipo > 4:
            print("Valor ingresado no valido, intente nuevamente")
        elif vTipo == 1:
            lRegistro_Vehiculo.append({'Tipo_Vehiculo' : "Automovil"})
            print("siguiente.")
            
        elif vTipo == 2:
            lRegistro_Vehiculo.append({'Tipo_Vehiculo' : "Camion"})
            print("siguiente.")
            
        elif vTipo == 3:
            lRegistro_Vehiculo.append({'Tipo_Vehiculo' : "Camioneta"})
            print("siguiente.")
            
        elif vTipo == 4:
            lRegistro_Vehiculo.append({'Tipo_Vehiculo' : "Moto"})
            print("siguiente.")
            
                                      
        
        while True:
            vPatente = input("Ingrese patente del vehiculo : ")
            if vPatente == "" or len(vPatente) != 6 :
                print("Valor Invalido")
            else :
                lRegistro_Vehiculo.append({'Patente_Vehiculo' : vPatente})
                print("siguiente.")
                break  
                
        while True:
            vMarca = input("Ingrese Marca del vehiculo : ")
            if vMarca == "" or len(vMarca) < 5 or len(vMarca) > 15:
                print("Valor Invalido")
            else :
                lRegistro_Vehiculo.append({'Marca_Vehiculo' : vMarca})
                print("siguiente.")
                break
        
        while True:
            try :
                vPrecio = int(input("Ingrese Precio del vehiculo : "))
            except :
                vPrecio = 0

            if vPrecio < 5000000 :
                print("Monto ingresado no valido")
            else :
                lRegistro_Vehiculo.append({'Precio_Vehiculo' : vPrecio})
                print("Siguiente.")
                break
       
        try : 
            vMulta = int(input("¿El vehiculo posee mutas?, Ingrese cantidad : "))
        except :
            vMulta = 0
            
        lMultas = []
                
        if vMulta >= 1 :
        
            while True :
                try :
                    vMonto_Multa = int(input("Ingrese Monto de la multa : "))
                except :
                    vMonto_Multa = 0
                    
                if vMonto_Multa < 1 :
                    print("Monto no valido")
                else :
                    vFecha_Multa = input("Ingrese fecha de la multa en (formato DD/MM/AAAA) : ")
                    if vFecha_Multa == "":
                        print("Valor ingresado no valido")
                    else:
                        lMultas.append({'Monto_Multa' : vMonto_Multa, 'Fecha_Multa' : vFecha_Multa})
                        lRegistro_Vehiculo.append({'Multas_del_Vehiculo' : vMulta})
                        break
                                        
        vNombre_Dueño = input("Ingrese nombre del dueño del vehiculo : ")
        if vNombre_Dueño == "" :
            print("Valor Invalido")
        else :
            lRegistro_Vehiculo.append({'Nombre_dueño_Vehiculo' : vNombre_Dueño})
            print("siguiente.")
        
        while True :
            try :
                vRUN_Dueño = int(input("Ingrese RUN del dueño del vehiculo : "))
            except :
                vRUN_Dueño = 0
            if vRUN_Dueño == "" :
                print("Valor Invalido")
            else :
                lRegistro_Vehiculo.append({'RUN_dueño_Vehiculo' : vRUN_Dueño})
                print("siguiente.") 
                break
                    
lRegistro_Vehiculo = []            


print("Bienvenido a Automotora Auto Seguro")
print("Opciones para escoger : ")
print("1) Grabar datos\n2) Buscar Información\n3) Imprimir Certificado\n4) Salir")

while True:
    try :
        vOp_Menu = int(input("Escoja su opcion : "))
    except :
        vOp_Menu = 0
        
    if vOp_Menu < 1 or vOp_Menu > 4 :
        print("opcion no valida")
    
    elif vOp_Menu == 1 :
        print("Ingrese los datos solicitados a continuacion")
        fGrabar_Datos()
        
    elif vOp_Menu == 2 :
        print("Ingrese patente para buscar su informacion")
        for elem in lRegistro_Vehiculo:
            for patente,vPatente in elem.lRegistro.Vehiculo():
                print(patente, vPatente)
            print ( "***" )
    
    elif vOp_Menu == 3 :
        print("¿Que tipo de certificado necesita?")
        print("1) Emisión de contaminantes\n2) Anotaciones Vigentes\n3) Multas")
    else :
        print("Eveline Aliaga Cartagena, v1")
        print("A salido de la aplicación\nAdios!")    
        break
    
        
    
        
