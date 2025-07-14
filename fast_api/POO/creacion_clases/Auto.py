class Auto:
    
    #atributos - propiedades - variables, aspectos visuales de un objeto
    color: str = ""
    price: float = 0
    type_gas: str = ""
    estado: bool = True
    Matricula: str = ""
    model: str = ""
    velocidad: int = 0
    
    # metodos - funciones - acciones que puede realizar mi objeto
    # funcion constru tor no es obligatoria, pero se ejecuta siempre, como programador me puede servir para inicializar datos: el metodo constructor en python es "__init__()"

    def __init__(self, color, price, model, type_gas): 
        self.color = color
        self.price = price
        self.model = model
        self.type_gas = type_gas

    def matrucular(self, numero_matricula):
        self.matrucular = numero_matricula
    
    def acelera(self, velocity):
        self.velocidad += velocity

    def frenar(self, velocity):
        self.velocidad -= velocity

ferrari = Auto('rojo', 100000, 'f380', 'gasolina')
fiat = Auto('vino', 1500, 'topolino', 'diesel')



print(fiat.color, fiat.price, fiat.type_gas)
print(ferrari.model)

ferrari.acelera(100)
print(ferrari.velocidad)


