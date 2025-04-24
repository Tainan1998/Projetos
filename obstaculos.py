import random
from OpenGL.GL import *
from objetos import desenhar_objeto

DISTANCIA_ANDAR = 1.2

class Obstacle:
    def __init__(self, x_pos, textura_cano):
        self.x_pos = x_pos
        self.altura_topo = random.uniform(0.3, 0.7)
        self.altura_inferior = self.altura_topo - DISTANCIA_ANDAR
        self.textura_cano = textura_cano
        self.largura = 0.3

    def mover(self, delta_time):
        self.x_pos -= 0.8 * delta_time
        if self.x_pos < -1.0:
            self.x_pos = 1.2
            self.altura_topo = random.uniform(0.3, 0.7)
            self.altura_inferior = self.altura_topo - DISTANCIA_ANDAR

    def desenhar(self):
        glPushMatrix()
        glTranslatef(self.x_pos, self.altura_topo, 0)
        desenhar_objeto(self.textura_cano, largura=self.largura, altura=0.6)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x_pos, self.altura_inferior, 0)
        desenhar_objeto(self.textura_cano, largura=self.largura, altura=0.6)
        glPopMatrix()

    def colidiu(self, pos_x, pos_y, largura_personagem=0.1, altura_personagem=0.1):
        metade_largura = self.largura / 2
        dentro_horizontal = (
                pos_x + largura_personagem / 2 > self.x_pos - metade_largura and
                pos_x - largura_personagem / 2 < self.x_pos + metade_largura
        )

        # Limites verticais da abertura entre os obstáculos
        topo_inferior = self.altura_inferior + 0.3  # topo do cano de baixo
        base_superior = self.altura_topo - 0.3  # base do cano de cima

        fora_abertura = (
                pos_y + altura_personagem / 2 > base_superior or
                pos_y - altura_personagem / 2 < topo_inferior
        )

        return dentro_horizontal and fora_abertura
