class ContadorDeVidas:
    def __init__(self, vidas_iniciais=3):
        self.vidas = vidas_iniciais

    def perder_vida(self):
        if self.vidas > 0:
            self.vidas -= 1

    def esta_vivo(self):
        return self.vidas > 0
