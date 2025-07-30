import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from Shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Shot_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (Shot_group, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    player1 = Player(SCREEN_WIDTH /2 , SCREEN_HEIGHT / 2)
    my_asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")   
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)    

        for each_asteroid in asteroids:
            if each_asteroid.CheckCollision(player1):
                raise SystemExit("Game Over")

        for bullet in Shot_group:
            for asteroid in asteroids:
                if bullet.CheckCollision(asteroid):
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
                

    


if __name__ == "__main__":
    main()
