# Escriba un programa que reciba por parte del usuario el costo de la orden realizada en un
# restaurante, el mesero que atendió la orden, y calcule el IVA y propina correspondientes a la orden.
# Utilice una tasa del 8% sobre el valor de la orden para calcular el IVA, y asuma que la propina
# corresponde al 10% del valor de la factura (antes de impuestos) y una tasa de servicio de 20.000
# pesos.. Su programa debe mostrar como resultado una factura como la que se muestra a
# continuación. Todos los valores deben mostrarse sólo con dos decimales

def main() -> int:
    costo_orden = float(input("Cual es el costo de tu orden?: "));
    mesero = input("Cual es el nombre de tu mesero?: ");
    imprimir_orden(costo_orden, mesero);
    return 0;

def imprimir_orden(cost_orden:float, mesero:str):
    iva = cost_orden*0.08;
    propina = cost_orden*0.1;
    servicio = 20000;

    print("Nombre del mesero: " + mesero);
    print("Costo de la orden: $" + str(round(cost_orden, 2)));
    print("-"*7 + " RECIBO DE PAGO " + "-"*7);
    print("Mesero: " + mesero);
    print("IVA (8%): $" + str(round(iva, 2)));
    print("Propina (10%): $" + str(round(propina, 2)));
    print("Tasa de Servicio: $" + str(round(servicio, 2)));
    print("-"*30);
    print("TOTAL A PAGAR: $" + str(round(cost_orden + iva + propina + servicio, 2)));
    print("-"*30 + "\n");

main();



    


