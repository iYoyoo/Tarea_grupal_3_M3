#Definir el stock de un producto en una variable.
stock = 60
#Definir una forma de solicitar el stock disponible del producto por consola.
pedir_stock = input("¿Quiere revisar el stock? (S/N): ").lower()
if pedir_stock== "s":
  print(stock)
#Definir una forma de solicitar unidades del producto por consola. Este número de productos se
#almacenarán en una nueva variable llamada ‘Productos seleccionados’.
productos_seleccionados = input("¿Quiere solicitar unidades del producto? (S/N) :").lower()
if productos_seleccionados == "s":
  productos_seleccionados = abs(int(input("Indique la cantidad de productos :")))
  adicional = productos_seleccionados + 1
  #El programa debe verificar que existan unidades disponibles.
  if stock - productos_seleccionados > 0 and productos_seleccionados <= 20:
    #Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen
    #más de 12 unidades.
    #Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las
    #unidades justas.
    if productos_seleccionados >= 12 and stock >= adicional:
      print ("¡Al llevar más de 12 productos, y al tener stock suficiente, se lleva un producto de regalo!, su compra es de :", adicional)
      #Los productos reubicados serán descontados del stock inicial.
      stock = stock - adicional
      print ("El total de su compra es de :", adicional," Productos")
      print ("El nuevo stock disponible es: ", stock)
    elif productos_seleccionados < 12:
      #Los productos reubicados serán descontados del stock inicial.
      stock = stock - productos_seleccionados
      print ("El total de su compra es de :", productos_seleccionados," Productos")
      print ("El nuevo stock disponible es: ", stock)
  elif stock - adicional < 0:
    stock = stock - productos_seleccionados
    print ("El stock no es suficiente para cumplir la promoción, por lo que sólo llevara la cantidad solicitada :", productos_seleccionados)
  #No se pueden solicitar más de 20 unidades en un mismo pedido.    
  elif productos_seleccionados > 20:
    print ("Debe ingresar valores menores o iguales a 20")
  #Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no
  #es posible realizar esta acción debido a que no hay stock suficiente.
  elif stock - productos_seleccionados < 0:
    print("No tenemos stock para su solicitud, el stock disponible es", stock)