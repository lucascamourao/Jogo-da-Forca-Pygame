import pygame
import random

# Inicializações
pygame.init()
LARGURA, ALTURA = 900, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
TAMANHO_TELA = tela.get_size()
pygame.display.set_caption("Jogo da Forca")
fonte = pygame.font.SysFont("arial", 45) 
fonte_pequena = pygame.font.SysFont("arial", 30) 
fonte_grande = pygame.font.SysFont("timesnewroman", 55)

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Lógica da palavra
MAX_TENTATIVAS = 9
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    lista_palavras = arquivo.readlines()

palavra_aleatoria = random.choice(lista_palavras).lower().strip()
letras_tentadas = []
letras_acertadas = []
letras_erradas = []
tentativas = 0
usou_dica = False
fim_de_jogo = False
mensagem_final = ""

# Carregando as fotos
imagem_fundo1 = pygame.image.load("imagens/ceu_fundo1.jpg")
imagem_fundo2 = pygame.image.load("imagens/ceu_fundo2.jpg")

background_victory = pygame.image.load("imagens/background_victory.jpg")

backgrounds = [imagem_fundo1, imagem_fundo2]

curr_background = random.choice(backgrounds)

curr_font_color = BLACK

if curr_background == imagem_fundo2:
    curr_font_color = BLACK # mudar para outros fundos

# Função para desenhar a forca e o boneco na tela
def desenhar_boneco(tentativas, curr_font_color):
    # Posição base do boneco (parte inferior do poste)
    base_x = 20
    base_y = 400

    # Poste e suporte
    pygame.draw.line(tela, curr_font_color, (base_x, base_y), (base_x + 100, base_y), 5)  # base
    pygame.draw.line(tela, curr_font_color, (base_x + 50, base_y), (base_x + 50, base_y - 250), 5)  # vertical
    pygame.draw.line(tela, curr_font_color, (base_x + 50, base_y - 250), (base_x + 150, base_y - 250), 5)  # topo
    pygame.draw.line(tela, curr_font_color, (base_x + 150, base_y - 250), (base_x + 150, base_y - 200), 5)  # corda

    if tentativas > 0:
        pygame.draw.circle(tela, curr_font_color, (base_x + 150, base_y - 175), 25, 3)  # cabeça
    if tentativas > 1:
        pygame.draw.line(tela, curr_font_color, (base_x + 150, base_y - 150), (base_x + 150, base_y - 80), 3)  # tronco
    if tentativas > 2:
        pygame.draw.line(tela, curr_font_color, (base_x + 150, base_y - 140), (base_x + 120, base_y - 110), 3)  # braço esquerdo
    if tentativas > 3:
        pygame.draw.line(tela, curr_font_color, (base_x + 150, base_y - 140), (base_x + 180, base_y - 110), 3)  # braço direito
    if tentativas > 4:
        pygame.draw.line(tela, curr_font_color, (base_x + 150, base_y - 80), (base_x + 120, base_y - 50), 3)  # perna esquerda
    if tentativas > 5:
        pygame.draw.line(tela, curr_font_color, (base_x + 150, base_y - 80), (base_x + 180, base_y - 50), 3)  # perna direita
    # Continue se quiser mais tentativas (até 9)

