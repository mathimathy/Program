import sqlite3
import os.path
import colorama

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
db_path = os.path.join(BASE_DIR, "data/data.db")


conn = sqlite3.connect(db_path)

def createColor(text,color,style):
    out=""
    match color:
        case "RED":
            out+=colorama.Fore.RED
        case "GREEN":
            out+=colorama.Fore.GREEN
        case "YELLOW":
            out+=colorama.Fore.YELLOW
        case "BLUE":
            out+=colorama.Fore.BLUE
        case "MAGENTA":
            out+=colorama.Fore.MAGENTA
        case "CYAN":
            out+=colorama.Fore.CYAN
        case _:
            out+=colorama.Fore.WHITE
    match style:
        case "DIM":
            out+=colorama.Style.DIM
        case "BRIGHT":
            out+=colorama.Style.BRIGHT
        case _:
            out+=colorama.Style.NORMAL

    out+=text+colorama.Style.RESET_ALL
    return out