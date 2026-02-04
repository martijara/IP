# La cantidad de energía necesaria para incrementar la temperatura de un gramo de un material, en
# un grado centígrado o Celsius, es la capacidad calorífica específica del material, C. La cantidad total
# de energía requerida para aumentar la temperatura de m gramos de un material en ΔT grados
# Celsius se puede calcular con la fórmula:
# 𝑞 = 𝑚𝐶∆𝑇
# Escriba un programa que reciba del usuario una masa de agua y el cambio de temperatura
# deseado, y calcule y muestre por pantalla el total de energía que debe agregarse o removerse para
# lograr el cambio de temperatura deseado. Tenga en cuenta que la capacidad calorífica específica
# del agua es de 4.186 𝐽/(𝑔℃)

def main() -> int:
    masa_de_agua = float(input("Masa de agua en gramos: "));
    cambio_temperatura = float(input("Cambio de temperatura deseado: "));

    print("La energia requerida es: " + str(calcular_energia(masa_de_agua, cambio_temperatura)) + " Joules");

    return 0;

def calcular_energia(masa_de_agua:float, cambio_temperatura:float) -> float:
    return masa_de_agua*cambio_temperatura*4.186;

main();