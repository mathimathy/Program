import rsa
class Sign:
    def __init__(self, createKey=True, public=None,private=None):
        self.rsa = rsa.RSA()
        if createKey:
            self.rsa.createKey()
        else:
            self.rsa.public = public
            self.rsa.private = private


    def hash(self, msg, turn=20):
        data = [ord(letter) for letter in msg]
        lastNumber = 1
        for _ in range(turn):
            newData=[]
            for el in data:
                newData.append((el*lastNumber)%256)
                lastNumber=el
            #data=newData[::-1]
        return abs(sum(data)%256)
        

    def sign(self, msg):
        hashedMsg = self.hash(msg)
        signed = self.rsa.cipher(hashedMsg, self.rsa.private)
        return signed
    
    def checkSign(self, msg, signed):
        hashedMsg = self.hash(msg)
        unsigned = self.rsa.decipher(signed, self.rsa.public)
        return hashedMsg==unsigned