import sqlite3
import os.path
import colorama

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data.db")


conn = sqlite3.connect(db_path)

def createColor(text,color,style):
    out=""
    if color=="RED":
        out+=colorama.Fore.RED
    elif color=="GREEN":
        out+=colorama.Fore.GREEN
    elif color=="YELLOW":
        out+=colorama.Fore.YELLOW
    elif color=="BLUE":
        out+=colorama.Fore.BLUE
    elif color=="MAGENTA":
        out+=colorama.Fore.MAGENTA
    elif color=="CYAN":
        out+=colorama.Fore.CYAN
    elif color=="WHITE":
        out+=colorama.Fore.WHITE
    if style=="DIM":
        out+=colorama.Style.DIM
    elif style=="NORMAL":
        out+=colorama.Style.NORMAL
    elif style=="BRIGHT":
        out+=colorama.Style.BRIGHT
    out+=text+colorama.Style.RESET_ALL
    return out