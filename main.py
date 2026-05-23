import pygame
from objects import Padle, Ball

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

left_player = Padle([0, 295, 10, 150], 'red', 0, 6)
right_player = Padle([1270, 295, 10, 150], 'blue', 0, 6)
ball = Ball([640, 360], 14, 'orange', 4, 4)
font = pygame.font.SysFont('liberationsans', 30, True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # miejsce na logike gry

    screen.fill('black')

    # rysowanie elementów planszy
    pygame.draw.rect(screen, left_player.color, left_player.position)
    pygame.draw.rect(screen, right_player.color, right_player.position)
    pygame.draw.circle(screen, ball.color, ball.position, ball.radius)

    ball.position[0] += ball.velocity_x
    ball.position[1] += ball.velocity_y

    left_player_points = font.render(f"{left_player.points}", True, 'white')
    right_player_points = font.render(f"{right_player.points}", True, 'white')
    screen.blit(left_player_points, (50,50))
    screen.blit(right_player_points, (1230,50))

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

    # koniec miejsca na logike gry

    pygame.display.flip()
    clock.tick(120)

pygame.quit()