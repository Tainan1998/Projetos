from OpenGL.GL import *

def desenhar_personagem(textura_id, altura, pos_x=0.0):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    largura = 0.1
    altura_sprite = 0.3

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(pos_x -largura, -0.4 + altura, 0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(pos_x +largura, -0.4 + altura, 0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(pos_x +largura, -0.4 + altura_sprite + altura, 0)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(pos_x -largura, -0.4 + altura_sprite + altura, 0)

    glEnd()

    glDisable(GL_TEXTURE_2D)
