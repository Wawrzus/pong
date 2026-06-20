import pygame
from objects import Padle, Ball

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PADLE_WIDTH = 10 
PADDLE_HEIGHT = 150
PADLE_VELOCITY_Y = 6

BALL_RADIUS = 14
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

start_points = 0
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
menu_running = True
game_end = False

ORANGE = (255, 153, 51)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

left_player = Padle([0, 295, PADLE_WIDTH, PADDLE_HEIGHT], RED, start_points, PADLE_VELOCITY_Y)
right_player = Padle([1270, 295, PADLE_WIDTH, PADDLE_HEIGHT], BLUE, start_points, PADLE_VELOCITY_Y)
ball = Ball([640, 360], 14, ORANGE, 4, 4)
font = pygame.font.SysFont('liberationsans', 30, True)
START_GAME_BUTTON = pygame.Rect(490, 200, 300, 100)
EXIT_GAME_BUTTON = pygame.Rect(490, 400, 300, 100)

def _ball_reset():
        ball.position[0] = SCREEN_WIDTH // 2
        ball.position[1] = SCREEN_HEIGHT // 2
        ball.velocity_x = 4

def render_menu():
    screen.fill(BLACK)
    pygame.draw.rect(surface=screen, color=BLUE, rect=START_GAME_BUTTON, border_radius=5)
    pygame.draw.rect(surface=screen, color=BLUE, rect=EXIT_GAME_BUTTON, border_radius=5)
    PLAY_TEXT = font.render('play', False, WHITE)
    EXIT_TEXT = font.render('exit', False, WHITE)
    screen.blit(PLAY_TEXT, (610, 230))
    screen.blit(EXIT_TEXT, (610, 430))
    

def render_game():
    screen.fill(BLACK)  

    # rysowanie elementów planszy
    pygame.draw.rect(screen, left_player.color, left_player.position)
    pygame.draw.rect(screen, right_player.color, right_player.position)
    pygame.draw.circle(screen, ball.color, ball.position, ball.radius)

    left_player_points = font.render(f"{left_player.points}", True, WHITE)
    right_player_points = font.render(f"{right_player.points}", True, WHITE)
    screen.blit(left_player_points, (50,50))
    screen.blit(right_player_points, (1230,50))

    ball.position[0] += ball.velocity_x
    ball.position[1] += ball.velocity_y

    if ball.position[0] < -80:
        right_player.points += 1
        _ball_reset()

    if ball.position[0] > 1300:
        left_player.points += 1 
        _ball_reset()

    # hitboxy graczy
    if (ball.position[0] > 1270) and right_player.position[1] < ball.position[1] < right_player.position[1] + 150:
        ball.velocity_x = ball.velocity_x * -1 - 2

    if (ball.position[0] < 10) and left_player.position[1] < ball.position[1] < left_player.position[1] + 150:
        ball.velocity_x = ball.velocity_x * -1 + 2

    # movement piłki w osi y
    if ball.position[1] > 720:
        ball.velocity_y *= -1
    
    if ball.position[1] < 0:
        ball.velocity_y *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_player.position[1] >= 0:
        left_player.position[1] -= left_player.velocity_y
    if keys[pygame.K_s] and left_player.position[1] <= 570:
        left_player.position[1] += left_player.velocity_y

    if keys[pygame.K_UP] and right_player.position[1] >= 0:
        right_player.position[1] -= right_player.velocity_y
    if keys[pygame.K_DOWN] and right_player.position[1] <= 570:
        right_player.position[1] += right_player.velocity_y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_GAME_BUTTON.collidepoint(event.pos):
                menu_running = False
            if EXIT_GAME_BUTTON.collidepoint(event.pos):
                running = False

    # miejsce na logike gry
    if not menu_running and left_player.points < 3 and right_player.points < 3:
        render_game()
    else:
        left_player.points = 0
        right_player.points = 0
        menu_running = True
        render_menu()

    # koniec miejsca na logike gry

    pygame.display.flip()
    clock.tick(120)

pygame.quit()