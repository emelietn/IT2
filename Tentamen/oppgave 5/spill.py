import pygame
import random
from ball import Ball
from hinder import Hinder
from rekkert import Rekkert
 
pygame.init()
 
BREDDE = 800
HOYDE = 600
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
 
vindu = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Pong 2.0")
 
 
spiller1_rekkert = Rekkert(20, HOYDE // 2 - 50)
spiller2_rekkert = Rekkert(BREDDE - 30, HOYDE // 2 - 50)
ball = Ball()

hindere = [Hinder(400, 50), Hinder(400, 300), Hinder(400, 500)]


spiller1_poeng = 0
spiller2_poeng = 0
font = pygame.font.Font(None, 80)
 
kjorer = True
klokke = pygame.time.Clock()
while kjorer:
    vindu.fill(SVART)
 
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        spiller2_rekkert.beveg(-5)
    if keys[pygame.K_DOWN]:
        spiller2_rekkert.beveg(5)
    if keys[pygame.K_w]:
        spiller1_rekkert.beveg(-5)
    if keys[pygame.K_s]:
        spiller1_rekkert.beveg(5)
 
    ball.oppdater()
 
    if ball.rect.left <= 0:
        spiller2_poeng += 1
        ball.tilbakestill()
    if ball.rect.right >= BREDDE:
        spiller1_poeng += 1
        ball.tilbakestill()
 
    for hinder in hindere:
        if hinder.treffer_ball(ball):
            ball.speed[0] = -ball.speed[0]
            break
 
    if ball.treffer_rekkert(spiller1_rekkert) or ball.treffer_rekkert(spiller2_rekkert):
        ball.speed[0] = -ball.speed[0]
 

 
    pygame.draw.rect(vindu, HVIT, spiller1_rekkert.rect)
    pygame.draw.rect(vindu, HVIT, spiller2_rekkert.rect)
    pygame.draw.rect(vindu, HVIT, ball.rect)
    for hinder in hindere:
        pygame.draw.rect(vindu, HVIT, hinder.rect)
    
    poeng_tekst = font.render(f"{spiller1_poeng} - {spiller2_poeng}", True, HVIT)
    vindu.blit(poeng_tekst, (BREDDE // 2 - poeng_tekst.get_width() // 2, 10))
 
    pygame.display.flip()
    klokke.tick(60)
 
pygame.quit()



