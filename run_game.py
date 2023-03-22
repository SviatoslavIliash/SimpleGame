"""Main run file"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialising game and create screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")     # Создание кнопки Play.
    stats = GameStats(ai_settings) # Создание экземпляра для хранения игровой статистики.
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen) # Создание корабля 
    aliens = Group() # Создание группы пришельцов.
    bullets = Group() # Создание группы для хранения пуль.
    gf.create_fleet(ai_settings, screen, ship, aliens) # Создание флота пришельцев.
    
    while True: # Запуск основного цикла игры.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) # Отслеживание событий клавиатуры и мыши.
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button) # Отображение последнего прорисованного экрана.
        

#if __name__ == "main":
run_game()
