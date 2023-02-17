import sys

import pygame

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# Make the most recently drawn screen visible.
pygame.display.flip()

run_game()

bg_color = (230,230,230)
screen.fill(bg_color)
