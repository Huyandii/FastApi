class Calculadora:

    #como no voy a inicializar ninguna propiedad de la clase no necesito el metodo __init__(constructor) POR QUE NO ES OBLIGATORIO

    #Funciones 

    def  sumar(self, numeros):
        resultado = 0
        for numero in numeros:
            resultado += numero
        return resultado
    

    def restar(self, n1, n2):
        return n1 - n2 if n1 >= n2 else n2 -n1


    def multiplicar(self, *numeros):
        resultado = 1
        for numero in numeros:
            resultado *= numero
        return resultado


    def dividir(self, n1, n2):
        try:
           return n1 / n2
        except ZeroDivisionError:
            print('No se puede dividir por cero')
    
# -----------------------------------------

