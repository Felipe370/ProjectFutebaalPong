import pygame
pygame.init()

window = pygame.display.set_mode([1200, 675])
pygame.display.set_caption('Futeball Pong')

field = pygame.image.load('assets/field.png')

score1 = 7
score1_img = pygame.image.load('assets/score/0.png')
score2 = 7
score2_img = pygame.image.load('assets/score/0.png')

win = pygame.image.load('assets/win.png')

player1 = pygame.image.load('assets/player1.png')
player1_y = 280
player1_moveup = False
player1_movedown = False


def move_player1():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0

    if player1_y <= 0:
        player1_y = 0
    if player1_y >= 565:
        player1_y = 565


player2 = pygame.image.load('assets/player2.png')
player2_y = 280


def move_player2():
    global player2_y

    player2_y = ball_y
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 565:
        player2_y = 565


ball = pygame.image.load('assets/ball.png')
ball_x = 580
ball_y = 320
ball_dir_x = -7
ball_dir_y = 3


def move_ball():
    global ball_x
    global ball_y
    global ball_dir_x
    global ball_dir_y
    global score1
    global score1_img
    global score2
    global score2_img

    ball_x += ball_dir_x
    ball_y += ball_dir_y

    if ball_y <= 0:
        ball_dir_y *= -1
    elif ball_y > 635:
        ball_dir_y *= -1

    if ball_x < 106:
        if player1_y < ball_y + 20:
            if player1_y + 112 > ball_y:
                ball_dir_x *= -1
    if ball_x > 1050:
        if player2_y < ball_y + 20:
            if player2_y + 112 > ball_y:
                ball_dir_x *= -1
    if ball_x < -50:
        ball_x = 580
        ball_y = 320
        ball_dir_x *= -1
        ball_dir_y *= -1
        score2 += 1
        score2_img = pygame.image.load('assets/score/' + str(score2) + '.png')

    elif ball_x > 1250:
        ball_x = 580
        ball_y = 320
        ball_dir_x *= -1
        ball_dir_y *= -1
        score1 += 1
        score1_img = pygame.image.load('assets/score' + str(score1) + '.png')


def draw():
    if score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1090, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (475, 10))
        window.blit(score2_img, (655, 10))
        move_ball()
        move_player1()
        move_player2()
    else:
        window.blit(win, (270, 300))


loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    draw()
    pygame.display.update()
