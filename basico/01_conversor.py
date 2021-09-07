DOLLAR = 22.05
pregunta = input("Cuantos pesos tienes? ")
respuesta = pregunta
# print( type(respuesta) )
print('Tengo '+ respuesta)
dolares = round(float(respuesta) / DOLLAR, 2)
print('Mis '+ respuesta +' son '+ str(dolares) +' dls')
