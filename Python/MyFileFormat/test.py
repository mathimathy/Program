def multiply(a,b):
    p = 0b100011011
    m=0
    for i in range(8):
        m = m<<1
        if m & 0b100000000:
            m = m^p
        if b & 0b010000000:
            m = m^a
        b=b<<1
    return m
def subProduct(line, column):
    result=0
    for i in range(len(line)):
        result^=multiply(line[i],column[i])
    return result
print(subProduct([0x02,0x03,0x01,0x01],[0x87,0x6e,0x46,0xa6]))