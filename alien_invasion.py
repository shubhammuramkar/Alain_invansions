import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from Alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

#from pygame import

def run_game():

    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the Play button
    play_button = Button(ai_settings,screen,'Play ,Q to exit')

    #Make ship
    ship = Ship(ai_settings,screen)

    # Make  a group to store bullets in.
    bullets = Group()

    #Make a group to store aliens
    aliens = Group()
    
    # create fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Make an alien
    alien = Alien(ai_settings,screen)

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) 
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens , bullets, play_button)


if __name__  == "__main__":
    run_game()
