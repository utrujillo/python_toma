def run():
  array = ("Hola", "mundo", 1)
  print( array )

  lista = ['Hola', 12, 45.7, 'mundo']
  print( lista )

  lista.append("Manuel")
  print( lista )

  lista2 = ['lista2', 'informacion']

  # lista.pop(1)
  # print( lista )

  for item in lista:
    print( 'Elemento de la lista %s' %(item) )

  lista_final = lista + lista2
  print( lista_final )


if __name__ == '__main__':
  run()