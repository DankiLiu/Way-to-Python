import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_events(ship, ai_settings, screen, bullets):
    """Responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets: []):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet and add it to the bullets group."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """Update positions of bullets and get rid of old bullets."""
    # Update bullets positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    for alien in aliens:
        alien.update()


def create_fleet(ai_settings, screen, aliens, ship):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings=ai_settings,
                  screen=screen)
    alien_width = alien.rect.width
    number_x_aliens, number_y_aliens = \
        get_number_aliens(ai_settings, alien, ship.rect.height)
    for alien_col_number in range(number_x_aliens):
        for alien_row_number in range(number_y_aliens):
            create_alien(ai_settings, screen, aliens,
                         alien_col_number, alien_row_number)


def get_number_aliens(ai_settings, alien, ship_height):
    """Determine the number of aliens that fit in a row."""
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_x_aliens = int(available_space_x / (2 * alien_width))

    available_space_y = (ai_settings.screen_height -
                         2 * alien_height - ship_height)

    number_y_aliens = int(available_space_y / (2 * alien_height))
    return number_x_aliens, number_y_aliens


def create_alien(ai_settings, screen, aliens,
                 alien_col_number, alien_row_number):
    # Create an alien and place it in the row.
    alien = Alien(ai_settings=ai_settings, screen=screen)
    alien.rect.x += alien.rect.width * alien_col_number * 2
    alien.rect.y += alien.rect.height * alien_row_number * 2
    alien.x = float(alien.rect.x)
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropritely if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1