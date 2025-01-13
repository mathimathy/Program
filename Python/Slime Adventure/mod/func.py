def clear():
    print("\n"*50)

def verifiedInput(firstMsg: str, possib: list, mustRedo: bool=True, redoMsg: str="", replaceTxt: bool=False):
    var=input(firstMsg)
    possib = [str(el) for el in possib]
    if var not in possib:
        if mustRedo:
            if replaceTxt:
                return verifiedInput(redoMsg, possib)
            else:
                return verifiedInput(firstMsg, possib)
        else:
            if redoMsg!="":
                print(redoMsg)
            return None
    return var