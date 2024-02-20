class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if(color == "rojo" or color == "verde" or color == "amarilo" or color == "negro" or color == "blanco"):
            self.color = color

        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if(tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, marca, motor, registro, asientos):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.asientos = asientos
    
    def cantidadAsientos(self):

        cAsientos = 0
        for asientos in self.asientos:
                if(type(asientos) == Asiento):
                    cAsientos = cAsientos + 1
        
        return cAsientos

    def verificarIntegridad(self):
        if(self.registro == self.motor.registro):
            for asiento in self.asientos:
                if(type(asiento) == Asiento):
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"