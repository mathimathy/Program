str_var={}
int_var={}
bool_var={}
float_var={}
def traitement_fichier():
    with open(input("file> ")) as f:
        code = f.read()
    code = code.split("\n")
    array_code=[]
    for line in code:
        line = line.split(".")
        print(line)
        array_code.append(line)
    return array_code
def traiement_code(code, line=0, incondition=False, inelse=False):
    while line < len(code):
        if(code[line][0]=="print"):
            if(code[line][1]=="str"):
                print(str_var[code[line][2]])
            elif(code[line][1]=="int"):
                print(int_var[code[line][2]])
            elif(code[line][1]=="float"):
                print(float_var[code[line][2]])
            elif(code[line][1]=="bool"):
                print(bool_var[code[line][2]])
            else:
                print(code[line][1])
        elif(code[line][0]=="jump"):
            if incondition==False and inelse==False:
                line=int(code[line][1])
            elif incondition or inelse:
                testline=line
                while testline<int(code[line][1]):
                    if code[testline][0]=="end":
                        traiement_code(code, int(code[line][1], False, False))
                        return
        elif(code[line][0]=="stop"):
            line=len(code)+10
        elif(code[line][0]=="str"):
            str_var[code[line][1]]=code[line][2]
        elif(code[line][0]=="int"):
            int_var[code[line][1]]=int(code[line][2])
        elif(code[line][0]=="bool"):
            bool_var[code[line][1]]=bool(code[line][2])
        elif(code[line][0]=="float"):
            float_var[code[line][1]]=float(code[line][2])
        elif(code[line][0]=="toStr"):
            if(code[line][1]=="fromInt"):
                str_var[code[line][2]]=str(int_var[code[line][2]])
                int_var.pop(code[line][2])
            if(code[line][1]=="fromBool"):
                str_var[code[line][2]]=str(bool_var[code[line][2]])
                bool_var.pop(code[line][2])
            if(code[line][1]=="fromFloat"):
                str_var[code[line][2]]=str(float_var[code[line][2]])
                float_var.pop(code[line][2])
        elif(code[line][0]=="toInt"):
            if(code[line][1]=="fromStr"):
                int_var[code[line][2]]=int(str_var[code[line][2]])
                str_var.pop(code[line][2])
            if(code[line][1]=="fromBool"):
                int_var[code[line][2]]=int(bool_var[code[line][2]])
                bool_var.pop(code[line][2])
            if(code[line][1]=="fromFloat"):
                int_var[code[line][2]]=int(float_var[code[line][2]])
                float_var.pop(code[line][2])
        elif(code[line][0]=="toBool"):
            if(code[line][1]=="fromInt"):
                bool_var[code[line][2]]=bool(int_var[code[line][2]])
                int_var.pop(code[line][2])
            if(code[line][1]=="fromStr"):
                bool_var[code[line][2]]=bool(str_var[code[line][2]])
                str_var.pop(code[line][2])
            if(code[line][1]=="fromFloat"):
                bool_var[code[line][2]]=bool(float_var[code[line][2]])
                float_var.pop(code[line][2])
        elif(code[line][0]=="toFloat"):
            if(code[line][1]=="fromInt"):
                float_var[code[line][2]]=float(int_var[code[line][2]])
                int_var.pop(code[line][2])
            if(code[line][1]=="fromBool"):
                float_var[code[line][2]]=float(bool_var[code[line][2]])
                bool_var.pop(code[line][2])
            if(code[line][1]=="fromStr"):
                float_var[code[line][2]]=float(str_var[code[line][2]])
                str_var.pop(code[line][2])
        elif(code[line][0]=="if"):
            if(code[line][1]=="equal"):
                if(code[line][2]=="str"):
                    if(code[line][4]=="str"):
                        if(str_var[code[line][3]]==str_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="int" or code[line][4]=="bool" or code[line][4]=="float"):
                        print("[ERROR] in a if.equal condition, you need to enter same var type !")
                    else:
                        if(str_var[code[line][3]]==code[line][4]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="int"):
                    if(code[line][4]=="int"):
                        if(int_var[code[line][3]]==int_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="float"):
                        print("[ERROR] in a if.equal condition, you need to enter same var type !")
                    else:
                        if(int_var[code[line][3]]==code[line][4]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="bool"):
                    if(code[line][4]=="bool"):
                        if(bool_var[code[line][3]]==bool_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="int" or code[line][4]=="float"):
                        print("[ERROR] in a if.equal condition, you need to enter same var type !")
                    else:
                        if(bool_var[code[line][3]]==code[line][4]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="float"):
                    if(code[line][4]=="float"):
                        if(float_var[code[line][3]]==float_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="int"):
                        print("[ERROR] in a if.equal condition, you need to enter same var type !")
                    else:
                        if(float_var[code[line][3]]==code[line][4]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
            elif(code[line][1]=="<"):
                if(code[line][2]=="int"):
                    if(code[line][4]=="int"):
                        if(int_var[code[line][3]]<int_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="float"):
                        print("[ERROR] in a if.< condition, you need to enter same var type !")
                    else:
                        if(int_var[code[line][3]]<int(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="float"):
                    if(code[line][4]=="float"):
                        if(float_var[code[line][3]]<float_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="int"):
                        print("[ERROR] in a if.< condition, you need to enter same var type !")
                    else:
                        if(float_var[code[line][3]]<float(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
            elif(code[line][1]==">"):
                if(code[line][2]=="int"):
                    if(code[line][4]=="int"):
                        if(int_var[code[line][3]]>int_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="float"):
                        print("[ERROR] in a if.> condition, you need to enter same var type !")
                    else:
                        if(int_var[code[line][3]]>int(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="float"):
                    if(code[line][4]=="float"):
                        if(float_var[code[line][3]]>float_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="int"):
                        print("[ERROR] in a if.> condition, you need to enter same var type !")
                    else:
                        if(float_var[code[line][3]]>float(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
            elif(code[line][1]=="<="):
                if(code[line][2]=="int"):
                    if(code[line][4]=="int"):
                        if(int_var[code[line][3]]<=int_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="float"):
                        print("[ERROR] in a if.<= condition, you need to enter same var type !")
                    else:
                        if(int_var[code[line][3]]<=int(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="float"):
                    if(code[line][4]=="float"):
                        if(float_var[code[line][3]]<=float_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="int"):
                        print("[ERROR] in a if.<= condition, you need to enter same var type !")
                    else:
                        if(float_var[code[line][3]]<=float(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
            elif(code[line][1]==">="):
                if(code[line][2]=="int"):
                    if(code[line][4]=="int"):
                        if(int_var[code[line][3]]>=int_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="float"):
                        print("[ERROR] in a if.>= condition, you need to enter same var type !")
                    else:
                        if(int_var[code[line][3]]>=int(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                if(code[line][2]=="float"):
                    if(code[line][4]=="float"):
                        if(float_var[code[line][3]]>=float_var[code[line][5]]):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
                    elif(code[line][4]=="str" or code[line][4]=="bool" or code[line][4]=="int"):
                        print("[ERROR] in a if.>= condition, you need to enter same var type !")
                    else:
                        if(float_var[code[line][3]]>=float(code[line][4])):
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                findline+=1
                            copyofcode = code
                            traiement_code(copyofcode, line+1, True)
                            return
                        else:
                            findline=line
                            cond = True
                            while cond:
                                if code[findline][0]=="else" or code[findline][0]=="end":
                                    cond=False
                                else:
                                    findline+=1
                            if code[findline][0]=="end":
                                line=findline
                            elif code[findline][0]=="else":
                                traiement_code(code, findline)
                                return
        elif(code[line][0]=="end"):
            traiement_code(code, line+1)
            return
        elif(code[line][0]=="else"):
            if incondition:
                cond = True
                findline=line
                while cond:
                    if code[findline][0]=="end":
                        cond=False
                    else:
                        findline+=1
                traiement_code(code, findline+1)
                return
            elif incondition==False:
                copyOfCode=code
                traiement_code(copyOfCode, line+1, incondition=False, inelse=True)
                return
#calc
        
#input
        line+=1
code=traitement_fichier()
def main():
    traiement_code(code)

main()