import pygame


class Simulator:
    def __init__(self):
        pygame.init()

        self.screen = 0
        self.xPos, self.yPos = 0, 0
        self.circle = 0
        self.width, self.height = 1000, 550
        self.clock = pygame.time.Clock()
        self.cover = pygame.image.load("resources/icon.png")

        self.window_colour = 0, 0, 0
        self.yellow = 255, 255, 100
        self.running = True
        self.xVelocity, self.yVelocity = 0, 0
        self.bounce = 3 / 4
        self.friction = 19 / 20
        self.follow = True
        self.dx, self.dy = 0, 0

    def create_window(self, window_title="Physics", width=1000, height=550, colour=(0, 206, 209)):
        self.width, self.height = width, height
        self.window_colour = colour
        self.screen = pygame.display.set_mode((self.width, self.height + 100))
        pygame.display.set_caption(window_title)
        pygame.display.set_icon(self.cover)

    def update(self, ball):
        pygame.display.flip()
        self.screen.fill(self.window_colour)

        self.clock.tick(40)

        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                self.dx, self.dy = event.rel

            if event.type == pygame.KEYDOWN:
                ball.switch_mode(self.dx, self.dy)


class Ball:
    def __init__(self, game, colour=(255, 255, 0), bounce=(3/4), friction=(19/20), size=10):
        self.width, self.height = game.width, game.height
        self.mouse = pygame.mouse
        self.screen = game.screen
        self.ball_colour = 0, 0, 0
        self.ball_colour = colour
        self.xVelocity, self.yVelocity = 0, 0
        self.bounceFriction = bounce
        self.friction = friction
        self.shouldFollow = False
        self.dx, self.dy = 0, 0
        self.size = size

        self.xPos, self.yPos = self.width / 2, self.height / 2
        self.circle = pygame.draw.circle(self.screen, self.ball_colour, [self.width / 2, self.height / 2], 10)

    def follow_mouse(self):
        self.mouse.set_visible(False)
        self.xPos, self.yPos = self.mouse.get_pos()

    def touching_ground(self):
        if self.yPos >= self.height+90 and self.yVelocity < 0:
            return True
        else:
            return False

    def touching_roof(self):
        if self.yPos <= 0 < self.yVelocity:
            return True
        else:
            return False

    def touching_walls(self):
        if (self.xPos >= self.width and self.xVelocity > 0) or (self.xPos <= 0 and self.xVelocity < 0):
            return True
        else:
            return False

    def bounce(self):
        if self.touching_ground() or self.touching_roof():
            self.yVelocity = -self.yVelocity * self.bounceFriction
        if self.touching_walls():
            self.xVelocity = -self.xVelocity * self.friction

    def stabilize(self):
        if self.yPos >= self.height+90 and abs(self.yVelocity < 5):
            self.yPos = self.height+90
            self.yVelocity = 0
            self.xVelocity = self.xVelocity * self.friction

    def gravity(self):
        if not (self.touching_ground() or (self.yPos >= self.height+90 and abs(self.yVelocity < 5))):
            self.yVelocity -= 9.8

    def move(self):
        if not self.shouldFollow:
            self.yPos -= self.yVelocity
            self.xPos += self.xVelocity

        self.circle = pygame.draw.circle(self.screen, self.ball_colour, [self.xPos, self.yPos], self.size)

    def switch_mode(self, dx, dy):
        self.shouldFollow = not self.shouldFollow
        if not self.shouldFollow:
            self.yVelocity = -dy
            self.xVelocity = dx
            self.mouse.set_visible(True)