# Função para desenhar os elementos na tela
def desenhar_tela():
    imagem_fundo = pygame.transform.scale(curr_background, TAMANHO_TELA)

    tela.blit(imagem_fundo, (0, 0))

    titulo_render = fonte_grande.render("JOGO DA FORCA", True, curr_font_color)
    tela.blit(titulo_render, (30, 30))

    texto_tentativas = fonte_pequena.render(f"TENTATIVAS: {tentativas}/{MAX_TENTATIVAS}", True, curr_font_color)
    tela.blit(texto_tentativas, (LARGURA - texto_tentativas.get_width() - 30, 30))

    palavra_exibida = ""

    acertos = 0
    for letra in palavra_aleatoria:
        if letra in letras_acertadas:
            palavra_exibida += letra + " "
            acertos += 1
        else:
            palavra_exibida = palavra_exibida +"_ "

    texto_palavra = fonte.render(palavra_exibida, True, curr_font_color)
    tela.blit(texto_palavra, ((LARGURA - texto_palavra.get_width()) // 2, 150))
  
    letras_usadas = fonte.render("Erradas: " + ", ".join(letras_erradas), True, curr_font_color)
    tela.blit(letras_usadas, ((LARGURA - letras_usadas.get_width()) // 2, 460))

    desenhar_boneco(tentativas, curr_font_color)  

    if usou_dica:
        dica_texto = fonte.render("Dica usada!", True, RED)
        tela.blit(dica_texto, ((LARGURA - dica_texto.get_width()) // 2, 250))

    if fim_de_jogo:
        resultado = fonte_grande.render(mensagem_final, True, GREEN if "ganhou" in mensagem_final else RED)
        
        #tela.fill(BRANCO) # tela de fundo

        if "ganhou" in mensagem_final:
            background_victory_renderized = pygame.transform.scale(background_victory, TAMANHO_TELA)
            tela.blit(background_victory_renderized, (0, 0))
            #tela.fill((50, 30, 20)) # poderia ser uma imagem
        else:
            tela.fill((0, 0, 0)) # poderia ser uma imagem

        tela.blit(resultado, ((LARGURA - resultado.get_width()) // 2, 250))

        replay = fonte.render("Pressione 'R' para jogar novamente! ", True, WHITE)
        tela.blit(replay, ((LARGURA - replay.get_width()) // 2, 350))
    
    pygame.display.flip()

def reiniciar_jogo():
    global palavra_aleatoria, letras_tentadas, letras_acertadas, letras_erradas, tentativas, fim_de_jogo, mensagem_final, curr_background
    palavra_aleatoria = random.choice(lista_palavras).lower().strip()
    letras_tentadas = []
    letras_acertadas = []
    letras_erradas = []
    tentativas = 0
    fim_de_jogo = False
    mensagem_final = ""
    curr_background = random.choice(backgrounds)

# Loop principal
rodando = True
while rodando:
    desenhar_tela()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            break

        if evento.type == pygame.KEYDOWN and not fim_de_jogo:
            letra = evento.unicode.lower() # INPUT DA LETRA

            if fim_de_jogo and (letra == "R"): # não muda?
                reiniciar_jogo()
                continue

            if letra == "1":
                if not usou_dica:
                    usou_dica = True
                    while True:
                        letra_dica = random.choice(list(palavra_aleatoria))
                        if letra_dica not in letras_acertadas:
                            letras_tentadas.append(letra_dica)
                            letras_acertadas.append(letra_dica)

                            if (letra_dica == "ã") or (letra_dica == "á") or (letra_dica == "à"):
                                letras_tentadas.append("a")
                                letras_acertadas.append("a")

                            if letra_dica == "a" and ("ã" in palavra_aleatoria):
                                letras_tentadas.append("ã")
                                letras_acertadas.append("ã")
                            break
                else:
                    continue  # já usou dica
            elif letra.isalpha() and len(letra) == 1:
                if letra in letras_tentadas:
                    #letra_ja_tentada = fonte.render("Essa letra já foi tentada. ", True, VERMELHO)
                    #tela.blit(letra_ja_tentada, (30, 300))
                    continue                        
                letras_tentadas.append(letra) 

                if letra in palavra_aleatoria:
                    if letra == "a":
                        if "ã" in palavra_aleatoria:
                            letras_acertadas.append("ã")
                        
                        if "á" in palavra_aleatoria:
                            letras_acertadas.append("á")
                            
                    elif (letra == "e"):
                        if "é" in palavra_aleatoria:
                            letras_acertadas.append("é")

                    elif (letra == "i"):
                        if "í" in palavra_aleatoria:
                            letras_acertadas.append("í")
                        if "ì" in palavra_aleatoria:
                            letras_acertadas.append("ì")

                    elif (letra == "c"):
                        if "ç" in palavra_aleatoria:
                            letras_acertadas.append("ç")

                    letras_acertadas.append(letra)
                else:
                    letras_erradas.append(letra)
                    tentativas += 1

            # Checagem de fim de jogo
            if tentativas >= MAX_TENTATIVAS:
                mensagem_final = "Você perdeu!"
                fim_de_jogo = True
                
            elif all(letra in letras_acertadas for letra in palavra_aleatoria):
                mensagem_final = "Você ganhou o jogo!"
                fim_de_jogo = True

pygame.quit()