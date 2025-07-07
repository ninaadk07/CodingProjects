'''Welcome to Connect 0100!

The Game that combines famous children's game Connect 4 with Discrete Mathematics
To win the game, you must place 4 pieces in a row before your opponent does
This can be vertical, horizontal or diagonal in any direction
However, before a player's turn, they will be provided with a discrete math question and have to answer it in the text field provided
They will only get their turn if their answer is correct
The game combines stratedy and intelligence with a little bit of fun
Good Luck!'''

import pygame
import enter_names

class RulesGUI:
        
    def __init__(self):
        pass

    def run(self):
        self.name = ""

        # Initialize Pygame
        pygame.init()

        # Set up the window
        WIDTH = 800
        LENGTH = 700
        WINDOW_SIZE = (WIDTH, LENGTH)
        window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Pygame GUI")

        # Set up the font
        font = pygame.font.SysFont("Arial", 20)

        # Set up the "Submit" button
        clicked = pygame.Color('black')

        back_button = pygame.Rect(WIDTH/2 - 150, 180, 150, 50)
        back_button.center = (WIDTH/2 + 150, LENGTH/4 + 3*LENGTH/5)
        back_button_text = 'Play game'
        back_button_color = pygame.Color('gray')
        back_button_active_color = pygame.Color('blue')
        back_button_active = True

        submitted = False

        # Game loop

        while not submitted:

            if (not back_button_active):
                submitted = True
                if not back_button_active: 
                    intro = enter_names.EnterNameGUI()
                    intro.run()
                else:
                    pass

            # Draw the window
            window.fill(pygame.Color('white'))

            # Add text
            welcome_text = font.render("Welcome to Connect 0100!", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("The Game that combines famous children's game Connect 4 with Discrete Mathematics.", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 20 + LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("To win the game, you must place 4 pieces in a row before your opponent does.", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 40+LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("This can be vertical, horizontal or diagonal in any direction", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 60+LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("However, before a player's turn, they will be provided with a discrete math question", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 80+LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("They will only get their turn if their answer is correct", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 100+LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("The game combines strategy and intelligence with a little bit of fun", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 120+LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)

            welcome_text = font.render("Good Luck!", True, pygame.Color('black'))
            welcome_text_surface = welcome_text.get_rect(center=(WIDTH/2, 140+LENGTH/4))
            window.blit(welcome_text, welcome_text_surface)
        
            # Draw the "Submit" button

            # back_button_color = back_button_active_color if back_button.collidepoint(pygame.mouse.get_pos()) else back_button_color
            back_button_color = 'blue' if back_button_active else back_button_color
            back_button_color = clicked if back_button_active == False else back_button_color
            pygame.draw.rect(window, back_button_color, back_button)
            back_button_surface = font.render(back_button_text, True, pygame.Color('white'))
            back_button_center = back_button_surface.get_rect(center=back_button.center)
            window.blit(back_button_surface, back_button_center)

            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Check if the "Submit" button was clicked

                    if back_button.collidepoint(event.pos) and back_button_active:

                        back_button_active = False
                    
                
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

# rules = RulesGUI()
# rules.run()
