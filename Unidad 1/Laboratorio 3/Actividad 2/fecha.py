class Fecha:
    def __init__(self, dia: int = 0, mes: int = 0, anio: int = 0):
        self.dia: int = dia
        self.mes: int = mes
        self.anio: int = anio

def fecha_a_dias(fecha: Fecha)->int:
    """
    convierte una fecha a dias
    
    :param fecha: Description
    :type fecha: Fecha
    :return: Description
    :rtype: int
    """
    return fecha.dia + fecha.mes*30 + fecha.anio*360

def diferencia_entre_fechas(fecha1: Fecha, fecha2: Fecha)->Fecha:
    """
    Diferencia entre fechas
    
    :param fecha1: Description
    :type fecha1: Fecha
    :param fecha2: Description
    :type fecha2: Fecha
    :return: Description
    :rtype: Fecha
    """
    dias: int = abs(fecha_a_dias(fecha1) - fecha_a_dias(fecha2))
    anio: int = dias//360
    meses:int = (dias%360)//30
    dias:int = meses%30

    return Fecha(dias, meses, anio)