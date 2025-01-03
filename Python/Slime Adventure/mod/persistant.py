class Persistant:
    def __init__(self):
        self.pers={}

    def set(self, name, value):
        self.pers[name]=value

    def get(self,name):
        return self.pers[name]