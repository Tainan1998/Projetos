from OpenGL.GL import *

def desenhar_objeto(textura_id, largura=0.15, altura=0.5):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex2f(-largura, -altura)
    glTexCoord2f(1.0, 0.0); glVertex2f(largura, -altura)
    glTexCoord2f(1.0, 1.0); glVertex2f(largura, altura)
    glTexCoord2f(0.0, 1.0); glVertex2f(-largura, altura)
    glEnd()

    glDisable(GL_TEXTURE_2D)
