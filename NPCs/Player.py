
from chars import Chars

class Player(Chars):
    def __init__(self, experiencia, nextlevel, levelup, name, forca, agilidade, destreza, inteligencia, sabedoria,
                 level, pontos, alive, skill, magicka, life, stamina):

        super().__init__(name, forca, agilidade, destreza, inteligencia, sabedoria,
                 level, pontos, alive, skill, magicka, life, stamina)

        self.experiencia = experiencia
        self.nextlevel = nextlevel
        self.levelup = levelup

        # Metodos set

    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def setNextlevel(self, nextlevel):
        self.nextlevel = nextlevel

    def setLeelup(self, levelup):
        self.levelup = levelup

        # Metodos get

    def getExperiencia(self, experiencia):
        return self.experiencia

    def getNextlevel(self, nextlevel):
        return self.nextlevel

    def getLevelup(self, levelup):
        return self.levelup
