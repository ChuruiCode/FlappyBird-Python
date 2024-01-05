import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("img/bird1.png"), pygame.image.load("img/bird2.png"), pygame.image.load("img/bird3.png")]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        # 小鸟下降的速度
        self.vel = 0
        # 最大下降速度
        self.max_vel = 8
        self.clicked = False
        self.flying = False

    def update(self):
        if self.flying == True:
            # 如果小鸟顶到天花板重置Y轴数值(测试用)
            # if self.rect.top <= 0 and self.vel == 0:
            #     self.rect.top = 0
            #     self.vel = 0

            # 限制下降速度
            if self.vel < self.max_vel:
                # 下降速度叠加
                self.vel += 0.5

            # print("vel值：", self.vel)
            # print("bottom值：", self.rect.bottom)
            # print("top值：", self.rect.top)
            if self.rect.bottom < 768 and self.rect.top >= 0:
                self.rect.y += int(self.vel)

        # 鼠标点击事件
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.flying = True
            self.clicked = True
            # 单击调整Y轴数值向上提升
            if self.rect.bottom < 768 and self.rect.top >= 0:
                self.vel = -10
            # if self.rect.bottom >= 768:
            #     self.rect.bottom += self.vel
            # if self.rect.top <= 0:
            #     self.vel = 0
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.index += 1
        self.index = self.index % len(self.images)
        self.image = self.images[self.index]

        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -3)

    def abc():
        print("abc方法")
