import pygame
import random
import numpy as np
import connect4_v3 as connect4
from cryptography.fernet import Fernet

class EnterNameGUI:
        
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
        font = pygame.font.SysFont("Arial", 24)

        background_color = pygame.Color("#EFE7DA")
        foreground_color = pygame.Color("#210F04")
    
        # Set up the entry field
        player1_name_input = pygame.Rect(WIDTH/2 - 150, 100, 200, 32)
        player1_name_input.center = (WIDTH/2 - 150, LENGTH/4 + LENGTH/10)
        player1_name = ""
        player1_name_input_active = True

        player1_pass_input = pygame.Rect(WIDTH/2 - 150, 100, 200, 32)
        player1_pass_input.center = (WIDTH/2 - 150, LENGTH/4 + 2.5*LENGTH/5)
        player1_pass = ""
        player1_pass_input_active = False

        player2_name_input = pygame.Rect(WIDTH/2 - 150, 100, 200, 32)
        player2_name_input.center = (WIDTH/2 + 150, LENGTH/4 + LENGTH/10)
        player2_name = ""
        player2_name_input_active = False

        player2_pass_input = pygame.Rect(WIDTH/2 - 150, 100, 200, 32)
        player2_pass_input.center = (WIDTH/2 + 150, LENGTH/4 + 2.5*LENGTH/5)
        player2_pass = ""
        player2_pass_input_active = False

        # Set up the "Submit" button
        clicked = pygame.Color('black')

        player1_name_button = pygame.Rect(WIDTH/2 - 150, 180, 100, 50)
        player1_name_button.center = (WIDTH/2 - 150, LENGTH/4 + LENGTH/5)
        player1_name_button_text = 'Submit'
        player1_name_button_color = pygame.Color('gray')
        player1_name_button_active_color = foreground_color
        player1_name_button_active = True

        player1_pass_button = pygame.Rect(WIDTH/2 - 150, 180, 100, 50)
        player1_pass_button.center = (WIDTH/2 - 150, LENGTH/4 + 3*LENGTH/5)
        player1_pass_button_text = 'Submit'
        player1_pass_button_color = pygame.Color('gray')
        player1_pass_button_active_color = foreground_color
        player1_pass_button_active = False

        player2_name_button = pygame.Rect(WIDTH/2 - 150, 180, 100, 50)
        player2_name_button.center = (WIDTH/2 + 150, LENGTH/4 + LENGTH/5)
        player2_name_button_text = 'Submit'
        player2_name_button_color = pygame.Color('gray')
        player2_name_button_active_color = foreground_color
        player2_name_button_active = False

        player2_pass_button = pygame.Rect(WIDTH/2 - 150, 180, 100, 50)
        player2_pass_button.center = (WIDTH/2 + 150, LENGTH/4 + 3*LENGTH/5)
        player2_pass_button_text = 'Submit'
        player2_pass_button_color = pygame.Color('gray')
        player2_pass_button_active_color = foreground_color
        player2_pass_button_active = False

        name_pass_entered = False

        # Game loop

        while not name_pass_entered:

            if (not player1_name_button_active and not player1_pass_button_active and not player2_name_button_active and not player2_pass_button_active):
                name_pass_entered = True
                cn4 = connect4.Connect4GUI(str(player1_name), str(player2_name))
                cn4.run()

            # Draw the window
            window.fill(background_color)

            # Add text
            player1_name_text = font.render("Player 1 Name", True, foreground_color)
            player1_name_text_surface = player1_name_text.get_rect(center=(WIDTH/2 - 150, LENGTH/4))
            window.blit(player1_name_text, player1_name_text_surface)

            player1_pass_text = font.render("Player 1 Password", True, foreground_color)
            player1_pass_text_surface = player1_pass_text.get_rect(center=(WIDTH/2 - 150, LENGTH/4 + 2*LENGTH/5))
            window.blit(player1_pass_text, player1_pass_text_surface)

            player2_name_text = font.render("Player 2 Name", True, foreground_color)
            player2_name_text_surface = player2_name_text.get_rect(center=(WIDTH/2 + 150, LENGTH/4))
            window.blit(player2_name_text, player2_name_text_surface)

            player2_pass_text = font.render("Player 2 Password", True, foreground_color)
            player2_pass_text_surface = player2_pass_text.get_rect(center=(WIDTH/2 + 150, LENGTH/4 + 2*LENGTH/5))
            window.blit(player2_pass_text, player2_pass_text_surface)

            # Draw the input boxes
            # player1_name_input_color = 'orange' if player1_name_input.collidepoint(pygame.mouse.get_pos()) else 'gray'

            player1_name_input_color = 'orange' if player1_name_input_active else background_color
            pygame.draw.rect(window, player1_name_input_color, player1_name_input)
            player1_name_input_surface = font.render(player1_name, True, foreground_color)
            window.blit(player1_name_input_surface, (player1_name_input.x + 5, player1_name_input.y + 5))
            
            # player1_pass_input_color = 'orange' if player1_pass_input.collidepoint(pygame.mouse.get_pos()) else 'gray'
            player1_pass_input_color = 'orange' if player1_pass_input_active else background_color
            pygame.draw.rect(window, player1_pass_input_color, player1_pass_input)
            player1_pass_input_surface = font.render(player1_pass, True, foreground_color)
            window.blit(player1_pass_input_surface, (player1_pass_input.x + 5, player1_pass_input.y + 5))

            # player2_name_input_color = 'orange' if player2_name_input.collidepoint(pygame.mouse.get_pos()) else 'gray'
            player2_name_input_color = 'orange' if player2_name_input_active else background_color
            pygame.draw.rect(window, player2_name_input_color, player2_name_input)
            player2_name_input_surface = font.render(player2_name, True, foreground_color)
            window.blit(player2_name_input_surface, (player2_name_input.x + 5, player2_name_input.y + 5))
            
            # player2_pass_input_color = 'orange' if player2_pass_input.collidepoint(pygame.mouse.get_pos()) else 'gray'
            player2_pass_input_color = 'orange' if player2_pass_input_active else background_color
            pygame.draw.rect(window, player2_pass_input_color, player2_pass_input)
            player2_pass_input_surface = font.render(player2_pass, True, foreground_color)
            window.blit(player2_pass_input_surface, (player2_pass_input.x + 5, player2_pass_input.y + 5))

            # Draw the "Submit" buttons
            # player1_name_button_color = player1_name_button_active_color if player1_name_button.collidepoint(pygame.mouse.get_pos()) else player1_name_button_color
            player1_name_button_color = 'blue' if player1_name_button_active else player1_name_button_color
            player1_name_button_color = clicked if player1_name_button_active == False else player1_name_button_color
            pygame.draw.rect(window, player1_name_button_color, player1_name_button)
            player1_name_button_surface = font.render(player1_name_button_text, True, background_color)
            player1_name_button_center = player1_name_button_surface.get_rect(center=player1_name_button.center)
            window.blit(player1_name_button_surface, player1_name_button_center)

            # player1_pass_button_color = player1_pass_button_active_color if player1_pass_button.collidepoint(pygame.mouse.get_pos()) else player1_pass_button_color
            player1_pass_button_color = 'blue' if player1_pass_button_active else player1_pass_button_color
            player1_pass_button_color = clicked if player1_pass_button_active == False else player1_pass_button_color
            pygame.draw.rect(window, player1_pass_button_color, player1_pass_button)
            player1_pass_button_surface = font.render(player1_pass_button_text, True, background_color)
            player1_pass_button_center = player1_pass_button_surface.get_rect(center=player1_pass_button.center)
            window.blit(player1_pass_button_surface, player1_pass_button_center)

            # player2_name_button_color = player2_name_button_active_color if player2_name_button.collidepoint(pygame.mouse.get_pos()) else player2_name_button_color
            player2_name_button_color = 'blue' if player2_name_button_active else player2_name_button_color
            player2_name_button_color = clicked if player2_name_button_active == False else player2_name_button_color
            pygame.draw.rect(window, player2_name_button_color, player2_name_button)
            player2_name_button_surface = font.render(player2_name_button_text, True, background_color)
            player2_name_button_center = player2_name_button_surface.get_rect(center=player2_name_button.center)
            window.blit(player1_pass_button_surface, player2_name_button_center)

            # player2_pass_button_color = player2_pass_button_active_color if player2_pass_button.collidepoint(pygame.mouse.get_pos()) else player2_pass_button_color
            player2_pass_button_color = 'blue' if player2_pass_button_active else player2_pass_button_color
            player2_pass_button_color = clicked if player2_pass_button_active == False else player2_pass_button_color
            pygame.draw.rect(window, player2_pass_button_color, player2_pass_button)
            player2_pass_button_surface = font.render(player2_pass_button_text, True, background_color)
            player2_pass_button_center = player2_pass_button_surface.get_rect(center=player2_pass_button.center)
            window.blit(player2_pass_button_surface, player2_pass_button_center)

            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if player1_name_input.collidepoint(event.pos):
                        player1_name_input_active = True
                        player1_pass_input_active = False
                        pygame.draw.rect(window, 'blue', player1_name_input)
                    
                    if player1_pass_input.collidepoint(event.pos):
                        player1_pass_input_active = True
                        player1_name_input_active = False
                        pygame.draw.rect(window, 'blue', player1_pass_input)

                    # Check if the "Submit" button was clicked
                    if player1_name_button.collidepoint(event.pos) and player1_name != "" and player1_name_button_active:
                        
                        self.name = player1_name
                        with open('player_info.txt','a+') as fp:
                            fp.write("\n------------------------------------------\n\n")
                            fp.write("Player1: \n")
                            fp.write("Name: " + str(player1_name) + "\n")
                        
                        player1_name_input_active = False
                        player1_name_button_active = False

                        player1_pass_input_active = True
                        player1_pass_button_active = True
                    
                    if player1_pass_button.collidepoint(event.pos) and player1_pass != "" and player1_pass_button_active:

                        key = Fernet.generate_key()
                        fernet = Fernet(key)
                        encMessage = fernet.encrypt(player1_pass.encode())

                        with open('player_info.txt','a+') as fp:
                            fp.write("Password: " + str(encMessage) + "\n")
                            fp.write("Key: " + str(key) + "\n")
                
                        player1_pass_input_active = False
                        player1_pass_button_active = False

                        player2_name_button_active = True
                        player2_name_input_active = True


                    if player2_name_button.collidepoint(event.pos) and player2_name != "" and player2_name_button_active:
                        
                        self.name = player2_name
                        with open('player_info.txt','a+') as fp:
                            fp.write("\nPlayer 2: \n")
                            fp.write("Name: " + str(player2_name) + "\n")
                        
                        player2_name_input_active = False
                        player2_pass_input_active = True
                        
                        player2_name_button_active = False
                        player2_pass_button_active = True
                    
                    if player2_pass_button.collidepoint(event.pos) and player2_pass != "" and player2_pass_button_active:

                        key2 = Fernet.generate_key()
                        fernet2 = Fernet(key)
                        encMessage2 = fernet.encrypt(player2_pass.encode())

                        with open('player_info.txt','a+') as fp:
                            fp.write("Password: " + str(encMessage2) + "\n")
                            fp.write("Key: " + str(key2) + "\n")
                
                        player2_pass_button_active = False
                        
                
                # Handle input text
                elif event.type == pygame.KEYDOWN:

                    if player1_name_input_active:
                        if event.key == pygame.K_RETURN:
                            player1_name_input_active = False
                            player1_pass_input_active = True
                        elif event.key == pygame.K_BACKSPACE:
                            player1_name = player1_name[:-1]
                        else:
                            player1_name += event.unicode
                    
                    if player1_pass_input_active:
                        if event.key == pygame.K_RETURN:
                            player1_pass_input_active = False
                            player2_name_input_active = True
                        elif event.key == pygame.K_BACKSPACE:
                            player1_pass = player1_pass[:-1]
                        else:
                            player1_pass += event.unicode

                    if player2_name_input_active:
                        if event.key == pygame.K_RETURN:
                            player2_name_input_active = False
                            player2_pass_input_active = True
                        elif event.key == pygame.K_BACKSPACE:
                            player2_name = player2_name[:-1]
                        else:
                            player2_name += event.unicode
                    
                    if player2_pass_input_active:
                        if event.key == pygame.K_RETURN:
                            player2_pass_input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            player2_pass = player2_pass[:-1]
                        else:
                            player2_pass += event.unicode

            # Update the display
            pygame.display.update()

# en = EnterNameGUI()
# en.run()
