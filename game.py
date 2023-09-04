import pygame, random
from spaceship import Spaceship
from alien import Alien
from alien import MysteryShip
from obstacle import Obstacle
from laser import Laser

class Game():
    def __init__(self, screen_width, screen_height, offset):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.spaceship = pygame.sprite.GroupSingle()
        self.spaceship.add(Spaceship(screen_width, screen_height, offset))
        self.obstacle_1 = Obstacle(screen_width/4 - 128,screen_height - 100)
        self.obstacle_2 = Obstacle((screen_width/4)*2 - 128,screen_height - 100)
        self.obstacle_3 = Obstacle((screen_width/4)*3 - 128,screen_height - 100)
        self.obstacle_4 = Obstacle((screen_width/4)*4 - 128,screen_height - 100)
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.mystery_ship = pygame.sprite.GroupSingle()
        self.alien_direction = 1        
        self.create_aliens()

    def create_mystery_ship(self):
        self.mystery_ship.add(MysteryShip(self.screen_width, self.offset))

    def check_for_collisions(self):
        #Spaceship Laser
        if self.spaceship.sprite.lasers:
            for laser in self.spaceship.sprite.lasers:
                for obstacle in [self.obstacle_1, self.obstacle_2, self.obstacle_3, self.obstacle_4]:
                    if pygame.sprite.spritecollide(laser, obstacle.blocks, True):
                        laser.kill()

                if pygame.sprite.spritecollide(laser, self.aliens, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.mystery_ship, True):
                    laser.kill()

        #Aliens Laser
        if self.alien_lasers:
            for laser in self.alien_lasers:
                for obstacle in [self.obstacle_1, self.obstacle_2, self.obstacle_3, self.obstacle_4]:
                    if pygame.sprite.spritecollide(laser, obstacle.blocks, True):
                        laser.kill()
                if pygame.sprite.spritecollide(laser, self.spaceship, False):
                    print("Game Over!")

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = column * 55
                y = row * 55
                if row == 0:
                    alien_sprite = Alien(3, 75 + x + self.offset/2, 80 + y + self.offset)
                elif row == 1 or row == 2:
                    alien_sprite = Alien(2, 75 + x + self.offset/2, 80 + y + self.offset)
                else:
                    alien_sprite = Alien(1, 75 + x + self.offset/2, 80 + y + self.offset)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        alien_sprites = self.aliens.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width + self.offset/2:
                self.alien_direction = -1
                self.alien_move_down(2) 
            elif alien.rect.left <= self.offset/2:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
            self.alien_lasers.add(laser_sprite)