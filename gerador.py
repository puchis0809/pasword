import random
contraseña =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int (input("cuantos caracteres nesecitas"))
pasword = ""
for i in range(long):
    pasword += random.choice(contraseña)
    
print(pasword)