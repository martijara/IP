# Escriba un programa que calcule el área total de la fachada de una casa para determinar el
# presupuesto de remodelación. El usuario debe ingresar, mediante la consola, el ancho de la casa
# (que servirá como base tanto para la estructura como para el techo), la altura de la pared (la parte
# rectangular), la altura del techo (la parte triangular medida desde donde termina la pared hasta la
# punta superior) y el costo de la pintura por metro cuadrado. El programa debe calcular el área de
# la base multiplicando el ancho por la altura de la pared, y el área del techo aplicando la fórmula
# del triángulo, la cual es el ancho multiplicado por la altura del techo, todo esto dividido entre dos;
# es fundamental aquí el uso correcto de paréntesis para asegurar que la división afecte al producto
# total. Finalmente, el sistema debe sumar ambas áreas para obtener el área total, calcular el costo
# final de la pintura y determinar la cantidad de baldes de pintura necesarios, asumiendo que un
# balde cubre exactamente 10 metros cuadrados. El resultado debe imprimirse en un solo párrafo
# que diga: "Para una fachada con un área total de [X] m², se requieren [Y] baldes de pintura, con un
# costo total de $[Z] pesos", asegurándose de que todos los valores numéricos se muestren con dos
# decimales

def main() -> int:
    ancho = float(input("äncho: "));
    altura_pared = float(input("ältura: "));
    altura_techo = float(input("ältura techo: "));
    costo_pintura = float(input("Costo pintura por metro cuadrado: "));

    calcular_costo(ancho, altura_pared, altura_techo, costo_pintura);

    return 0;

def calcular_costo(ancho:float, altura_pared:float, altura_techo:float, costo_pintura:float):
    area_base = ancho*altura_pared;
    area_techo = (ancho*altura_techo)/2;
    area_total = area_base + area_techo;

    baldes = area_total/10;
    costo_total = costo_pintura*area_total;

    print("Para una fachada con un área total de " + str(round(area_total, 2)) + "m², se requieren " + str(round(baldes, 2)) + " baldes de pintura, con un costo total de $" + str(round(costo_total,2)) +" pesos");

main();