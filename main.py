import json
from os import system

with open("compras.json","r") as openfile:
    comprajson= json.load(openfile)

with open("empleados.json","r") as openfile:
    empleadosjson= json.load(openfile)

with open ("medicamentos.json", "r") as openfile:
    medicamentosjson= json.load(openfile)

with open ("pacientes.json", "r") as openfile:
    pacientesjson= json.load(openfile)

with open ("provedores.json", "r") as openfile:
    provedoresjson= json.load(openfile)

with open("ventas.json","r") as openfile:
    ventasjson= json.load(openfile)

print("─── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ──")
print("                   Farmacia                  ")
print("─── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ──")
print("")
print("1. Registrar Ventas")
print("2. Registrar Compras")
print("3. Ver medicamentos")
print("4. Ver provedores")
print("5. Ver pacientes")
print("6. Ver empleados")
print("")

opcion=int(input("Ingrese el número de la opción que deseas ver: "))
if opcion==1:
    system("cls")
    print("─── ⋆⋅☆⋅⋆ ──Registrar Ventas─── ⋆⋅☆⋅⋆ ──")
    print("")
    fechaVenta= str(input("Fecha: "))
    print("")
    print("Información del paciente")
    print("")
    nombrePaciente= str(input("Nombre: "))
    direccionPaciente= str(input("Dirección: "))
    telefono= str(input("Teléfono: "))
    print("")
    print("Información del empleado")
    print("")
    nombreEmpleado=str(input("Nombre: "))
    cargo= str(input("Cargo: "))
    print("")
    print("Información del Medicamento vendido")
    print("")
    nombreMedicamento= str(input("Nombre: "))
    cantidadVenta= int(input("Cantidad: "))
    precioVenta=str(input("Precio: "))

    #agregar un paciente nuevo al json de pacientes
    ventaPaciente= {
        "nombre": nombrePaciente,
        "direccion": direccionPaciente,
        "telefono": telefono
    }
    pacientesjson +=[ventaPaciente]
    
    with open("pacientes.json","w") as outfile:
        json.dump(pacientesjson, outfile, indent=4)

    venta={
        "fechaVenta": fechaVenta,
        "paciente": {
            "nombre": nombrePaciente,
            "direccion": direccionPaciente
        },
        "empleado": {
            "nombre": nombreEmpleado,
            "cargo": cargo
        },
        "medicamentosVendidos": [
            {
                "nombreMedicamento": nombreMedicamento,
                "cantidadVendida": cantidadVenta,
                "precio": precioVenta
            }
        ]
    }
    

    ventasjson +=[venta]
    
    with open("ventas.json","w") as outfile:
        json.dump(ventasjson, outfile, indent=4)
   
    
if opcion==2:
    system("cls")
    print("─── ⋆⋅☆⋅⋆ ──Registrar Compras─── ⋆⋅☆⋅⋆ ──")
    print("")
    fechaCompra= str(input("Fecha: "))
    print("")
    print("Información del Provedor")
    print("")
    nombreProvedor= str(input("Nombre: "))
    contactoProvedor= str(input("Contacto: "))
    direccionprovedor= str(input("Dirección: "))
    print("")
    print("Información del Medicamento Comprado")
    print("")
    nombreCompraM= str(input("Nombre: "))
    cantidadCompra= int(input("Cantidad: "))
    precioCompra=str(input("Precio de compra: "))

    compraAgg= {
        "fechaCompra": fechaCompra,
        "proveedor": {
            "nombre": nombreProvedor,
            "contacto": contactoProvedor
        },
        "medicamentosComprados": [
            {
                "nombreMedicamento": nombreCompraM,
                "cantidadComprada": cantidadCompra,
                "precioCompra": precioCompra
            }
        ]
    }

    comprajson +=[compraAgg]

    with open("compras.json","w") as outfile:
        json.dump(comprajson, outfile, indent=4)

    provedor={
        "nombre": nombreProvedor,
        "contacto": contactoProvedor,
        "direccion": direccionprovedor
    }

    provedoresjson +=[provedor]

    with open("provedores.json","w") as outfile:
        json.dump(provedoresjson, outfile, indent=4)

if opcion==3:
    contador=1
    system("cls")
    print("─── ⋆⋅☆⋅⋆ ──Medicamentos─── ⋆⋅☆⋅⋆ ──")
    print("")

    for i in medicamentosjson:

        print(contador)
        print(f"Nombre del medicamento: {i["nombre"]}")
        print(f"Precio: {i["precio"]}")
        print(f"Stock: {i["stock"]}")
        print("˗ˏˋ ★ ˎˊ˗")
        print("")
        contador=contador+1

if opcion==4:
    system("cls")
    print("─── ⋆⋅☆⋅⋆ ──Provedores─── ⋆⋅☆⋅⋆ ──")
    print("")
    contador=1
    for i in provedoresjson:

        print(contador)
        print(f"{i["nombre"]}")
        print(f"Contacto: {i["contacto"]}")
        print(f"Dirección: {i["direccion"]}")
        print("˗ˏˋ ★ ˎˊ˗")
        print("")
        contador=contador+1
if opcion==5:

    system("cls")
    print("─── ⋆⋅☆⋅⋆ ──Pacientes─── ⋆⋅☆⋅⋆ ──")
    print("")
    contador=1
    for i in pacientesjson:

        print(contador)
        print(f"Nombre: {i["nombre"]}")
        print(f"Telefono: {i["telefono"]}")
        print(f"Dirección: {i["direccion"]}")
        print("˗ˏˋ ★ ˎˊ˗")
        print("")
        contador=contador+1

if opcion==6:

    system("cls")
    print("─── ⋆⋅☆⋅⋆ ──Empleados─── ⋆⋅☆⋅⋆ ──")
    print("")
    contador=1
    for i in empleadosjson:

        print(contador)
        print(f"Nombre: {i["nombre"]}")
        print(f"Fecha del contrato: {i["fechaContratacion"]}")
        print(f"Cargo: {i["cargo"]}")
        print("˗ˏˋ ★ ˎˊ˗")
        print("")
        contador=contador+1