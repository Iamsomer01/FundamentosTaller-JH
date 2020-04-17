""" Mostrar en pantalla la cantidad de meses
 transcurridos desde la fecha de nacimiento 
 de un usuario. (Ejercicio bonus. Hay premio!)."""

 #Programa que calcula el total de meses desde cierta fecha 

print (" Programa que calcula el total de meses desde cierta fecha ")
print ("FECHA DE NACIMIENTO")
día=int(input("Ingrese el dia de su nacimiento: "))
mes=int(input("Ingrese el mes de su nacimiento: "))
años=int(input("Ingrese el año de su nacimiento: "))
mesactual=int(input("Ingrese el mes actual: "))
mesactual1= 12-mesactual
Añoactual=int(input("Ingrese el año actual: "))


TolalDeAños = Añoactual-años
TotalDeMeses = TolalDeAños*12-mesactual1


print("Usted tiene",TotalDeMeses,"meses dede su fecha de nacimiento",día,"/",mes,"/",años )

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""Profesor, me ha parececido un ejercicio muy interesante
 y me gustaría ampliar el detalle de este ejercicio, no solo colocando los meses, 
 sino incluir años y dias. En el siguiente ejercicio lo vera de esa manera. 
 Espero que lo disfrute""" #postd: Seguir al EjercicioN11, le echa un vistazo
 #y me cuenta
 

 #Julian Hernandez..