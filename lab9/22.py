import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle settings
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball settings
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Time-based variables
start_time = pygame.time.get_ticks()  # Get the start time
speed_increase_interval = 5000  # Increase speed every 10 seconds (milliseconds)
paddle_shrink_interval = 10000   # Shrink paddle every 15 seconds (milliseconds)



# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 120 + 70 * j, 100, 50) for i in range(10) for j in range(3)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) 
              for _ in range(10) for _ in range(4)]

# Unbreakable brick settings
unbreakable_block_list = [pygame.Rect(10 + 360 * i, 330, 100, 50) for i in range(10)]
unbreakable_color = (255, 255, 255)

#bonus brick
bonus_block_list = [pygame.Rect(10 + 120 * i, 50, 100, 50) for i in range(10)]
bonus_color = (0, 0, 255)

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # Draw blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    # Draw unbreakable bricks
    [pygame.draw.rect(screen, unbreakable_color, block) for block in unbreakable_block_list]
    # Draw bonus bricks
    [pygame.draw.rect(screen, bonus_color, block) for block in bonus_block_list]

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    # Check collision with unbreakable bricks
    unbreakable_hit_index = ball.collidelist(unbreakable_block_list)
    if unbreakable_hit_index != -1:
        unbreakable_hit_rect = unbreakable_block_list[unbreakable_hit_index]
        dx, dy = detect_collision(dx, dy, ball, unbreakable_hit_rect)

    # Check collision with bonus bricks
    hitBonusIndex = ball.collidelist(bonus_block_list)
    if hitBonusIndex != -1:
        bonus_block_list.pop(hitBonusIndex)  # Remove the bonus brick
        paddleW += 25  # Increase paddle width
        paddle.width = paddleW  # Update paddle width

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Check elapsed time for speed increase
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= speed_increase_interval:
        ballSpeed += 1  # Increase ball speed
        start_time = current_time  # Reset start time for the next interval

    # Check elapsed time for paddle shrinkage
    if elapsed_time >= paddle_shrink_interval:
        paddleW -= 10  # Decrease paddle width
        paddle.width = paddleW  # Update paddle width
        paddle_shrink_interval += 1000  # Increase interval for next paddle shrinkage

    pygame.display.flip()
    clock.tick(FPS)
