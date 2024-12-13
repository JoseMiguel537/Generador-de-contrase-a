import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

Longitud = int(input("elige la longitud de tu contraseña"))
contraseña = ""

for i in range(Longitud):
    contraseña = contraseña + (random.choice(caracteres))

print ("la contraseña segura es:",contraseña)
