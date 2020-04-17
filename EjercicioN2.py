""" Convertir la cantidad de dólares ingresados 
por un usuario a pesos colombianos y mostrar el 
resultado en pantalla"""

#Programa que convierta dolarea a pesos colombianos 
print("Programa que convierta dolarea a pesos colombianos ")
dolarCOP = 3937.96
print ("¿En la actualidad el dolar está a ",dolarCOP,"pesos colombianos? (si/no)")
actualidad = input()
if actualidad == "si":
  print("Ingrese el valor en dolares a convertir")
  dolar= input()
  cop=int(dolar)*int(dolarCOP)
  print("La conversion de",dolar,"a pesos colombianos es:",cop)
elif actualidad == "no": 
  print ("ingrese el valor del dolar actualmente")
  dolarAT = input()
  print ("Ingrese el valor en dolaresa convertir")
  dolarAC = input()
  cop2=int(dolarAC)*int(dolarAT)
  print("La conversion de",dolarAC,"a pesos colombianos es:",cop2)

  #Julian Hernandez..