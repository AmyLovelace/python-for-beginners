#ejercicio for loop 
calculo_de_minutos = 24 * 60
nombre_de_unidad2 ='minutos'


def dias_a_minutos(num_de_dias):
    return f"{num_de_dias} dias son {num_de_dias * calculo_de_minutos} {nombre_de_unidad2}"
  
def validar_y_ejecutar():
    try:
        user_input_number = int(num_de_dias_elemento)
        if user_input_number > 0:
            valor_calculado = dias_a_minutos(user_input_number)#asi el usuario entrega la informacion para que la variable lo calcule
            print(valor_calculado)
        elif user_input_number == 0:
            print("entregaste un 0, porfavor digita un numero positivo")
        else:
            print("lo ingresado no es un numero valido. fuck off bitch")
    except ValueError:
        print("lo que ingresaste no es un numero valido, no te voy a convertir nah")

user_input =""
while user_input != "salir":
    user_input=input("hola usuario, dame el numero de dias y los convertiré en minutos\n")
    print(type(user_input.split(" , ")))
    print(user_input.split(" , "))
    for num_de_dias_elemento in user_input.split(" , "):
        validar_y_ejecutar()
    
    