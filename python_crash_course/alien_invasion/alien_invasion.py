import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship
    ship = Ship(screen=screen, ai_settings=ai_settings)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, ship)
    """
    # Import a character
    cat = DrawCharacter(image="images/cat.png",
                        screen=screen)
    """

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship=ship,
                        ai_settings=ai_settings,
                        screen=screen,
                        bullets=bullets,
                        stats=stats,
                        play_button=play_button,
                        aliens=aliens,
                        sb=sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens=aliens, bullets=bullets,
                              ship=ship, screen=screen,
                              settings=ai_settings,
                              stats=stats,
                              sb=sb)
            gf.update_aliens(ai_settings=ai_settings,
                             stats=stats,
                             aliens=aliens,
                             ship=ship,
                             bullets=bullets,
                             screen=screen,
                             sb=sb)
        gf.update_screen(ai_settings=ai_settings,
                         screen=screen,
                         ship=ship,
                         aliens=aliens,
                         bullets=bullets,
                         play_button=play_button,
                         stats=stats,
                         sb=sb)

run_game()