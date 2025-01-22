class Queue:
    def __init__(self):
        self._d = []
    
    def push(self, value):
        self._d.append(value)
    
    def pop(self):
        if len(self._d)>0:
            data = self._d[0]
            del self._d[0]
            return data
        else:
            raise IndexError("You're trying to pop the queue but it's empty")
    
    def clear(self):
        self._d=[]