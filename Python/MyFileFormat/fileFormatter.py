import aes
import sign
class FileFormatter:
    def __init__(self, key):
        self.key = key
    
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