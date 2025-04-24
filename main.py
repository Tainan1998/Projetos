import glfw
from OpenGL.GL import *
import time

from texturas import carregar_textura
from personagem import desenhar_personagem
from cenario import desenhar_cenario
from valores import GRAVIDADE, IMPULSO_PULO
from obstaculos import Obstacle
from vidas import ContadorDeVidas

def main():
    if not glfw.init():
        return

    janela = glfw.create_window(1200, 1000, "FlapX", None, None)
    if not janela:
        glfw.terminate()
        return

    glfw.make_context_current(janela)
    glfw.swap_interval(1)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Carrega texturas
    textura_personagem = carregar_textura("Skin/skin2.png")
    textura_fundo = carregar_textura("Fundo/cenario.png")
    textura_cano = carregar_textura("Objeto/obj.png")

    tempo_anterior = time.time()
    pulo = False
    velocidade = 0
    altura = 0
    pode_pular = True

    obstáculos = [Obstacle(1.2, textura_cano), Obstacle(2.5, textura_cano)]

    contador_vidas = ContadorDeVidas(3)
    tempo_invencivel = 0

    while not glfw.window_should_close(janela):
        glClearColor(0.5, 0.7, 1.0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        desenhar_cenario(textura_fundo)

        tempo_atual = time.time()
        delta_time = tempo_atual - tempo_anterior
        tempo_anterior = tempo_atual
        delta_time = min(delta_time, 0.05)

        tempo_invencivel -= delta_time

        estado_espaco = glfw.get_key(janela, glfw.KEY_SPACE)

        if estado_espaco == glfw.PRESS and pode_pular:
            pulo = True
            velocidade = IMPULSO_PULO
            pode_pular = False

        if estado_espaco == glfw.RELEASE:
            pode_pular = True

        if pulo:
            altura += velocidade * delta_time
            velocidade += GRAVIDADE * delta_time

            if altura >= 1.0:
                altura = 1.0

            if altura <= -1.0:
                if tempo_invencivel <= 0:
                    contador_vidas.perder_vida()
                    tempo_invencivel = 1.0

                    if not contador_vidas.esta_vivo():
                        print("Game Over!")
                        glfw.set_window_should_close(janela)

        y_personagem = (-0.4 + altura) + 0.3 / 2

        for obstaculo in obstáculos:
            obstaculo.mover(delta_time)
            obstaculo.desenhar()

            if obstaculo.colidiu(-0.7, y_personagem, largura_personagem=0.2, altura_personagem=0.3):
                if tempo_invencivel <= 0:
                    contador_vidas.perder_vida()
                    tempo_invencivel = 1.0

                    if not contador_vidas.esta_vivo():
                        print("Fim de Jogo!")
                        glfw.set_window_should_close(janela)

        desenhar_personagem(textura_personagem, altura, pos_x=-0.7)

        glfw.swap_buffers(janela)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()