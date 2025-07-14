from Calculadora import Calculadora

# casio = Calculadora()# CREAR UNA CALCULADORA EN BASE A LA CLASE:
# resultado = casio.sumar(1, 2, 3, 4, 5, 6)
# print(resultado)

# 
def main():
    casio = Calculadora()

    menu ="""Calculadora
    [1]Sumar
    [2]Restar
    [3]Multiplicar
    [4]Dividir
    [x]Salir
   """
    print(menu)
    option = input('¿Que operacion quieres realizar?: ')


    # SUMAR
    if option == '1':
        lista_numeros = []
        cantidad = int(input('dime cuantos numero quieres sumar: '))
        for i in range(0, cantidad):
            numero = int(input('Dime el numero: '))
            lista_numeros.append(numero)

        print (casio.sumar(lista_numeros))



    # RESTAR
    elif option == '2':
        numero1 = float(input('Dime el primer numero: : '))
        numero2 = float(input('Dime el segundo numero: '))
        print(casio.sumar(numero1, numero2))


    # MULTIPLICAR
    elif option == '3':
        numero1 = float(input('dime el primer numero: '))
        numero2 = float(input('dime el segundo numero: '))
        numero3 = float(input('dime el tercer numero: '))
        print(casio.multiplicar(numero1, numero2, numero3))


    # DIVIDIR
    elif option == '4':
        numero1 = float(input('Dime el primer numero: '))
        numero2 = float(input('Dime el segundo numero distinto de cero: '))
        print(casio.dividir(numero1, numero2))



    # SALIR
    elif option == 'x':
        pass
    else: 
        print('opcion no valida')
        main()







# -----------------------------
if __name__ == '__main__':
    main()