import pygame
from objects import Padle, Ball

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
menu_running = True

left_player = Padle([0, 295, 10, 150], 'red', 0, 6)
right_player = Padle([1270, 295, 10, 150], 'blue', 0, 6)
ball = Ball([640, 360], 14, 'orange', 4, 4)
font = pygame.font.SysFont('liberationsans', 30, True)
START_GAME_BUTTON = pygame.Rect(490, 200, 300, 100)
EXIT_GAME_BUTTON = pygame.Rect(490, 400, 300, 100)

def menu():
    screen.fill('black')
    pygame.draw.rect(surface=screen, color='blue', rect=START_GAME_BUTTON, border_radius=5)
    pygame.draw.rect(surface=screen, color='blue', rect=EXIT_GAME_BUTTON, border_radius=5)
    PLAY_TEXT = font.render('play', False, 'white')
    EXIT_TEXT = font.render('exit', False, 'white')
    screen.blit(PLAY_TEXT, (610, 230))
    screen.blit(EXIT_TEXT, (610, 430))
    

def game():
    screen.fill('black')

    # rysowanie elementów planszy
    pygame.draw.rect(screen, left_player.color, left_player.position)
    pygame.draw.rect(screen, right_player.color, right_player.position)
    pygame.draw.circle(screen, ball.color, ball.position, ball.radius)

    left_player_points = font.render(f"{left_player.points}", True, 'white')
    right_player_points = font.render(f"{right_player.points}", True, 'white')
    screen.blit(left_player_points, (50,50))
    screen.blit(right_player_points, (1230,50))

    ball.position[0] += ball.velocity_x
    ball.position[1] += ball.velocity_y

    if ball.position[0] < -80:
        right_player.points += 1
        ball.position[0] = 640
        ball.position[1] = 360
        ball.velocity_x = 4

    if ball.position[0] > 1300:
        left_player.points += 1 
        ball.position[0] = 640
        ball.position[1] = 360
        ball.velocity_x = 4

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

    # miejsce na logike gry
    mouse_position = pygame.mouse.get_pos()
    if (pygame.Rect.collidepoint(START_GAME_BUTTON, mouse_position) and event.type == pygame.MOUSEBUTTONDOWN):
        menu_running = False

    if (pygame.Rect.collidepoint(EXIT_GAME_BUTTON, mouse_position) and event.type == pygame.MOUSEBUTTONDOWN):
        running = False

    if not menu_running:
        game()
    else:
        menu()

    # koniec miejsca na logike gry

    pygame.display.flip()
    clock.tick(120)

pygame.quit()