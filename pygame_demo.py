import pygame
import sys

# Inicializar pygame
pygame.init()

# Tamaño de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("PONG - por Josue")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Paletas
paleta_ancho, paleta_alto = 10, 100
paleta1 = pygame.Rect(50, alto // 2 - 50, paleta_ancho, paleta_alto)
paleta2 = pygame.Rect(ancho - 60, alto // 2 - 50, paleta_ancho, paleta_alto)

# Pelota
pelota = pygame.Rect(ancho // 2 - 15, alto // 2 - 15, 20, 20)
velocidad_pelota = [5, 5]

# Velocidad de paletas
velocidad_paleta = 6

# Fuente
fuente = pygame.font.SysFont(None, 36)

# Marcadores
puntos1 = 0
puntos2 = 0

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento de paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1.top > 0:
        paleta1.y -= velocidad_paleta
    if teclas[pygame.K_s] and paleta1.bottom < alto:
        paleta1.y += velocidad_paleta
    if teclas[pygame.K_UP] and paleta2.top > 0:
        paleta2.y -= velocidad_paleta
    if teclas[pygame.K_DOWN] and paleta2.bottom < alto:
        paleta2.y += velocidad_paleta

    # Movimiento de pelota
    pelota.x += velocidad_pelota[0]
    pelota.y += velocidad_pelota[1]

    # Rebote arriba y abajo
    if pelota.top <= 0 or pelota.bottom >= alto:
        velocidad_pelota[1] *= -1

    # Rebote con paletas
    if pelota.colliderect(paleta1) or pelota.colliderect(paleta2):
        velocidad_pelota[0] *= -1

    # Punto para jugador 2
    if pelota.left <= 0:
        puntos2 += 1
        pelota.center = (ancho // 2, alto // 2)
        velocidad_pelota[0] *= -1

    # Punto para jugador 1
    if pelota.right >= ancho:
        puntos1 += 1
        pelota.center = (ancho // 2, alto // 2)
        velocidad_pelota[0] *= -1

    # Dibujar
    ventana.fill(negro)
    pygame.draw.rect(ventana, blanco, paleta1)
    pygame.draw.rect(ventana, blanco, paleta2)
    pygame.draw.ellipse(ventana, blanco, pelota)
    pygame.draw.aaline(ventana, blanco, (ancho // 2, 0), (ancho // 2, alto))

    texto1 = fuente.render(str(puntos1), True, blanco)
    texto2 = fuente.render(str(puntos2), True, blanco)
    ventana.blit(texto1, (ancho // 4, 20))
    ventana.blit(texto2, (ancho * 3 // 4, 20))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()

