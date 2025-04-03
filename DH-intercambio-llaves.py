import random

# Parametros comunes, publicamente conocidos
g = 5 # Raiz primitiva modulo de 23
p = 23 # Numero primo

# Alice y Bob generan sus llaves publicas y privadas

def generar_llaves():
    llave_privada = random.randint(1, p)
    llave_publica = (g ** llave_privada) % p #g^llave_privada mod p
    return llave_privada, llave_publica

#Alice
a_privada, a_publica = generar_llaves()

# Bob
b_privada, b_publica = generar_llaves()

#Intercambiar llaves publicas y computar secreto compartido

def computar_secreto_compartido(llave_privada, llave_publica):
    return (llave_publica ** llave_privada) % p # llave_pulbica^llave_privada mod p

# Alice computa el secreto compartido
alice_secreto = computar_secreto_compartido(a_privada, b_publica)

# Bob computa el secreto compartido
bob_secreto = computar_secreto_compartido(b_privada, a_publica)

print("Secreto compartido de Alice:", alice_secreto)
print("Secreto compartido de Bob:", bob_secreto)

#Validar el secreto compartido