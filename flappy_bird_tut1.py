import pygame
from pygame.locals import *

from Bird import Bird

pygame.init()

# 设置游戏画面帧率
clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("小鸟飞鱼")

# 定义游戏变量
ground_scroll = 0
# 每次移动4个像素
scroll_speed = 4

# 载入背景图片
bg = pygame.image.load("img/bg.png")
ground_img = pygame.image.load("img/ground.png")

bird_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)

run = True
while run:
    clock.tick(fps)

    # 绘制背景
    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()

    # 绘制下方拼接背景图
    screen.blit(ground_img, (ground_scroll, 768))
    # 设置下方图片以每次4像素的速度平移，制造动态效果
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # 检测键盘按下事件
        elif event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            print(f"Key pressed: {key_name}")
            if event.key == pygame.K_SPACE:
                print("空格键")

    pygame.display.update()

pygame.quit()
