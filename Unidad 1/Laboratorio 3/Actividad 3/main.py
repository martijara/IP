import traductor

def ejecutar_saludos(nombre: str)->None:
    """
    Saluda en ingles, espanol, frances, aleman
    
    :param nombre: Description
    :type nombre: str
    """
    print("En ingles -> " + traductor.saludo_ingles(nombre))
    print("En espanol -> " + traductor.saludo_espanol(nombre))
    print("En frances -> " + traductor.saludo_frances(nombre))
    print("En aleman -> " + traductor.saludo_aleman(nombre))

def main()->int:
    print("Bienvenido al programa que muestra tu nombre en 4 saludos diferentes en diferentes idiomas \n\n")
    nombre: str = input("Ingresa tu nombre -> ")
    print("\n\n")
    ejecutar_saludos(nombre)

    return 0

main()