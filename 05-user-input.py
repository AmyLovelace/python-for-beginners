# user input exercise
# calculo_de_segundos = 24 * 60 * 60 #declarar la variable  la antes
calculo_de_minutos = 24 * 60
nombre_de_unidad2 = " minutos"


def dias_a_minutos(num_de_dias):
    return(f"{num_de_dias} dias son {num_de_dias * calculo_de_minutos} {nombre_de_unidad2}")

user_input=input("hola usuario, dame el numero de dias y los convertiré en horas\n")
user_input_number = int(user_input)#volver una string en un numero/integer se le dice casting

valor_calculado = dias_a_minutos(user_input_number)#asi el usuario entrega la informacion para que la variable lo calcule
print(valor_calculado)