import aes
from matrice import Matrice
key = [Matrice([0x6b,0x2c,0x3e,0x9f]),Matrice([0x23,0x5e,0x07,0x03]),Matrice([0xa9,0xc3,0x2f,0x11]),Matrice([0x13,0x4b,0x5d,0x9a])]
a = aes.AES(key)
msg="Coucou les amis ça va ?"
print(msg)
crypted = a.cipher(msg)
print(crypted[0],crypted[1])
new_msg = a.decipher(crypted)
print(new_msg)