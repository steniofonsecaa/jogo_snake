import pygame

#Inicializando o pygame
pygame.init()

#Tela inicial
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo Snake")

#Fonte texto do título
titulo = pygame.font.SysFont("arial", 50)

#Texto menu e fonte
opcoes = ["Jogar", "Opções", "Sair"]
fonte = pygame.font.SysFont("arial", 30)

#Fonte do texto de desenvolvimento
desenvolvido = pygame.font.SysFont("arial", 15)

#Indicador de seleção do menu
indicador = pygame.Surface((25, 10))
indicador.fill((255, 255, 255))

#Loop da tela inicial
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #Desenhando o título
    titulo_texto = titulo.render("Snake Classic", True, (255, 0, 0))
    titulo_pos = titulo_texto.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 100))
    screen.blit(titulo_texto, titulo_pos)
    
    #Desenhando o texto de desenvolvimento
    desenvolvido_texto = desenvolvido.render("Desenvolvido por Stenio Fonsêca", True, (255, 255, 255))
    desenvolvido_pos = desenvolvido_texto.get_rect(center=(screen.get_width()/2, screen.get_height() - 30))
    screen.blit(desenvolvido_texto, desenvolvido_pos)

    #Desenhando o indicador de seleção do menu fazendo piscar devagar
    if pygame.time.get_ticks() % 1000 < 500:
        indicador_pos = indicador.get_rect(center=(screen.get_width()/2 - 100, screen.get_height()/2))
        screen.blit(indicador, indicador_pos)
    
    
    #Desenhando o menu
    for i, opcao in enumerate(opcoes):
        texto_menu = fonte.render(opcao, True, (255, 255, 255))
        texto_menu_pos = texto_menu.get_rect(center=(screen .get_width()/2, screen.get_height()/2 + i * 50))
        screen.blit(texto_menu, texto_menu_pos)
        
    pygame.display.update()