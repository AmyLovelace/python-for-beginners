from modulos_helper import validar_y_ejecutar, user_input_message
user_input =""
while user_input != "salir":
    user_input=input(user_input_message)
    dias_y_unidad = user_input.split(":")
    dias_y_unidad_dictionary = {"dias":dias_y_unidad[0], "unidad": dias_y_unidad[1]} 
    validar_y_ejecutar(dias_y_unidad_dictionary)
