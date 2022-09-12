class Vehiculo:
    def __init__(self,codigo=000,modelo="No hay",marca="No hay",color="No hay",placa="No hay",estado="No identificado"):
        self.codigo=codigo
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self.placa=placa
        self.estado=estado

    def get_codigo(self):
        return self.codigo
    def get_modelo(self):
        return self.modelo
    def get_marca(self):
        return self.marca
    def get_color(self):
        return self.color
    def get_placa(self):
        return self.placa
    def get_estado(self):
        return self.estado

    def set_codigo(self,nuevo_codigo):
        self.codigo=nuevo_codigo
    def set_modelo(self,nuevo_modelo):
        self.modelo=nuevo_modelo
    def set_marca(self,nueva_marca):
        self.marca=nueva_marca
    def set_color(self,nuevo_color):
        self.color=nuevo_color
    def set_placa(self,nueva_placa):
        self.placa=nueva_placa
    def set_estado(self,nuevo_estado):
        self.estado=nuevo_estado

    def __str__(self):
        return "\nCodigo "+str(self.codigo)+"\nModelo "+self.modelo +"\nMarca "+self.marca+ "\nColor "+self.color+"\nPlaca "+self.placa+ "\nEstado "+self.estado

vehiculo=Vehiculo(1,"Rv4","Toyota","Azul","4512AQF","Nuevo")

print(vehiculo)
vehiculo.set_marca("Tesla")
vehiculo.set_color("Rojo")
print(vehiculo)



