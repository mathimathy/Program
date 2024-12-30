import datetime
def Log(function):
    def wrapper(*args):
        func = function(*args)
        arguments=args
        with open("log.txt", "a") as f:
            f.write(f"{function} executed at {datetime.datetime.now().isoformat()} with arguments {arguments}\n / RESULTS: {func}\n")
        return func

    return wrapper

class ErrorManager:
    def __init__(self, file):
        self.errorCode = self.readFile(file)

    def readFile(self, file):
        with open(file, "r") as f:
            read = f.read()
        read = read.split("\n")
        errorCode={}
        for el in read:
            el=el.split("/")
            errorCode[el[0]]=el[1]
        return errorCode

    def error(self, idN):
        return Error(idN, self.errorCode[str(idN)])



class Error:
    def __init__(self, idN, msg):
        self.id=idN
        self.msg=msg

    def __str__(self):
        return f"FATAL ERROR: Error code {self.id}: {self.msg}"