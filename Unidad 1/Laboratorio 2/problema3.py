# Extienda el programa del punto anterior para que calcule también el costo de calentar el agua. La
# electricidad se cobra normalmente usando unidades de kilowatt hora (kWh), en vez de Joules. En
# este ejercicio, asuma que la electricidad vale 8.9 centavos por kilowatt-hora. Utilice su programa
# para calcular el costo de hervir agua para una taza de café. Tenga en cuenta que 1 kWh equivale a
# 3600000 Joules.

def main() -> int:
    masa_de_agua = float(input("Masa de agua en gramos: "));
    cambio_temperatura = float(input("Cambio de temperatura deseado: "));

    energia = calcular_energia(masa_de_agua, cambio_temperatura);

    print("La energia requerida es: " + str(energia) + " Joules");
    print("Ël costo es: " + str(8.9*(1/3600000)*energia) + " centavos");

    return 0;

def calcular_energia(masa_de_agua:float, cambio_temperatura:float) -> float:
    return masa_de_agua*cambio_temperatura*4.186;

main();
