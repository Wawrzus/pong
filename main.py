import pygame
from random import choice
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
game_state = "menu"

running = True
menu_running = True
game_end = False
win_menu_running = False

start_time = None

who_win = None

ORANGE = (255, 153, 51)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

left_player = Padle([0, 295, PADLE_WIDTH, PADDLE_HEIGHT], RED, start_points, PADLE_VELOCITY_Y)
right_player = Padle([1270, 295, PADLE_WIDTH, PADDLE_HEIGHT], BLUE, start_points, PADLE_VELOCITY_Y)
ball = Ball([640, 360], 14, ORANGE, 4 * choice([-1, 1]), 4 * choice([-1, 1]))
font = pygame.font.SysFont('liberationsans', 30, True)
START_GAME_BUTTON = pygame.Rect(490, 200, 300, 100)
EXIT_GAME_BUTTON = pygame.Rect(490, 400, 300, 100)

def render_win(player: Padle):
    screen.fill(player.color)
    win_text = font.render("gratulacje", False, WHITE)
    win_text_rec = win_text.get_rect(center=((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
    screen.blit(win_text, win_text_rec)


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
    left_player.draw(screen=screen)
    right_player.draw(screen=screen)
    ball.draw(screen=screen)

    left_player_points = font.render(f"{left_player.points}", True, WHITE)
    right_player_points = font.render(f"{right_player.points}", True, WHITE)

    screen.blit(left_player_points, (50,50))
    screen.blit(right_player_points, (1230,50))

    ball.move()

    if ball.position[0] < -80:
        right_player.add_point()
        ball.reset(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

    if ball.position[0] > 1300:
        left_player.add_point()
        ball.reset(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

    # hitboxy graczy
    if right_player.get_rect().colliderect(ball.get_rect()):
        ball.velocity_x = ball.velocity_x * -1 - 2

    if left_player.get_rect().colliderect(ball.get_rect()):
        ball.velocity_x = ball.velocity_x * -1 + 2

    # movement piłki w osi y
    if ball.position[1] > 720:
        ball.bounce_vertical()
    
    if ball.position[1] < 0:
        ball.bounce_vertical()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_player.move_up()
    if keys[pygame.K_s]:
        left_player.move_down()

    if keys[pygame.K_UP]:
        right_player.move_up()
    if keys[pygame.K_DOWN]:
        right_player.move_down()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_GAME_BUTTON.collidepoint(event.pos):
                game_state = "game"
            if EXIT_GAME_BUTTON.collidepoint(event.pos):
                running = False

    if (left_player.points > 2 or right_player.points > 2) and game_state == "game":
        if left_player.points > right_player.points:
            who_win = right_player
        elif right_player.points > left_player.points:
            who_win = left_player
        game_state = "win"
        start_time = pygame.time.get_ticks()

    if game_state == "win" and pygame.time.get_ticks() - start_time > 2000:
        left_player.points = 0
        right_player.points = 0
        game_state = "menu"

    # miejsce na logike gry

    if game_state == "menu":
        render_menu()

    if game_state == "game":
        render_game()

    if game_state == "win":
        render_win(who_win)

    # koniec miejsca na logike gry

    pygame.display.flip()
    clock.tick(120)

pygame.quit()