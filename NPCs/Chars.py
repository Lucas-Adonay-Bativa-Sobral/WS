
class Char:
    def __init__(self, name, forca, agilidade, destreza, inteligencia, sabedoria,
                 level, pontos, alive, skill, magicka, life, stamina):

        self.name = name
        self.forca = forca
        self.agilidade = agilidade
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.level = level
        self.pontos = pontos
        self.skill = skill
        self.magicka = magicka
        self.life = life
        self.stamina = stamina
        self.alive = alive
        # Metodos set

    def setName(self, name):
        self.name = name

    def setForca(self, forca):
        self.forca = forca

    def setAgilidade(self, agilidade):
        self.agilidade = agilidade

    def setDestreza(self, destreza):
        self.destreza = destreza

    def setInteligencia(self, inteligencia):
        self.inteligencia = inteligencia

    def setSabedoria(self, sabedoria):
        self.sabedoria = sabedoria

    def setLevel(self, level):
        self.level = level

    def setPontos(self, pontos):
        self.pontos = pontos

    def setSkill(self, skill):
        self.skill = skill

    def setMagicka(self, magicka):
        self.magicka = magicka

    def setLife(self, life):
        self.life = life

    def setStamina(self, stamina):
        self.stamina = stamina

        # Metodos get

    def getNome(self, nome):
        return self.nome

    def getForca(self, forca):
        return self.forca

    def getAgilidade(self, agilidade):
        return self.agilidade

    def getDestreza(self, destreza):
        return self.destreza

    def getInteligencia(self, inteligencia):
        return self.inteligencia

    def getSabedoria(self, sabedoria):
        return self.sabedoria

    def getLevel(self, level):
        return self.level

    def getPontos(self, pontos):
        return self.pontos

    def getSkill(self, skill):
        return self.skill

    def getMagicka(self, magicka):
        return self.magicka

    def getLife(self, life):
        return self.life

    def getStamina(self, stamina):
        return self.stamina
