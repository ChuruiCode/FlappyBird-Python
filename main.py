import sys
import time
import pygame, configs, assets
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.brid import Brid
from objects.game_start_message import GameStartMessage
from objects.game_over_message import GameOverMessage
from objects.score import Score


class Game:
    def __init__(self):
        pygame.init()

        # title
        pygame.display.set_caption("小鸟飞鱼")

        # 设置画面像素
        self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.running = True

        # 动作开启
        self.gamestart = False
        self.gameover = False

        # 暂停
        self.paused = False

        # 加载图片资源
        assets.load_sprites()

        self.sprites = pygame.sprite.LayeredUpdates()
        self.collision_sprites = pygame.sprite.Group()

        # 计算画面比例
        bg_height = assets.get_sprite("background").get_height()
        self.scale_factor = configs.SCREEN_HEIGHT / bg_height

        # 创建定时器，每隔一段时间更新管道
        self.column_timer = pygame.USEREVENT + 1

        # 创建精灵组
        self.brid, self.game_start_message, self.score = self.create_sprite()

    def create_sprite(self):
        self.over_msg = False
        self.start_msg = True
        Background(self.sprites)
        Floor([self.sprites, self.collision_sprites])
        Column([self.sprites, self.collision_sprites])
        return Brid(self.sprites), GameStartMessage(self.sprites), Score(self.sprites)

    def collisions(self):
        # 碰撞函数调用 参数：param1:主精灵，param2：碰撞关联的组，param3:是否销毁,param4:使用mask模式
        if pygame.sprite.spritecollide(self.brid, self.collision_sprites, False, pygame.sprite.collide_mask):
            self.game_over()

    # 游戏开始
    def game_start(self):
        # 开启管道定时器
        pygame.time.set_timer(self.column_timer, configs.COLUMN_TIME_INTERVAL)
        self.gamestart = True
        self.paused = False
        self.game_start_message.kill()

    # 游戏结束
    def game_over(self):
        self.game_over_message = GameOverMessage(self.sprites)
        self.gameover = True
        self.gamestart = False
        self.score.value = 0
        pygame.time.set_timer(self.column_timer, 0)

    def run(self):
        last_time = time.time()
        # 开启程序循环监听
        while self.running:
            # 延时时间
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                # 监听退出游戏事件
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # 鼠标点击游戏开始
                    if not self.gamestart and not self.gameover:
                        self.game_start()
                    elif self.gamestart:
                        self.brid.jump()
                if event.type == pygame.KEYDOWN:
                    # 空格点击事件
                    if event.key == pygame.K_SPACE:
                        if not self.gamestart:
                            self.gameover = False
                            # 创建精灵组
                            self.sprites.empty()
                            self.collision_sprites.empty()
                            self.brid, self.game_start_message, self.score = self.create_sprite()
                    elif event.key == pygame.K_p:
                        print("暂停游戏")
                        self.paused = True

                if event.type == self.column_timer and self.gamestart and not self.paused:
                    Column([self.sprites, self.collision_sprites])

            self.screen.fill(0)

            # 绘制图像
            self.sprites.draw(self.screen)
            if self.gamestart and not self.paused:
                # 循环更新背景
                self.sprites.update(dt)
                # 碰撞事件
                self.collisions()

            for sprite in self.sprites:
                if type(sprite) is Column and sprite.is_passed():
                    self.score.value += 1
                    # print("得分：", self.score.value)

            pygame.display.flip()

            # 设置游戏帧数
            self.clock.tick(configs.FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
