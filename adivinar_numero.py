# programa para adivinar un número

import random

print("-------------------------------------")
print("-------- ADIVINA EL NÚMERO ----------")
print("-------------------------------------")

MIN = 50
MAX = 100

numero_secreto = random.choice(range(MIN,MAX))
max_intentos = 3
num_intentos = 0

while True:
    intento = int(input(f"\nAdivina un número entre {MIN} y {MAX}: "))
    num_intentos += 1
    
    if intento==numero_secreto:
        print("Felicitaciones, su intento es correcto!")
        print(f"El numero_secreto era {numero_secreto}")
        break
    if num_intentos==max_intentos:
        print("Lo siento, no tiene mas intentos!")
        print(f"El numero_secreto era {numero_secreto}")
        break