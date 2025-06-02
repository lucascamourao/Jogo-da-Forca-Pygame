import pygame
import random

# Inicializations
pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_SIZE = screen.get_size()
pygame.display.set_caption("Jogo da Forca")
main_font = pygame.font.SysFont("arial", 45) 
font_small = pygame.font.SysFont("arial", 30) 
font_big = pygame.font.SysFont("timesnewroman", 55)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

MAX_TRIES = 6

with open("palavras.txt", "r", encoding="utf-8") as file:
    words_list = file.readlines()

random_word = random.choice(words_list).lower().strip()
tried_letters = []
correct_letters = []
wrong_letters = []
tries = 0
usou_dica = False
is_game_over = False
final_message = ""

# Loading images
background_img1 = pygame.image.load("imagens/ceu_fundo1.jpg")
background_img2 = pygame.image.load("imagens/ceu_fundo2.jpg")

background_victory = pygame.image.load("imagens/background_victory.jpg")

backgrounds = [background_img1, background_img2]

current_background = random.choice(backgrounds)

current_font_color = BLACK

if current_background == background_img2:
    current_font_color = BLACK # mudar para outros fundos

# Função para desenhar a forca e o boneco na tela
def desenhar_boneco(tentativas, curr_font_color):
    # Posição base do boneco (parte inferior do poste)
    base_x = 20
    base_y = 400

    # Poste e suporte
    pygame.draw.line(screen, curr_font_color, (base_x, base_y), (base_x + 100, base_y), 5)  # base
    pygame.draw.line(screen, curr_font_color, (base_x + 50, base_y), (base_x + 50, base_y - 250), 5)  # vertical
    pygame.draw.line(screen, curr_font_color, (base_x + 50, base_y - 250), (base_x + 150, base_y - 250), 5)  # topo
    pygame.draw.line(screen, curr_font_color, (base_x + 150, base_y - 250), (base_x + 150, base_y - 200), 5)  # corda

    if tentativas > 0:
        pygame.draw.circle(screen, curr_font_color, (base_x + 150, base_y - 175), 25, 3)  # cabeça
    if tentativas > 1:
        pygame.draw.line(screen, curr_font_color, (base_x + 150, base_y - 150), (base_x + 150, base_y - 80), 3)  # tronco
    if tentativas > 2:
        pygame.draw.line(screen, curr_font_color, (base_x + 150, base_y - 140), (base_x + 120, base_y - 110), 3)  # braço esquerdo
    if tentativas > 3:
        pygame.draw.line(screen, curr_font_color, (base_x + 150, base_y - 140), (base_x + 180, base_y - 110), 3)  # braço direito
    if tentativas > 4:
        pygame.draw.line(screen, curr_font_color, (base_x + 150, base_y - 80), (base_x + 120, base_y - 50), 3)  # perna esquerda
    if tentativas > 5:
        pygame.draw.line(screen, curr_font_color, (base_x + 150, base_y - 80), (base_x + 180, base_y - 50), 3)  # perna direita
    # Continue se quiser mais tentativas (até 9)

# Draw elements in the screen
def draw_screen():
    imagem_fundo = pygame.transform.scale(current_background, SCREEN_SIZE)

    screen.blit(imagem_fundo, (0, 0))

    titulo_render = font_big.render("JOGO DA FORCA", True, current_font_color)
    screen.blit(titulo_render, (30, 30))

    texto_tentativas = font_small.render(f"TENTATIVAS: {tries}/{MAX_TRIES}", True, current_font_color)
    screen.blit(texto_tentativas, (WIDTH - texto_tentativas.get_width() - 30, 30))

    palavra_exibida = ""

    acertos = 0
    for letra in random_word:
        if letra in correct_letters:
            palavra_exibida += letra + " "
            acertos += 1
        else:
            palavra_exibida += "_ "

    texto_palavra = main_font.render(palavra_exibida, True, current_font_color)
    screen.blit(texto_palavra, ((WIDTH - texto_palavra.get_width()) // 2, 150))
  
    letras_usadas = main_font.render("Erradas: " + ", ".join(wrong_letters), True, current_font_color)
    screen.blit(letras_usadas, ((WIDTH - letras_usadas.get_width()) // 2, 460))

    desenhar_boneco(tries, current_font_color)  

    if usou_dica:
        dica_texto = main_font.render("Dica usada!", True, RED)
        screen.blit(dica_texto, ((WIDTH - dica_texto.get_width()) // 2, 250))

    if is_game_over:
        resultado = font_big.render(final_message, True, GREEN if "ganhou" in final_message else RED)
        
        if "ganhou" in final_message:
            background_victory_renderized = pygame.transform.scale(background_victory, SCREEN_SIZE)
            screen.blit(background_victory_renderized, (0, 0))
        else:
            screen.fill((0, 0, 0)) # poderia ser uma imagem

        screen.blit(resultado, ((WIDTH - resultado.get_width()) // 2, 200))

        replay = main_font.render("Pressione 'R' para jogar novamente! ", True, WHITE)
        screen.blit(replay, ((WIDTH - replay.get_width()) // 2, 310))
    
    pygame.display.flip()

def reiniciar_jogo():
    global random_word, tried_letters, correct_letters, wrong_letters, tries, is_game_over, final_message, current_background, usou_dica
    random_word = random.choice(words_list).lower().strip()
    tried_letters = []
    correct_letters = []
    wrong_letters = []
    tries = 0
    is_game_over = False
    final_message = ""
    current_background = random.choice(backgrounds)
    usou_dica = False

# Main loop
running = True
while running:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break # close the game screen

        if event.type == pygame.KEYDOWN:
            key = event.unicode.lower() # letter 'input'

            if is_game_over and (key == "r"):
                reiniciar_jogo()
                continue

            if key == "1":
                if not usou_dica:
                    usou_dica = True
                    while True:
                        letra_dica = random.choice(list(random_word))
                        if letra_dica not in correct_letters:
                            tried_letters.append(letra_dica)
                            correct_letters.append(letra_dica)

                            if (letra_dica == "ã") or (letra_dica == "á") or (letra_dica == "à"):
                                tried_letters.append("a")
                                correct_letters.append("a")

                            if letra_dica == "a" and ("ã" in random_word):
                                tried_letters.append("ã")
                                correct_letters.append("ã")
                            break
                else:
                    continue  # já usou dica

            elif key.isalpha() and len(key) == 1:
                if key in tried_letters:
                    #letra_ja_tentada = fonte.render("Essa letra já foi tentada. ", True, VERMELHO)
                    #tela.blit(letra_ja_tentada, (30, 300))
                    continue                        
                tried_letters.append(key) 

                if key in random_word:
                    if key == "a":
                        if "ã" in random_word:
                            correct_letters.append("ã")
                        
                        if "á" in random_word:
                            correct_letters.append("á")
                            
                    elif (key == "e"):
                        if "é" in random_word:
                            correct_letters.append("é")

                    elif (key == "i"):
                        if "í" in random_word:
                            correct_letters.append("í")
                        if "ì" in random_word:
                            correct_letters.append("ì")

                    elif (key == "c"):
                        if "ç" in random_word:
                            correct_letters.append("ç")

                    correct_letters.append(key)
                else:
                    wrong_letters.append(key)
                    tries += 1

            # Check if the game is over
            if tries >= MAX_TRIES:
                final_message = "Você perdeu!"
                is_game_over = True
                
            elif all(letter in correct_letters for letter in random_word):
                final_message = "Você ganhou o jogo!"
                is_game_over = True

pygame.quit()