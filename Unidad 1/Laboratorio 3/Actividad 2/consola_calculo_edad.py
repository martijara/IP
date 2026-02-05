from fecha import Fecha, diferencia_entre_fechas

def main()->int:
    print("Bienvenid@ al calculador de edad!")
    print()

    fechaNacimiento: Fecha = Fecha()
    fechaActual: Fecha = Fecha()
    
    fechaNacimiento.dia = int(input("Cual es el dia de tu nacimiento -> "))
    fechaNacimiento.mes = int(input("Cual es el ms de tu nacimiento? -> "))
    fechaNacimiento.anio = int(input("Cual es el anio de tu nacimiento -> "))

    print("\n Ahora, ingrese la fecha actual")
    fechaActual.dia = int(input("Cual es el dia actual -> "))
    fechaActual.mes = int(input("Cual es el mes actual -> "))
    fechaActual.anio = int(input("Cual es el anio actual -> "))
    
    resultado: Fecha = diferencia_entre_fechas(fechaActual, fechaNacimiento)

    print("La edad es " + str(resultado.dia) + " dias, " + str(resultado.mes) + " meses, " + str(resultado.anio) + " anios")

    return 0


main()