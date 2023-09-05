import pygame, sys, random
from spaceship import Spaceship
from obstacle import *
from alien import Alien
from game import Game

pygame.init()

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

title_font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = title_font.render("LEVEL 01", False, YELLOW)
game_over_surface = title_font.render("GAME OVER", False, YELLOW)
score_text_surface = title_font.render("SCORE", False, YELLOW)
high_score_text_surface = title_font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
ALIENLASER = pygame.USEREVENT
pygame.time.set_timer(ALIENLASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1 
pygame.time.set_timer(MYSTERYSHIP, random.randint(10000,20000))

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == ALIENLASER:
            game.alien_shoot_laser()
        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

    screen.fill(GREY)
    pygame.draw.rect(screen, YELLOW, (10, 10 ,775, 775), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 800 - 70), (800 -25, 800 - 70), 3)
    
    if game.run:
        game.alien_lasers.update()
        game.spaceship.update()
        game.mystery_ship.update()
        game.check_for_collisions()
        game.alien_position_checker()
        game.aliens.update(game.alien_direction)
    
    game.spaceship.draw(screen)
    game.spaceship.sprite.lasers.draw(screen)
    game.obstacle_1.blocks.draw(screen)
    game.obstacle_2.blocks.draw(screen)
    game.obstacle_3.blocks.draw(screen)
    game.obstacle_4.blocks.draw(screen)
    game.aliens.draw(screen)
    game.alien_lasers.draw(screen)
    game.mystery_ship.draw(screen)
    screen.blit(score_text_surface, (50, 15, 50, 50))
    screen.blit(high_score_text_surface, (550, 15, 50, 50))

    formatted_high_score = str(game.highscore).zfill(5)  # Pad with leading zeros to make it 4 digits
    formatted_score = str(game.score).zfill(5)  # Pad with leading zeros to make it 4 digits
    score_surface = title_font.render(formatted_score, False, YELLOW)
    high_score_surface = title_font.render(formatted_high_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))
    screen.blit(high_score_surface, (625, 40, 50, 50))

    if game.run:
        screen.blit(level_surface, (570, SCREEN_HEIGHT + 38, 50, 50))
    else:
        screen.blit(game_over_surface, (570, SCREEN_HEIGHT + 38, 50, 50))

    x_start = 50  # Adjust this based on your desired starting x-coordinate
    y = SCREEN_HEIGHT + OFFSET - 5

    for _ in range(game.lives):
        screen.blit(game.lives_surface, (x_start, y))
        x_start += 50  # Adjust this value to control the spacing between lives
    
    pygame.display.update()
    clock.tick(60)