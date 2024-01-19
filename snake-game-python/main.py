import pygame
import sys
import random

pygame.init()

LATIME, INALTIME = 600, 400
DIMENSIUNE_SARPE = 20
FPS = 10

NEGRU = (0, 0, 0)
ROSU = (255, 0, 0)
VERDE = (0, 255, 0)

ecran = pygame.display.set_mode((LATIME, INALTIME))
pygame.display.set_caption("Jogo da serpente")

serpente = [(100, 50), (90, 50), (80, 50)]
direcao_serpente = "DREAPTA"

comida_posicao = (random.randrange(1, (LATIME // DIMENSIUNE_SARPE)) * DIMENSIUNE_SARPE,
                  random.randrange(1, (INALTIME // DIMENSIUNE_SARPE)) * DIMENSIUNE_SARPE)

lungime_sarpe = 3

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao_serpente != "JOS":
                direcao_serpente = "SUS"
            if evento.key == pygame.K_DOWN and direcao_serpente != "SUS":
                direcao_serpente = "JOS"
            if evento.key == pygame.K_LEFT and direcao_serpente != "DREAPTA":
                direcao_serpente = "STANGA"
            if evento.key == pygame.K_RIGHT and direcao_serpente != "STANGA":
                direcao_serpente = "DREAPTA"

    if direcao_serpente == "DREAPTA":
        cap_nou = (serpente[0][0] + DIMENSIUNE_SARPE, serpente[0][1])
    elif direcao_serpente == "STANGA":
        cap_nou = (serpente[0][0] - DIMENSIUNE_SARPE, serpente[0][1])
    elif direcao_serpente == "SUS":
        cap_nou = (serpente[0][0], serpente[0][1] - DIMENSIUNE_SARPE)
    elif direcao_serpente == "JOS":
        cap_nou = (serpente[0][0], serpente[0][1] + DIMENSIUNE_SARPE)

    serpente.insert(0, cap_nou)

    if serpente[0] == comida_posicao:
        lungime_sarpe += 1
        comida_posicao = (random.randrange(1, (LATIME // DIMENSIUNE_SARPE)) * DIMENSIUNE_SARPE,
                          random.randrange(1, (INALTIME // DIMENSIUNE_SARPE)) * DIMENSIUNE_SARPE)

    while len(serpente) > lungime_sarpe:
        serpente.pop()

    ecran.fill(NEGRU)
    for segment in serpente:
        pygame.draw.rect(ecran, ROSU, pygame.Rect(segment[0], segment[1], DIMENSIUNE_SARPE, DIMENSIUNE_SARPE))
    pygame.draw.rect(ecran, VERDE, pygame.Rect(comida_posicao[0], comida_posicao[1], DIMENSIUNE_SARPE, DIMENSIUNE_SARPE))

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
