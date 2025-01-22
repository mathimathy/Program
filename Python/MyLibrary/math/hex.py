class Hex:
    def __init__(self, value):
        if type(value)==type(int):
            self._value = value
        else:
            raise TypeError("value should be an int not a "+type(value))
    
    def __add__(self, other):
        return self^other
    
    def __radd__(self, other):
        return self+other
    
    def __mod__(self, other):
        return self._value^other
    
    def __rmod__(self, other):
        return other^self._value
    
    def __mul__(self, other):
        if type(other)==type(self):
            p = 0b100011011
            m=0
            for i in range(8):
                m = m<<1
                if m & 0b100000000:
                    m = m^p
                if other._value & 0b010000000:
                    m = m^self._value
                other._value=other._value<<1
            return m
        else:
            raise ArithmeticError(f"Can't multiply {type(self)} and {type(other)}")
    
    def __str__(self):
        return hex(self._value)
    
    def __format__(self, format_spec):
        return hex(self._value)
    
    def __int__(self):
        return self._value
    
    def __float__(self):
        return float(self._value)