import pygame
import random
import numpy as np
import connect4_v3 as connect4
from cryptography.fernet import Fernet
import enter_names
import rules
import credits

class IntroScreenGUI:
        
    def __init__(self):
        pass

    def run(self):
        self.name = ""

        # Initialize Pygame
        pygame.init()

        # Set up the window
        WIDTH = 600
        LENGTH = 700
        WINDOW_SIZE = (WIDTH, LENGTH)
        window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Pygame GUI")

        # Set up the font
        font_header = pygame.font.SysFont("Arial", 35, True)
        font = pygame.font.SysFont("Arial", 24)
        
        background_color = pygame.Color("#EFE7DA")
        foreground_color = pygame.Color("#210F04")

        # Set up the "Submit" button
        clicked = pygame.Color('black')

        play_game_button = pygame.Rect(WIDTH/2 - 150, 180, 185, 50)
        play_game_button.center = (WIDTH/2 - 150, LENGTH/4 + LENGTH/5)
        play_game_button_text = 'Play Game'
        play_game_button_color = pygame.Color('gray')
        play_game_button_active_color = foreground_color
        play_game_button_active = True

        leaderboard_button = pygame.Rect(WIDTH/2 - 150, 180, 185, 50)
        leaderboard_button.center = (WIDTH/2 - 150, LENGTH/4 + 2*LENGTH/5)
        leaderboard_button_text = 'Leaderboard'
        leaderboard_button_color = pygame.Color('gray')
        leaderboard_button_active_color = foreground_color
        leaderboard_button_active = True

        rules_button = pygame.Rect(WIDTH/2 - 150, 180, 185, 50)
        rules_button.center = (WIDTH/2 + 150, LENGTH/4 + LENGTH/5)
        rules_button_text = 'Rules'
        rules_button_color = pygame.Color('gray')
        rules_button_active_color = foreground_color
        rules_button_active = True

        credits_button = pygame.Rect(WIDTH/2 - 150, 180, 185, 50)
        credits_button.center = (WIDTH/2 + 150, LENGTH/4 + 2*LENGTH/5)
        credits_button_text = 'Credits'
        credits_button_color = pygame.Color('gray')
        credits_button_active_color = foreground_color
        credits_button_active = True

        submitted = False

        # Game loop

        while not submitted:

            if (not play_game_button_active or not leaderboard_button_active or not rules_button_active or not credits_button_active):
                print("HERE")
                submitted = True
                if not play_game_button_active: 
                    en = enter_names.EnterNameGUI()
                    en.run()
                elif not rules_button_active:
                    rule = rules.RulesGUI()
                    rule.run()
                elif not credits_button_active:
                    credit = credits.CreditsGUI()
                    credit.run()

            # Draw the window
            window.fill(background_color)

            # Add text
            welcome_text = font_header.render("Welcome to Connect 0100", True, foreground_color)
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)
        
            # Draw the "Submit" buttons
            play_game_button_font_color = foreground_color
            if play_game_button.collidepoint(pygame.mouse.get_pos()):
                play_game_button_color = play_game_button_active_color
                play_game_button_font_color = background_color
            elif play_game_button_active == False:
                play_game_button_color = clicked
            else:
                play_game_button_color = background_color
                play_game_button_font_color = foreground_color
            # play_game_button_color = 'blue' if play_game_button_active else play_game_button_color
            # play_game_button_color = play_game_button_active_color if play_game_button.collidepoint(pygame.mouse.get_pos()) else play_game_button_color
            # play_game_button_color = clicked if play_game_button_active == False else play_game_button_color
            pygame.draw.rect(window, play_game_button_color, play_game_button)
            play_game_button_surface = font.render(play_game_button_text, True, play_game_button_font_color)
            play_game_button_center = play_game_button_surface.get_rect(center=play_game_button.center)
            window.blit(play_game_button_surface, play_game_button_center)

            leaderboard_button_font_color = foreground_color
            if leaderboard_button.collidepoint(pygame.mouse.get_pos()):
                leaderboard_button_color = leaderboard_button_active_color
                leaderboard_button_font_color = background_color
            elif leaderboard_button_active == False:
                leaderboard_button_color = clicked
            else:
                leaderboard_button_color = background_color
                leaderboard_button_font_color = foreground_color

            pygame.draw.rect(window, leaderboard_button_color, leaderboard_button)
            leaderboard_button_surface = font.render(leaderboard_button_text, True, leaderboard_button_font_color)
            leaderboard_button_center = leaderboard_button_surface.get_rect(center=leaderboard_button.center)
            window.blit(leaderboard_button_surface, leaderboard_button_center)

            rules_button_font_color = foreground_color
            if rules_button.collidepoint(pygame.mouse.get_pos()):
                rules_button_color = rules_button_active_color
                rules_button_font_color = background_color
            elif rules_button_active == False:
                rules_button_color = clicked
            else:
                rules_button_color = background_color
                rules_button_font_color = foreground_color

            pygame.draw.rect(window, rules_button_color, rules_button)
            rules_button_surface = font.render(rules_button_text, True, pygame.Color(rules_button_font_color))
            rules_button_center = rules_button_surface.get_rect(center=rules_button.center)
            window.blit(rules_button_surface, rules_button_center)

            credits_button_font_color = foreground_color
            if credits_button.collidepoint(pygame.mouse.get_pos()):
                credits_button_color = credits_button_active_color
                credits_button_font_color = background_color
            elif credits_button_active == False:
                credits_button_color = clicked
            else:
                credits_button_color = background_color
                credits_button_font_color = foreground_color

            pygame.draw.rect(window, credits_button_color, credits_button)
            credits_button_surface = font.render(credits_button_text, True, pygame.Color(credits_button_font_color))
            credits_button_center = credits_button_surface.get_rect(center=credits_button.center)
            window.blit(credits_button_surface, credits_button_center)

            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Check if the "Submit" button was clicked
                    if play_game_button.collidepoint(event.pos) and play_game_button_active:
                        
                        play_game_button_active = False
                    
                    if leaderboard_button.collidepoint(event.pos) and leaderboard_button_active:

                        leaderboard_button_active = False

                    if rules_button.collidepoint(event.pos) and rules_button_active:

                        rules_button_active = False
                    
                    if credits_button.collidepoint(event.pos) and credits_button_active:

                        credits_button_active = False
                    
                
                # Handle input text
                # elif event.type == pygame.KEYDOWN:

                #     if player1_name_input_active:
                #         if event.key == pygame.K_RETURN:
                #             player1_name_input_active = False
                #             player1_pass_input_active = True
                #         elif event.key == pygame.K_BACKSPACE:
                #             player1_name = player1_name[:-1]
                #         else:
                #             player1_name += event.unicode
                    
                #     if player1_pass_input_active:
                #         if event.key == pygame.K_RETURN:
                #             player1_pass_input_active = False
                #             player2_name_input_active = True
                #         elif event.key == pygame.K_BACKSPACE:
                #             player1_pass = player1_pass[:-1]
                #         else:
                #             player1_pass += event.unicode

                #     if player2_name_input_active:
                #         if event.key == pygame.K_RETURN:
                #             player2_name_input_active = False
                #             player2_pass_input_active = True
                #         elif event.key == pygame.K_BACKSPACE:
                #             player2_name = player2_name[:-1]
                #         else:
                #             player2_name += event.unicode
                    
                #     if player2_pass_input_active:
                #         if event.key == pygame.K_RETURN:
                #             player2_pass_input_active = False
                #         elif event.key == pygame.K_BACKSPACE:
                #             player2_pass = player2_pass[:-1]
                #         else:
                #             player2_pass += event.unicode

            # Update the display
            pygame.display.update()

intro = IntroScreenGUI()
intro.run()
