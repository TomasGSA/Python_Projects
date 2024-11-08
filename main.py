import pygame
import random
import math

# Iniciar pygame
pygame.init()

# Creacion de pantalla
pantalla = pygame.display.set_mode((800, 600))

# Nombre e Icono
pygame.display.set_caption("Invacion espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Jugador

img_jugador = pygame.image.load("transbordador-espacial.png")
jugador_x = 368
jugador_y = 500
move_player = 0


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Puntaje

puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final juego

finally_fount = pygame.font.Font('freesansbold.ttf', 40)


def texto_final():
    fuente_final = finally_fount.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(fuente_final, (60, 200))


# Funcion mostrar puntaje

def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Enemigos

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemy_move_y = []
enemy_move_x = []
enemy_change = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("ovni_02.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemy_move_y.append(0.3)
    enemy_move_x.append(0.3)
    enemy_change.append(1.5)


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_visible = False
move_balaX = 0
move_balaY = 1


def dis_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
running = True

while running:
    pantalla.fill((0, 0, 0))

    # EVENTOS
    for evento in pygame.event.get():
        # Evento para finalizar
        if evento.type == pygame.QUIT:
            running = False

        # Evento para presion de las teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                move_player = -0.2
            if evento.key == pygame.K_RIGHT:
                move_player = 0.2
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    dis_bala(bala_x, bala_y)

        # Evento para dejar de presionar
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                move_player = 0

    # Actualizacion de los eventos jugador
    jugador_x += move_player

    # definicion de limites de movimiento jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 250:
            for k in range(cantidad_enemigos):
                enemigo_y[e] = 1000
            texto_final()
            break

        # Actualizacion de los eventos enemigo
        enemigo_x[e] += enemy_move_x[e]

        # definicion de limites de movimiento enemigo
        if enemigo_x[e] <= 0:
            enemy_move_x[e] = 0.2
            enemigo_y[e] += enemy_change[e]
        elif enemigo_x[e] >= 736:
            enemy_move_x[e] = -0.2
            enemigo_y[e] += enemy_change[e]
        # colision
        hay_colision = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if hay_colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Definición del movimiento de la bala
    if bala_visible:
        dis_bala(bala_x, bala_y)
        bala_y -= move_balaY
    if bala_y <= -16:
        bala_y = 500
        bala_visible = False

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    pygame.display.update()
