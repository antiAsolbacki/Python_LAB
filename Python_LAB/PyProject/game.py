import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter 🚀")

# Load âm thanh
bullet_sound = pygame.mixer.Sound("bullet.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
meteor_grow_sound = pygame.mixer.Sound("meteor_grow.wav")

# Load hình ảnh phi thuyền
ship_img = pygame.image.load("ship_img.png").convert_alpha()
ship_img.set_colorkey((255, 255, 255))  # Loại bỏ viền trắng
ship_img = pygame.transform.scale(ship_img, (50, 50))

# Load hình ảnh viên đạn
bullet_img = pygame.image.load("bullet.png").convert_alpha()
bullet_img.set_colorkey((255, 255, 255))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Load hình ảnh vụ nổ
explosion_img = pygame.image.load("explosion.png").convert_alpha()
explosion_img.set_colorkey((255, 255, 255))
explosion_img = pygame.transform.scale(explosion_img, (50, 50))

# Tạo thiên thạch lớn và nhỏ
class Meteor:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size  # "big" hoặc "small"
        self.hp = 3 if size == "big" else 1
        self.image_original = pygame.image.load("meteor_big.png" if size == "big" else "meteor_small.png").convert_alpha()
        self.image_original.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image_original, (60, 60) if size == "big" else (40, 40))

    def move(self, speed):
        self.y += speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def grow(self):
        scale_factor = 1.2 if self.size == "big" else 1.0
        new_size = (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor))
        self.image = pygame.transform.scale(self.image_original, new_size)
        meteor_grow_sound.play()

meteors = []
meteor_speed = 3
start_time = time.time()

# Vị trí ban đầu của phi thuyền
ship_x = WIDTH // 2 - 25
ship_y = HEIGHT - 70
ship_speed = 7

# Danh sách đạn
bullets = []
bullet_speed = 7

# Điểm số
score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def game_over():
    screen.fill(BG)
    draw_text("GAME OVER! Press R to Restart", WIDTH // 4, HEIGHT // 2)
    pygame.display.update()
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart = True

def check_collision():
    global running, score
    for meteor in meteors[:]:
        if ship_x in range(meteor.x, meteor.x + meteor.image.get_width()) and ship_y in range(meteor.y, meteor.y + meteor.image.get_height()):
            game_over()
            meteors.clear()
            bullets.clear()
            score = 0

# Màu nền
BG = (96, 139, 193)

# Vòng lặp game
running = True
while running:
    pygame.time.delay(30)
    screen.fill(BG)
    screen.blit(ship_img, (ship_x, ship_y))
    draw_text(f"Score: {score}", 10, 10)

    # Tăng tốc độ thiên thạch mỗi 30 giây
    if time.time() - start_time > 30:
        meteor_speed += 1
        start_time = time.time()

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([ship_x + 22, ship_y])
                bullet_sound.play()

    # Điều khiển phi thuyền
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= ship_speed
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - 50:
        ship_x += ship_speed

    # Cập nhật vị trí đạn
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        screen.blit(bullet_img, bullet)

    # Sinh thiên thạch ngẫu nhiên
    if random.randint(1, 40) == 1:
        size = "big" if random.randint(1, 3) == 1 else "small"
        meteors.append(Meteor(random.randint(0, WIDTH - 60 if size == "big" else 40), 0, size))
    
    # Cập nhật vị trí thiên thạch
    for meteor in meteors[:]:
        meteor.move(meteor_speed)
        if meteor.y > HEIGHT:
            meteors.remove(meteor)
        meteor.draw()
    
    # Xử lý va chạm giữa đạn và thiên thạch
    for bullet in bullets[:]:
        for meteor in meteors[:]:
            if bullet[0] in range(meteor.x, meteor.x + meteor.image.get_width()) and bullet[1] in range(meteor.y, meteor.y + meteor.image.get_height()):
                bullets.remove(bullet)
                meteor.hp -= 1
                if meteor.size == "big":
                    meteor.grow()
                if meteor.hp <= 0:
                    explosion_sound.play()
                    screen.blit(explosion_img, (meteor.x, meteor.y))
                    pygame.display.update()
                    pygame.time.delay(100)
                    meteors.remove(meteor)
                    score += 10 if meteor.size == "small" else 30
                break
    
    # Kiểm tra va chạm giữa thiên thạch và phi thuyền
    check_collision()
    
    pygame.display.update()

pygame.quit()
