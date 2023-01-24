import pygame

#Inicializando o pygame
pygame.init()

#Tela inicial
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo Snake")

#Título do jogo
titulo = pygame.font.SysFont("arial", 50)
titulo_texto = titulo.render("Snake Classic", True, (255, 0, 0))
titulo_pos = titulo_texto.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 100))
screen.blit(titulo_texto, titulo_pos)

#Indicador do menu
seta = pygame.Surface((25, 10))
seta.fill((255, 255, 255))
seta_pos = seta.get_rect(center=(screen.get_width()/2 - 70, screen.get_height()/2))
screen.blit(seta, seta_pos)

#Texto menu
opcoes = ["Jogar", "Opções", "Sair"]
fonte = pygame.font.SysFont("arial", 30)
for i, opcao in enumerate(opcoes):
    texto_menu = fonte.render(opcao, True, (255, 255, 255))
    texto_menu_pos = texto_menu.get_rect(center=(screen .get_width()/2, screen.get_height()/2 + i * 50))
    screen.blit(texto_menu, texto_menu_pos)

#Texto de desenvolvimento
desenvolvido = pygame.font.SysFont("arial", 15)
desenvolvido_texto = desenvolvido.render("Desenvolvido por Stenio Fonsêca", True, (255, 255, 255))
desenvolvido_pos = desenvolvido_texto.get_rect(center=(screen.get_width()/2, screen.get_height() - 30))
screen.blit(desenvolvido_texto, desenvolvido_pos)


#Loop da tela inicial
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()