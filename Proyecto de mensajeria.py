import random
import datetime
#Proyecto de mensajeria
#Registro de Usuario

print("Bienvenidos a Mensajería Fidelitas")
print("Registre su cuenta de usuario")

print("Informacion personal ")
nombre=input("Ingrese su nombre: ")
print(nombre)
telefonopersonal=int(input("Ingrese teléfono personal: "))
print(telefonopersonal)
correo=input("Ingrese su correo electrónico: ")
print(correo)
numerocedula=int(input("Ingrese su número de cédula: "))
print(numerocedula)
ubcacion=input("Ingrese dirección del destinatario: ")
print(ubcacion)
telefono=int(input("Teléfono del destinatario: "))
print(telefono)

print("Informacion del local")
nombrecomercio=input("Nombre del comercio: ")
print(nombrecomercio)
telefonocomercio=int(input("Teléfono de comercio: "))
print(telefonocomercio)
ubicacionlocal=input("Ubicación de su local: ")
print(ubicacionlocal)
#prueba de git
#Registro de la Factura Electrónica opcional
facturaelectro=int(input("Seleccione 1 si desea factura electrónica, y 2 si no la desea: "))
if facturaelectro==1:
  tipodecedula=int(input("Seleccione 1 para cédula de identidad y 2 para cédula jurídica: "))
  print(tipodecedula)
  if tipodecedula==1:
    cedulaID=int(input("Digite su cédula de identidad: "))
    print(cedulaID)
  if tipodecedula==2:
    cedulajuridica=int(input("Digite su cédula de identidad: "))
    print(cedulajuridica)
  nombreregistrado=input("Digite su nombre registrado: ")
  print(nombreregistrado)
  telefonocomercio=int(input("Ingrese el número de teléfono de la compañia: "))
  print(telefonocomercio)
  correo=input("Ingrese su correo electrónico: ")
  print(correo)
  print("Ingrese su ubicación por: Provincia, canton y distrito: ")
  provincia=input("Provincia: ")
  print(provincia)
  canton=input("Canto: ")
  print(canton)
  distrito=input("Distrito: ")
  print(distrito)
  print(provincia,canton,distrito)

  

#Creacion del paquete
print(nombre) 
print(telefonocomercio)
print(telefonopersonal)


peso = float(input("Igrese el peso de su paquete:kg "))

respuesta= int(input("Seleccione 1 para pago en efectivo y 2 para pago en tarjeta: "))
if respuesta == 2:
  nombretarjeta= input("Ingrese el nombre en su tarjeta: ")
  print(nombretarjeta)
  numerotarjeta= int(input("Ingrese los numeros: "))
  print(numerotarjeta)
  clave= int(input("Ingrese la clave, son los 3 números detrás de su tarjeta: "))
  print(clave)

suma= peso+4000+1000
print("Su total a pagar es:","peso", peso, "Envio",suma)
print("\n")



#INFORMACION COMERCIAL/Nombre/Telefono
print("Guia del Paquete:""\n\n""Remitente""\n" "Mensajeria Fidelitas""\n""22656454""\n""Monto total:",suma)

fechaEntraga=datetime.datetime.now()
print("Fecha de Remitente:",fechaEntraga)


#Numero random
numeroGuia=random.randint(1,1000000)
print("Numero Guia:",numeroGuia)
print("\n")


#PARA FIRMA DE EL USUARIO
print("Destinatario:""\n",nombrecomercio,"\n",telefonocomercio,"\n",ubicacionlocal,"\n""Monto total:",suma)

#iNFORAMCION DEL CONDUCTOR
print("Fecha de Envio:",fechaEntraga)
print("\n")
print("Firma del Socio Conductor:____________________________""\n""Cedula:_________________________")
print("\n")

#PARA FIRMA DE EL USUARIO
print("Firma del Cliente:____________________________""\n""Cedula:_________________________")


#cambio del estado
def paquete_en_preparacion():
  print("El paquete se está preparando.")

def paquete_en_empacado():
  print("El paquete se está empaquetando.")

def paquete_entregado_a_conductor(conductor):
  print(f"El paquete ha sido entregado al conductor {conductor}.")

def paquete_en_camino():
  print("El paquete está en camino.")

  if nombre == "_main_":
    paquete_en_preparacion()
    paquete_en_empacado()

    conductor = "Juan"
    paquete_entregado_a_conductor(conductor)
    
    paquete_en_camino()

#cambio del estado
def paquete_en_preparacion():
  print("El paquete se está preparando.")

def paquete_entregado_a_conductor():
  conductor = input("Ingrese el nombre del conductor: ")
  print("El paquete ha sido entregado al conductor:",conductor)

def paquete_en_camino():
  print("El paquete está en camino.")

  if nombre == "_main_":
    paquete_en_preparacion()
    paquete_en_empacado()

    conductor = "Juan"
    paquete_entregado_a_conductor(conductor)
    
    paquete_en_camino()

# Pregunta si se realizó la entrega
respuesta = input("¿Se realizó la entrega? (Seleccione 1 para Sí y 2 para No): ").lower()

if respuesta == 1:
  print("Entrega Completa")
elif respuesta ==2:
  print("Entrega Fallida")
  
# Función para rastrear el estado del paquete
def rastrear_paquete(numeroGuia):
    if numeroGuia in paquetes_estado:
        return paquetes_estado[numeroGuia]
    else:
        return "Número de guía no encontrado. Verifique el número ingresado."

paquetes_estado=int(input("Seleccione 1 si desea ver el estado del paquete, y 2 si no la desea:"))
if paquetes_estado==1:
  # Rastreo del paquete
  numero_guia_rastreo = input("Ingrese el número de guía del paquete a rastrear: ")
  estado_actual = rastrear_paquete(numero_guia_rastreo)
  print(f"El estado actual del paquete con número de guía {numero_guia_rastreo} es: {estado_actual}")








