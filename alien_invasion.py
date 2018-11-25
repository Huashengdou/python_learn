import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化设置类
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_event(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update( ai_settings, screen, ship, bullets)
        # 更新子弹位置
        gf.update_bullets(ai_settings, screen, ship,aliens, bullets)
        # 更新外星人
        gf.update_aliens(ai_settings, ship, aliens)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets )

run_game()