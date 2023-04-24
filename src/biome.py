class BiomeProperties:

    def __init__(self):
        self.topLayer = "grass"
        self.fillerLayer = "dirt"
        self.canSpread = False

    def setProps(self, tL:str, fL:str, cS:bool):
        self.topLayer = tL
        self.fillerLayer = fL
        self.canSpread = cS

def getBiome(p1, p2, p3):
    b = BiomeProperties()
    b.setProps(p1, p2, p3)
    return b