import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from draw_character import DrawCharacter

import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen=screen, ai_settings=ai_settings)
    # Make a group to store bullets in.
    bullets = Group()

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
                        bullets=bullets)
        ship.update()
        gf.update_bullets(bullets=bullets)
        gf.update_screen(ai_settings=ai_settings,
                         screen=screen,
                         ship=ship,
                         bullets=bullets)


run_game()