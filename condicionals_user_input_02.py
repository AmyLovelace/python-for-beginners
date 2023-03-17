#conditionals in the case of an user input exercise 
#what happens if the user put a text instead of a number

calculo_de_minutos = 24 * 60
nombre_de_unidad2 = " minutos"


def dias_a_minutos(num_de_dias):
    if num_de_dias > 0 :# > operadores de comparacion 
        return f"{num_de_dias} dias son {num_de_dias * calculo_de_minutos} {nombre_de_unidad2}"
    elif num_de_dias == 0: #= representa asignarle un valor a una variable == checkea por igualdad
        return "entregaste un 0, porfavor digita un numero positivo"
    else:
        return "entregaste un numero negativo, no te podré dar resultado!"

def validar_y_ejecutar():
    if user_input.isdigit():
        user_input_number = int(user_input)#volver una string en un numero/integer se le dice casting
        valor_calculado = dias_a_minutos(user_input_number)#asi el usuario entrega la informacion para que la variable lo calcule
        print(valor_calculado)
    else:
        print("lo ingresado no es un numero valido. fuck off bitch")
  
user_input=input("hola usuario, dame el numero de dias y los convertiré en horas\n")
validar_y_ejecutar()
