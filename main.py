import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Пинг-понг')

# Инициализация объектов
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]

left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Управление левой ракеткой
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Управление правой ракеткой
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Движение мяча
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Отскок мяча от верхней и нижней границ
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Отскок мяча от ракеток
    if left_paddle.collidepoint(ball_pos) or right_paddle.collidepoint(ball_pos):
        ball_speed[0] = -ball_speed[0]

    # Проверка на выход за границы (восстановление позиции мяча)
    if ball_pos[0] < 0 or ball_pos[0] > WIDTH:
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]

    # Отрисовка объектов
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    pygame.display.flip()
    clock.tick(60)