import aes
import sign
from matrice import Matrice
import random
class FileFormatter:
    def __init__(self, key):
        if key == None:
            key = self.generateKey()
        self.key = key
    
    def generateKey(self):
        return [Matrice([random.randint(0,255) for _ in range(4)]) for _ in range(4)]
    
    def save(self, data, outputFile):
        a = aes.AES(self.key)
        s = sign.Sign()
        signature = s.sign(data)
        data = a.cipher(data)

        with open(outputFile, "w") as f:
            f.write(f"{a.invCreateMsg(data)}/s/{signature}/k/{s.rsa.public}")

    def load(self, file):
        with open(file, 'r') as f:
            fileData = f.read().split("/s/")
            data = fileData[0]
            fileData = fileData[1].split("/k/")
            signature = int(fileData[0])
            publicKey = fileData[1][1:-1].split(",")
            publicKey = (int(publicKey[0]), int(publicKey[1]))
            a = aes.AES(self.key)
            s = sign.Sign(None, publicKey)
            data = a.decipher(a.createMsg(data))
            if s.checkSign(data, signature):
                return data
            else:
                return "Wrong Signature"