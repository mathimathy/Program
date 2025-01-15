import sign
s = sign.Sign()
message="Salut les amis !"
signature = s.sign(message)
message="Salut"
print(s.checkSign(message, signature))