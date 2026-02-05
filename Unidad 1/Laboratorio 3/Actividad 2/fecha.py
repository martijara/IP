class Fecha:
    def __init__(self, dia: int = 0, mes: int = 0, anio: int = 0):
        self.dia: int = dia
        self.mes: int = mes
        self.anio: int = anio

def fecha_a_dias(fecha: Fecha)->int:
    return fecha.dia + fecha.mes*30 + fecha.anio*360

def diferencia_entre_fechas(fecha1: Fecha, fecha2: Fecha)->Fecha:
    dias: int = abs(fecha_a_dias(fecha1) - fecha_a_dias(fecha2))
    anio: int = dias//360
    meses:int = (dias%360)//30
    dias:int = meses%30

    return Fecha(dias, meses, anio)