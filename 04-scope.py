calculo_de_segundos = 24 * 60 * 60 #declarar la variable  la antes 
calculo_de_minutos = 24 * 60
nombre_de_unidad = "segundos"
nombre_de_unidad2= " minutos"

def dias_a_minutos(num_de_dias):
    print(f"{num_de_dias} dias son {num_de_dias * calculo_de_minutos} {nombre_de_unidad2}")
dias_a_minutos(1)

def scope_check(nombreminutos):
    my_var = "variable dentro de una funcion"
    print(nombre_de_unidad)
    print(nombreminutos)
    print(my_var)
scope_check(20)

def dias_a_segundos(num_de_dias,mensaje_personal):
    print(f"{num_de_dias} dias son {num_de_dias* calculo_de_segundos } { nombre_de_unidad} ")
    print(mensaje_personal)
dias_a_segundos(10, "wow!")


