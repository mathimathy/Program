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

def sha256(msg):
	def init(m):
		basebinary = "".join([bin(ord(char)) for char in m]).replace("0b", "")
		words=[]
		while len(basebinary)!=0:
			print(basebinary)
			if len(basebinary)<=501:
				binary=basebinary
				basebinary=""
			else:
				binary=basebinary[:501]
				basebinary=basebinary[501:]
			size = len(binary)
			sizeB = bin(size)[2:]
			binary+="1"+"".join(["O" for _ in range(512-(1+size+len(sizeB)))])+sizeB
			words.append("0b"+binary)
		print(words)
	def rotr(n, amount):
		r=n%(2**amount)
		n=n//(2**amount)
		n+=r*(2**(32-amount))
		return n
	init(msg)