from MyLibrary.crypto import aes, sign
from MyLibrary.math.matrice import Matrice
import random
import pickle
class FileFormatter:
    def __init__(self, key=None):
        if key == None:
            try:
                with open("/home/mathias/key", "rb") as f:
                    key=pickle.load(f)
            except:
                key = self.generateKey()
        self.key = key

    
    def generateKey(self):
        return [Matrice([random.randint(0,255) for _ in range(4)]) for _ in range(4)]
    
    def save(self, data, outputFile):
        a = aes.AES(self.key)
        s = sign.Sign()
        signature = s.sign(data)
        data = a.cipher(data)
        storage=(data,signature,s.rsa.public)

        with open(outputFile, "wb+") as f:
            pickle.dump(storage, f)
        
        with open("/home/mathias/key", "wb+") as f:
            pickle.dump(self.key, f)
    
    def translateToETF(self, inFile, outFile):
        with open(inFile) as f:
            data=f.read()
            self.save(data, outFile)
    
    def translateToTXT(self, inFile, outFile):
        data=self.load(inFile)
        with open(outFile) as f:
            f.save(data)

    def load(self, file):
        with open(file, 'rb') as f:
            fileData = pickle.load(f)
            data = fileData[0]
            signature = fileData[1]
            publicKey = fileData[2]
            a = aes.AES(self.key)
            s = sign.Sign(None, publicKey)
            data = a.decipher(data)
            if s.checkSign(data, signature):
                return data
            else:
                return "Wrong Signature"