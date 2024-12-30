class Command:
    def __init__(self):
        self.isInit = False
    def init(self):
        if self.isInit:
            self.isInit = False
            return "The processus is shutdown"
        else:
            self.isInit= True
            return "The processus is started"