from circleshape import *
from player import *
from asteroid import *


SHOT_RADIUS = 5

class Shot(CircleShape):
    def __init__(self, x, y): 
        super().__init__(x, y, SHOT_RADIUS)
            
    def draw(self, surface):
        pygame.draw.circle(surface, "white", tuple(self.position), SHOT_RADIUS)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
