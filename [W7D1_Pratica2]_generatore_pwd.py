import random
import string

def pwd_generator():
    print ('Benvenuto!')

ascii_chars = string.digits + string.ascii_letters + string.punctuation
alphaum_chars = string.ascii_letters

print ('Benvenuto!')
print ('Con questo programma puoi generare una password!')

if input ('Ne desideri una semplice o più complessa? Rispondi con S o C: ') == 's':
    lunghezza = 8
    tipo = alphaum_chars
else:
    lunghezza = 15
    tipo = ascii_chars

pwd = ''
counter = 0

while counter < lunghezza:
    char = random.choice(tipo)
    pwd += char
    counter += 1

print ('La password generata è:', pwd)