import game
from mod import persistant

if __name__=="__main__":
    game_engine=game.Game()
    game_engine.start()
    PERSISTANT=persistant.Persistant()