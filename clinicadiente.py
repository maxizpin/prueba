Carillas_Porcelana = 250000
Implantes_Dentales = 475000
Ortodoncia_Brackets = 800000
Auxiliar = 0.15
Administrativo = 0.10
Docente = 0.05
menutratamientos = int(input("¿Que tratamiento desea? \n 1- Carillas Porcelana \n 2- Implantes Dentales \n 3- Ortodoncia Brackets \n :"))
while menutratamientos != 0:
    if menutratamientos == 1:
        puestoduoc = int(input("¿Que puesto tiene en duoc? \n 1- Auxiliar \n 2- Administrativo \n 3- Docente \n : "))
        if puestoduoc == 1:
          cant = int(input("Canidad: "))
          sub = Carillas_Porcelana * cant
          desc = sub * Auxiliar
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
        if puestoduoc == 2:
          cant = int(input("Canidad: "))
          sub = Carillas_Porcelana * cant
          desc = sub * Administrativo
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
        if puestoduoc == 3:
          cant = int(input("Canidad: "))
          sub = Carillas_Porcelana * cant
          desc = sub * Docente
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
    elif menutratamientos == 2:
        puestoduoc = int(input("¿Que puesto tiene en duoc? \n 1- Auxiliar \n 2- Administrativo \n 3- Docente \n : "))
        if puestoduoc == 1:
          cant = int(input("Canidad: "))
          sub = Implantes_Dentales * cant
          desc = sub * Auxiliar
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
        if puestoduoc == 2:
          cant = int(input("Canidad: "))
          sub = Implantes_Dentales * cant
          desc = sub * Administrativo
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
        if puestoduoc == 3:
          cant = int(input("Canidad: "))
          sub = Implantes_Dentales * cant
          desc = sub * Docente
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
    elif menutratamientos == 3:
        puestoduoc = int(input("¿Que puesto tiene en duoc? \n 1- Auxiliar \n 2- Administrativo \n 3- Docente \n : "))
        if puestoduoc == 1:
          cant = int(input("Canidad: "))
          sub = Ortodoncia_Brackets * cant
          desc = sub * Auxiliar
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total)
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
        if puestoduoc == 2:
          cant = int(input("Canidad: "))
          sub = Ortodoncia_Brackets * cant
          desc = sub * Administrativo
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total) 
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")
        if puestoduoc == 3:
          cant = int(input("Canidad: "))
          sub = Implantes_Dentales * cant
          desc = sub * Docente
          total = sub - desc
          cuotas = total / 12
          print("Subtotal: ",sub)
          print("Descuento: ",desc)
          print("Total a pagar: ",total) 
          print("Son 12 cuotas de: ",cuotas)
          print("Sonria bonito!!!")  
    else:
        print("seleccione una opcion valida")               
