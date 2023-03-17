import modulos_helper
user_input =""
while user_input != "salir":
    user_input=input("hola usuario, dame el numero de dias y la unidad de conversion\n")
    dias_y_unidad = user_input.split(":")
    print(dias_y_unidad)
    dias_y_unidad_dictionary = {"dias":dias_y_unidad[0], "unidad": dias_y_unidad[1]} 
    modulos_helper.validar_y_ejecutar(dias_y_unidad_dictionary)
