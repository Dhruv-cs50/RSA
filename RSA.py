from Crypto.Util import number

n_length = 2048

a = number.getPrime(n_length)
b = number.getPrime(n_length)

p = number.getPrime(1024)
g = 65537

A = (g**a) % p
B = (g**b) % p

S1 = (B**a) % p
S2 = (A**b) % p

print(S1==S2)