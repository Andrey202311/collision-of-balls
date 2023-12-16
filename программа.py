import pygame
import random
# Импортируем необходимые классы и функции из модуля pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


# Инициализируем pygame
pygame.init()
screen_wize = width, height = 500, 500
screen = pygame.display.set_mode(screen_wize)
clock = pygame.time.Clock()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Создаем 10 шаров
for i in range(10):
    Ball(20, 100, 100)

running = True
while running:
    screen.fill((255, 255, 255))

    all_sprites.draw(screen)
    all_sprites.update()

    # Рисуем границы
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# Завершаем работу с pygame
pygame.quit()