'''
texto = "arquitectuta"
vocales = "aeiou"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1
print("cantidad de vocales", contador) 






for i in range(21):  #desde 0 hasta 21 inclusive
     if i % 2 == 0:
      print (i)


'''
 

contrase = "chauchau"
entrada=""
intentos=0

while entrada!=contrase and intentos < 3 :
    entrada = input("ingresa su contrase: ")      
    if entrada != contrase:
         print("incorrecta-siga participando:")
         intentos +=1
if entrada == contrase:
       print("correcto!!!")
else:
    print("no hay mas intentos.")
  

  