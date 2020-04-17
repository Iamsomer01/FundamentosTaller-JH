"""Calcular el número de vueltas que da
 una llanta en 1 km, dado que el diámetro 
 de la llanta es de 50 cm, mostrar el resultado en pantalla."""

#Programa que calcule el numero de vueltas que da un llanta
print ("Programa que calcule el numero de vueltas que da un llanta")
Diametro = 50
pi = 3.1416
Distancia_cm = 100000
Circunferencia = Diametro*pi #formula de la circunferencia 
NumeroDeVueltas= Distancia_cm/Circunferencia
print ("El numero de vueltas que da la llanta a una distancia de",Distancia_cm,"cm es de: ",round (NumeroDeVueltas))

#Julian Hernandez..