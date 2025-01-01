import game
import mod.persistant as persistant

if __name__=="__main__":
    gameEngine=game.Game()
    gameEngine.start()
    PERSISTANT=persistant.Persistant()