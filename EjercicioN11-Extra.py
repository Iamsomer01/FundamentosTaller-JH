


#Programa extra que calcula el total de dias, meses y 
# años desde la fecha de naciemineto 

print (" #Programa extra que calcula el total de dias, mese y años desde la fecha de naciemineto ")
print ("FECHA DE NACIMIENTO")
día=int(input("Ingrese el dia de su nacimiento: "))
mes=int(input("Ingrese el mes de su nacimiento: "))
años=int(input("Ingrese el año de su nacimiento: "))
print ("El mes actual tiene 30 dias (si/no)")
tipodemes =input ()
if tipodemes == "si":
 díaactual=int(input("Ingrese el día actual: "))
 mesactual=int(input("Ingrese el mes actual: "))
 mesactual1= 12-mesactual
 Añoactual=int(input("Ingrese el año actual: "))

 TolalDeAños = Añoactual-años
 TotalDeMeses = TolalDeAños*12-mesactual1
 Totaldedia = 30-díaactual
 Totaldedia1 = Totaldedia-30

 print("Usted tiene",Totaldedia1,"dias, tine",TotalDeMeses,"meses y ",TolalDeAños,"años dede su fecha de nacimiento",día,"/",mes,"/",años )

elif tipodemes == "no":
 print ("Ingrese cuantos dias tiene el mes actual")
 diames = int (input())
 díaactual=int(input("Ingrese el día actual: "))
 mesactual=int(input("Ingrese el mes actual: "))
 mesactual1= 12 - mesactual
 Añoactual=int(input("Ingrese el año actual: "))

 TolalDeAños = Añoactual-años
 TotalDeMeses = TolalDeAños*12-mesactual1
 Totaldedia = diames-díaactual
 Totaldedia1 = diames-Totaldedia

 print("Usted tiene",Totaldedia1,"dias, tines",TotalDeMeses,"meses y ",TolalDeAños,"años. Esto dede su fecha de nacimiento",día,"/",mes,"/",años )


 #Julian Hernandez. ¡Muchas gracias!..