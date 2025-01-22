def chainMod(msg, turn=20, mod=256, reverse=False):
        data = [ord(letter) for letter in msg]
        lastNumber = 1
        for _ in range(turn):
            newData=[]
            for el in data:
                newData.append((el*lastNumber)%mod)
                lastNumber=el
            if reverse: data=newData[::-1]
        return abs(sum(data)%mod)