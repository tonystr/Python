import pygame
pygame.init()

window_width  = 480 * 2
window_height = 270 * 2
window = pygame.display.set_mode((window_width, window_height))
window.fill((76, 81, 119))
clock = pygame.time.Clock()
FPS = 60

arrow = pygame.image.load('arrow.png').convert_alpha()
gravity = .084
bounce_factor = 1.92

class Ball:
    x = window_width  / 2
    y = window_height / 2
    xvel = .5
    yvel = -2
    color = (210, 63, 126)
    radius = 10

    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        self.yvel += gravity
        x = self.x
        y = self.y
        radius = self.radius

        if x + radius > window_width:
            self.x += self.xvel * -2
            self.xvel *= 1 - bounce_factor
        elif x - radius < 0:
            self.x += self.xvel * -2
            self.xvel *= 1 - bounce_factor

        if y + radius > window_height:
            self.y += self.yvel * -2
            self.yvel *= 1 - bounce_factor
        elif y - radius < 0:
            self.y += self.yvel * -2
            self.yvel *= 1 - bounce_factor

    def draw(self):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius, 0)
        window.blit(arrow, (int(self.x), int(self.y)))

def game_loop():
    ball = Ball()
    ball.draw()
    mouse = 0
    ok = 0
    started = True

    while True:
        window.fill((76, 81, 119))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEMOTION:
                # if mouse == 1:
                ok = 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = 1

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = 0

        if started:
            ball.update()
        ball.draw()
        pygame.display.update()
        clock.tick(FPS)

game_loop()
