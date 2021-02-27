colones = input("¿Cuántos colones salvadoreños tienes? ")
colones = float(colones)
valor_dolar=8.75
dolares= colones / valor_dolar
dolares = round(dolares,2)
dolares= str(dolares)
print("Tienes $" + dolares + " dólares" )

dolares = input("¿Cuántos USD tienes? ")
dolares=float(dolares)
valor_colon=0.11
colones = dolares / valor_colon
colones = round(colones,2)
colones=str(colones)
print("Tienes ¢ " + colones + " colones")