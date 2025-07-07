import pygame
import random
import numpy as np
import math

'''This class just includes functions to create permutations and solve their questions'''

def random_question(player):
    question_number = random.randint(0,2)
    if question_number == 0:
        permutations_question = PermutationQuestionGUI(player)
        permutations_question.run()
    elif question_number == 1:
        matrices_question = MatricesGUI(player)
        matrices_question.run()
    elif question_number == 2:
        euler_question = EulerTotientQuestionGUI(player)
        euler_question.run()

class Permutation:

    ''' Creates a random permutation of integers, parameters are the range (max_num) and the length of the list (length)'''

    def permutation_array(self, max_num, length):

        arr = random.sample(range(max_num), length)
        shuffled = arr.copy()
        random.shuffle(shuffled)

        permutation = [sorted(arr), shuffled]
        return permutation

    ''' Takes in a NumPy array, returns an integer (order of permutation)'''

    def find_order(self, np_arr): 
        pairs = []

        for i in range(len(np_arr[0])):
            pair = np_arr[:, i]
            pairs.append(list(pair))

        count = 0
        for i in pairs:
            if i[0] == i[1]:
                count += 1

        order = 0
        if count == len(pairs):
            order = 1
        else:
            order = len(pairs) - count

        return order

    ''' Takes in an array, and returns a 2D array of all the possible pairs.
        This is used when calculating the sign of a permutation'''

    def ordered_pairs(self, arr):
        pairs = []
        i = 0
        while i < len(arr):
            if i + 1 < len(arr):
                j = i + 1
                while j < len(arr):
                    pairs.append([arr[i],arr[j]])
                    j += 1
            i += 1
        return pairs

    ''' Takes in an array and returns an integer (1 or -1, representing the sign of a permutation)'''

    def find_sign(self, arr):
        row1 = self.ordered_pairs(arr[0])
        row2 = self.ordered_pairs(arr[1])
        disorders = 0
        for i in range(len(row1)):
            if row1[i][0] < row1[i][1] and row2[i][0] > row2[i][1]:
                disorders += 1
        if disorders % 2 == 0:
            return 1
        return -1

class PermutationQuestionGUI:
        
    def __init__(self, player):

        # Math-related variables
        self.player = player
        p = Permutation()
        length = random.randint(3,5)
        max_num = 20
        self.arr = p.permutation_array(max_num, length)
        self.np_arr = np.array(self.arr)
        self.order = p.find_order(self.np_arr)
        self.sign = p.find_sign(self.arr) 
        self.player_correct = False

        self.background_color = pygame.Color("#EFE7DA")
        self.foreground_color = pygame.Color("#210F04")

    def question(self, q_type): 
        if q_type == 0:
            
            text = f"{self.player}, Find the order of the permutation:"
            arr1 = f"{self.arr[0]}"
            arr2 = f"{self.arr[1]}"
            return [text, arr1, arr2, self.order]
        
        elif q_type == 1: 

            text = f"{self.player}, Find the sign of the permutation:"
            arr1 = f"{self.arr[0]}"
            arr2 = f"{self.arr[1]}"
            return [text, arr1, arr2, self.sign]

    def run(self):

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

        # Set up the entry field
        input_box = pygame.Rect(WIDTH/2, 100, 200, 32)
        input_box.center = (WIDTH/2, 1.1*LENGTH/2)
        input_text = ""

        # Set up the "Submit" button
        button_rect = pygame.Rect(WIDTH/2, 180, 100, 50)
        button_rect.center = (WIDTH/2, 3*LENGTH/4)
        button_text = 'Submit'
        button_color = pygame.Color('gray')
        button_active_color = self.foreground_color

        # Generate question
        q_type = random.randint(0,1)
        q, arr1, arr2, a = self.question(q_type)[0], self.question(q_type)[1], self.question(q_type)[2], self.question(q_type)[3]
        print(a)

        counter = 0

        question_answered = False

        # Game loop
        while not question_answered:

            # Draw the window
            window.fill(self.background_color)

            # Add question
            question_text = font.render(q, True,self.foreground_color)
            question_text_surface = question_text.get_rect(center=(WIDTH/2, LENGTH/4))
            window.blit(question_text, question_text_surface)

            arr1_text = font.render(arr1, True, self.foreground_color)
            arr1_text_surface = arr1_text.get_rect(center=(WIDTH/2, LENGTH/4 + LENGTH/10))
            window.blit(arr1_text, arr1_text_surface)

            arr2_text = font.render(arr2, True, self.foreground_color)
            arr2_text_surface = arr2_text.get_rect(center=(WIDTH/2, LENGTH/4 + LENGTH/10 + 30))
            window.blit(arr2_text, arr2_text_surface)

            # Draw the input box
            pygame.draw.rect(window, self.foreground_color, input_box)
            input_surface = font.render(input_text, True, self.background_color)
            window.blit(input_surface, (input_box.x + 5, input_box.y + 5))

            # Draw the "Submit" button
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                button_color = button_active_color
            #     button_font_color = self.background_color
            # else:
            #     button_color = self.background_color
            #     button_font_color = self.foreground_color

            # button_color = button_active_color if button_rect.collidepoint(pygame.mouse.get_pos()) else button_color
            pygame.draw.rect(window, button_color, button_rect)
            button_surface = font.render(button_text, True, self.background_color)
            button_rect_center = button_surface.get_rect(center=button_rect.center)
            window.blit(button_surface, button_rect_center)

            # Handle events
            for event in pygame.event.get():

                input_active = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Check if the "Submit" button was clicked
                    if button_rect.collidepoint(event.pos) and input_text != "":

                        # Collect response, Check if it is valid type and if it is correct, Add to txt file
                        try:

                            answer = int(input_text)
                            correct = answer == a

                            if correct:
                                correct_text = font.render("That is correct", True, self.foreground_color)
                                self.player_correct = True
                                correct_text_surface = correct_text.get_rect(center=(WIDTH/2, LENGTH/4 + LENGTH/10 + 65))
                                window.blit(correct_text, correct_text_surface)

                            else:
                                correct_text = font.render("Sorry, that is wrong", True, self.foreground_color)
                                self.player_correct = False
                                correct_text_surface = correct_text.get_rect(center=(WIDTH/2, LENGTH/4 + LENGTH/10 + 65))
                                window.blit(correct_text, correct_text_surface)

                            with open('report.txt','a+') as fp:
                                fp.write("------------------------------------------\n\n")
                                fp.write("Player: " + str(self.player) + "\n\n")
                                fp.write("Question number: " + str(counter) + "\n\n")
                                fp.write(str(q) + "\n" + arr1 + "\n" + arr2 + "\n\n")
                                fp.write("Correct answer: " + str(a) + "\n")
                                fp.write("User answer: " + str(answer) + "\n\n")
                                fp.write("Correct: " + str(correct) + "\n\n")
                                counter += 1

                        except ValueError:
                            pass

                        question_answered = True

                # Handle input text
                elif event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            # Update the display
            pygame.display.update()

class Matrices:
    def matrix_generator(self, rows, columns, rand_min, rand_max):
        """
        Randomly generates a matrix of integers of size ROWSxCOLUMNS, using values from rand_min to rand_max (inclusive)
        :param rand_max: minimum value possible in matrix
        :param rand_min: maximum value possible in matrix
        :param rows: the number of rows of the array
        :param columns: the number of columns of the array
        :return: a numpy array of size ROWSxCOLUMNS
        """
        return np.random.randint(rand_min, high=rand_max + 1, size=(rows, columns))

    def get_determinant(self, matrix):
        """
        Calculates the determinant of a matrix
        :param matrix: a numpy matrix of NxM size of integers, e.g. [[1, 2], [3, 4]]
        :return: the determinant of the matrix as an integer
        """
        return int(np.linalg.det(matrix))

    def get_eigenvalues(self, np_matrix):
        """
        Calculates the eigenvalues of a matrix
        :param matrix: a numpy matrix of size NxN, e.g. [[1, 2], [3, 4]]
        :return: the eigenvalues of the NxN matrix, as an N-element array
        """
        e_value, e_vector = np.linalg.eig(np_matrix)
        return e_value

    def matrix_multiplication(self, matrix_1, matrix_2):
        """
        A matrix multiplication function.
        :param matrix_1: a numpy array of size NxM where N >= M
        :param matrix_2: a numpy array of size MxN where N >= M
        :return: a numpy array of size NxN
        """
        return np.matmul(matrix_1, matrix_2)

class MatricesGUI:
    def __init__(self, player):

        # Math-related variables
        self.player = player
        m = Matrices()
        self.rows = random.randint(2, 3)
        max_num = 20
        self.sq_arr = m.matrix_generator(self.rows, self.rows, 0, max_num)
        self.sq_arr_2 = m.matrix_generator(self.rows, self.rows, 0, max_num)
        self.determinant = m.get_determinant(self.sq_arr)
        self.eigen = np.around(m.get_eigenvalues(self.sq_arr), decimals=2)
        self.eigen_str = ' '.join(map(str, self.eigen))
        self.compound_det = m.get_determinant(m.matrix_multiplication(self.sq_arr, self.sq_arr_2))
        self.background_color = pygame.Color("#EFE7DA")
        self.foreground_color = pygame.Color("#210F04")

    def question(self, q_type):

        if q_type == 0:  # Determinant
            if self.rows == 2: # 2x2 matrix
                text_l1 = f"Find the determinant of the following matrix:"
                text_l2 = f"{self.sq_arr[0]}"
                text_l3 = f"{self.sq_arr[1]}"
                text_l4 = f""
                text_l5 = f""
            else: # 3x3 matrix
                text_l1 = f"Find the determinant of the following matrix:"
                text_l2 = f"{self.sq_arr[0]}"
                text_l3 = f"{self.sq_arr[1]}"
                text_l4 = f"{self.sq_arr[2]}"
                text_l5 = f""
            return [text_l1, text_l2, text_l3, text_l4, text_l5, self.determinant]

        elif q_type == 1:  # Eigenvalue
            if self.rows == 2:  # 2x2 matrix
                text_l1 = f"Find the Eigenvalues of the following matrix."
                text_l2 = f"(To 2 decimal places, seperated by 1 space)"
                text_l3 = f"{self.sq_arr[0]}"
                text_l4 = f"{self.sq_arr[1]}"
                text_l5 = f""
            else:  # 3x3 matrix
                text_l1 = f"Find the Eigenvalues of the following matrix."
                text_l2 = f"(To 2 decimal places, seperated by 1 space)"
                text_l3 = f"{self.sq_arr[0]}"
                text_l4 = f"{self.sq_arr[1]}"
                text_l5 = f"{self.sq_arr[2]}"
            return [text_l1, text_l2, text_l3, text_l4, text_l5, self.eigen_str]

        elif q_type == 2:  # Compound Determinant

            if self.rows == 2:  # yikes, that formatting TODO: FIX
                text_l1 = f"Find the determinant of the following statement."
                text_l2 = f"{self.sq_arr[0]}            {self.sq_arr_2[0]} "
                text_l3 = f"X"
                text_l4 = f"{self.sq_arr[1]}            {self.sq_arr_2[1]} "
                text_l5 = f""
            else:
                text_l1 = f"Find the determinant of the following statement."
                text_l2 = f"{self.sq_arr[0]}            {self.sq_arr_2[0]} "
                text_l3 = f"{self.sq_arr_2[1]}      X      {self.sq_arr_2[1]} "
                text_l4 = f"{self.sq_arr[2]}            {self.sq_arr_2[2]}"
                text_l5 = f""
            return [text_l1, text_l2, text_l3, text_l4, text_l5, self.compound_det]

    def run(self):

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

        # Set up the entry field
        input_box = pygame.Rect(WIDTH / 2, 100, 200, 32)
        input_box.center = (WIDTH / 2, 1.3 * LENGTH / 2)
        input_text = ""

        # Set up the "Submit" button
        button_rect = pygame.Rect(WIDTH / 2, 180, 100, 50)
        button_rect.center = (WIDTH / 2, 3 * LENGTH / 4)
        button_text = 'Submit'
        button_color = pygame.Color('gray')
        button_active_color = self.foreground_color

        # Generate question
        q_type = random.randint(0, 2)

        text_l1, text_l2, text_l3, text_l4, text_l5, a = self.question(q_type)[0], self.question(q_type)[1], self.question(q_type)[2], self.question(q_type)[3], self.question(q_type)[4], self.question(q_type)[5]
        print(a)

        counter = 0

        question_answered = False

        # Game loop
        while not question_answered:

            # Draw the window
            window.fill(pygame.Color(self.background_color))

            # Add question
            text_l1_row = font.render(text_l1, True, self.foreground_color)
            question_text_surface = text_l1_row.get_rect(center=(WIDTH / 2, LENGTH / 4))
            window.blit(text_l1_row, question_text_surface)

            text_l2_row = font.render(text_l2, True, self.foreground_color)
            question_text_surface = text_l2_row.get_rect(center=(WIDTH / 2, LENGTH / 4 + LENGTH/10))
            window.blit(text_l2_row, question_text_surface)

            text_l3_row = font.render(text_l3, True, self.foreground_color)
            question_text_surface = text_l3_row.get_rect(center=(WIDTH / 2, LENGTH / 4 + LENGTH/10 + 30))
            window.blit(text_l3_row, question_text_surface)

            text_l4_row = font.render(text_l4, True, self.foreground_color)
            question_text_surface = text_l4_row.get_rect(center=(WIDTH / 2, LENGTH / 4 + LENGTH/10 + 60))
            window.blit(text_l4_row, question_text_surface)

            text_l5_row = font.render(text_l5, True, self.foreground_color)
            question_text_surface = text_l5_row.get_rect(center=(WIDTH / 2, LENGTH / 4 + LENGTH/10 + 90))
            window.blit(text_l5_row, question_text_surface)

            # Draw the input box
            pygame.draw.rect(window, self.foreground_color, input_box)
            input_surface = font.render(input_text, True, self.background_color)
            window.blit(input_surface, (input_box.x + 5, input_box.y + 5))

            # Draw the "Submit" button
            button_color = button_active_color if button_rect.collidepoint(pygame.mouse.get_pos()) else button_color
            pygame.draw.rect(window, button_color, button_rect)
            button_surface = font.render(button_text, True, self.background_color)
            button_rect_center = button_surface.get_rect(center=button_rect.center)
            window.blit(button_surface, button_rect_center)

            # Handle events
            for event in pygame.event.get():

                input_active = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Check if the "Submit" button was clicked
                    if button_rect.collidepoint(event.pos) and input_text != "":

                        # Collect response, Check if it is valid type and if it is correct, Add to txt file
                        try:

                            answer = input_text
                            correct = str(answer) == str(a)

                            if correct:
                                correct_text = font.render("That is correct", True, pygame.Color('black'))
                                self.player_correct = True
                                correct_text_surface = correct_text.get_rect(
                                    center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 120))
                                window.blit(correct_text, correct_text_surface)

                            else:
                                correct_text = font.render("Sorry, that is wrong", True, pygame.Color('black'))
                                self.player_correct = False
                                correct_text_surface = correct_text.get_rect(
                                    center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 120))
                                window.blit(correct_text, correct_text_surface)

                            with open('report.txt', 'a+') as fp:
                                fp.write("------------------------------------------\n\n")
                                fp.write("Player: " + str(self.player) + "\n\n")
                                fp.write("Question number: " + str(counter) + "\n\n")
                                fp.write(str(text_l1 + "\n" + text_l2 + "\n" + text_l3 + "\n" + text_l4 + "\n" + text_l5 + "\n") + "\n\n")
                                fp.write("Correct answer: " + str(a) + "\n")
                                fp.write("User answer: " + str(answer) + "\n\n")
                                fp.write("Correct: " + str(correct) + "\n\n")
                                counter += 1

                        except ValueError:
                            pass

                        question_answered = True

                # Handle input text
                elif event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            # Update the display
            pygame.display.update()

class Vector:

    # def __init__(self, dim):
    #     self.dim = dim
    #     self.v = np.random.randint(1, 10, dim)

    # def __repr__(self):
    #     return f"{self.v}"
    
    # def dot(self, other):
    #     return f"{self.v[0]*other.v[0] + self.v[1]*other.v[1] + self.v[2]*other.v[2]}"
    
    # def cross(self, other):
    #     i = self.v[1] * other.v[2] - self.v[2] * other.v[1]
    #     j = self.v[2] * other.v[0] - self.v[0] * other.v[2]
    #     k = self.v[0] * other.v[1] - self.v[1] * other.v[0]
    #     return f"{i}, {j}, {k}"

    def __init__(self, dim):
        self.dim = dim
        self.v = np.random.randint(1, 10, dim)

    def __repr__(self):
        return f"{self.v}"
    
    def dot(self, other):
        return f"{self.v[0]*other.v[0] + self.v[1]*other.v[1] + self.v[2]*other.v[2]}"
    
    def cross(self, other):
        i = self.v[1] * other.v[2] - self.v[2] * other.v[1]
        j = self.v[2] * other.v[0] - self.v[0] * other.v[2]
        k = self.v[0] * other.v[1] - self.v[1] * other.v[0]
        return f"{i}, {j}, {k}"

class VectorQuestionGUI:

    def __init__(self, player):
        self.player = player
        self.v1 = Vector(3)
        self.v2 = Vector(3)
        self.type = random.choice(['dot', 'cross'])
        self.answer = self.calculate_answer()
        self.player_correct = False
        self.background_color = pygame.Color("#EFE7DA")
        self.foreground_color = pygame.Color("#210F04")


    def calculate_answer(self):
        if self.type == 'dot':
            return self.v1.dot(self.v2)
        elif self.type == 'cross':
            return self.v1.cross(self.v2)

    def question(self):
        text = f"Find the {self.type} product of vectors {self.v1} and {self.v2}"
        text2 = f"(For cross products answer format is: _, _, _)"
        a_text = f"a = {self.v1}"
        b_text = f"b = {self.v2}"
        if self.type == 'dot':
            return [text, a_text, b_text]
        else:
            return [text, a_text, b_text, text2]

    def check_answer(self, user_answer):
        return self.answer == user_answer

    def run(self):

        # Initialize Pygame
        pygame.init()

        # Set up the window
        WIDTH = 600
        LENGTH = 700
        WINDOW_SIZE = (WIDTH, LENGTH)
        window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Vector Question")

        # Set up the font
        font = pygame.font.SysFont("Arial", 24)
        font2 = pygame.font.SysFont("Arial", 16)

        # Set up the entry field
        input_box = pygame.Rect(WIDTH/2, 100, 200, 32)
        input_box.center = (WIDTH/2, 1.1*LENGTH/2)
        input_text = ""

        # Set up the "Submit" button
        button_rect = pygame.Rect(WIDTH/2, 180, 100, 50)
        button_rect.center = (WIDTH/2, 3*LENGTH/4)
        button_text = 'Submit'
        button_color = pygame.Color('gray')
        button_active_color = pygame.Color('blue')

        # Generate question
        q, v1, v2 = self.question()[0], self.question()[1], self.question()[2]
        if self.type == 'cross':
            q2 = self.question()[3]
        print(self.answer)

        counter = 0

        question_answered = False

        # Game loop
        while not question_answered:

            # Draw the window
            window.fill( self.background_color)

            # Add question
            question_text = font.render(q, True, self.foreground_color)
            question_text_surface = question_text.get_rect(center=(WIDTH / 2, LENGTH / 4))
            window.blit(question_text, question_text_surface)

            if self.type == 'cross':
                question_text_row2 = font2.render(q2, True, self.foreground_color)
                question_text_surface = question_text.get_rect(center=(WIDTH / 2, LENGTH / 4 + LENGTH/15))
                window.blit(question_text_row2, question_text_surface)

            # Draw the input box
            pygame.draw.rect(window, self.foreground_color, input_box)
            input_surface = font.render(input_text, True,  self.background_color)
            window.blit(input_surface, (input_box.x + 5, input_box.y + 5))

            # Draw the "Submit" button
            button_color = button_active_color if button_rect.collidepoint(pygame.mouse.get_pos()) else button_color
            pygame.draw.rect(window, button_color, button_rect)
            button_surface = font.render(button_text, True,  self.background_color)
            button_rect_center = button_surface.get_rect(center=button_rect.center)
            window.blit(button_surface, button_rect_center)

            # Handle events
            for event in pygame.event.get():

                input_active = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Check if the "Submit" button was clicked
                    if button_rect.collidepoint(event.pos) and input_text != "":

                        # Collect response, Check if it is valid type and if it is correct, Add to txt file
                        try:

                            answer = input_text
                            correct = answer == self.answer

                            if correct:
                                correct_text = font.render("That is correct", True, pygame.Color('black'))
                                self.player_correct = True
                                correct_text_surface = correct_text.get_rect(
                                    center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 65))
                                window.blit(correct_text, correct_text_surface)

                            else:
                                correct_text = font.render("Sorry, that is wrong", True, pygame.Color('black'))
                                self.player_correct = False
                                correct_text_surface = correct_text.get_rect(
                                    center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 65))
                                window.blit(correct_text, correct_text_surface)

                            with open('report.txt', 'a+') as fp:
                                fp.write("------------------------------------------\n\n")
                                fp.write("Player: " + str(self.player) + "\n\n")
                                fp.write("Question number: " + str(counter) + "\n\n")
                                fp.write(str(q) + "\n\n")
                                fp.write("Correct answer: " + str(self.answer) + "\n")
                                fp.write("User answer: " + str(answer) + "\n\n")
                                fp.write("Correct: " + str(correct) + "\n\n")
                                counter += 1

                        except ValueError:
                            pass

                        question_answered = True

                # Handle input text
                elif event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            # Update the display
            pygame.display.update()

    # def __init__(self, player):
    #     self.player = player
    #     self.v1 = Vector(3)
    #     self.v2 = Vector(3)
    #     self.type = random.choice(['dot', 'cross'])
    #     self.answer = self.calculate_answer()
    #     self.player_correct = False
    #     self.background_color = pygame.Color("#EFE7DA")
    #     self.foreground_color = pygame.Color("#210F04")

    # def calculate_answer(self):
    #     if self.type == 'dot':
    #         return self.v1.dot(self.v2)
    #     elif self.type == 'cross':
    #         return self.v1.cross(self.v2)

    # def question(self):
    #     text = f"Find the {self.type} product of vectors {self.v1} and {self.v2}"
    #     a_text = f"a = {self.v1}"
    #     b_text = f"b = {self.v2}"
    #     return [text, a_text, b_text]

    # def check_answer(self, user_answer):
    #     return self.answer == user_answer

    # def run(self):

    #     # Initialize Pygame
    #     pygame.init()

    #     # Set up the window
    #     WIDTH = 600
    #     LENGTH = 700
    #     WINDOW_SIZE = (WIDTH, LENGTH)
    #     window = pygame.display.set_mode(WINDOW_SIZE)
    #     pygame.display.set_caption("Vector Question")

    #     # Set up the font
    #     font = pygame.font.SysFont("Menlo", 24)

    #     # Set up the entry field
    #     input_box = pygame.Rect(WIDTH/2, 100, 200, 32)
    #     input_box.center = (WIDTH/2, 1.1*LENGTH/2)
    #     input_text = ""

    #     # Set up the "Submit" button
    #     button_rect = pygame.Rect(WIDTH/2, 180, 100, 50)
    #     button_rect.center = (WIDTH/2, 3*LENGTH/4)
    #     button_text = 'Submit'
    #     button_color = pygame.Color('gray')
    #     button_active_color = self.foreground_color

    #     # Generate question
    #     q, v1, v2 = self.question()[0], self.question()[1], self.question()[2]
    #     print(self.answer)

    #     counter = 0

    #     question_answered = False

    #     # Game loop
    #     while not question_answered:

    #         # Draw the window
    #         window.fill(self.background_color)

    #         # Add question
    #         question_text = font.render(q, True, self.foreground_color)
    #         question_text_surface = question_text.get_rect(center=(WIDTH / 2, LENGTH / 4))
    #         window.blit(question_text, question_text_surface)

    #         # Draw the input box
    #         pygame.draw.rect(window, self.foreground_color, input_box)
    #         input_surface = font.render(input_text, True, self.background_color)
    #         window.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    #         # Draw the "Submit" button
    #         button_color = button_active_color if button_rect.collidepoint(pygame.mouse.get_pos()) else button_color
    #         pygame.draw.rect(window, button_color, button_rect)
    #         button_surface = font.render(button_text, True, self.background_color)
    #         button_rect_center = button_surface.get_rect(center=button_rect.center)
    #         window.blit(button_surface, button_rect_center)

    #         # Handle events
    #         for event in pygame.event.get():

    #             input_active = True

    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 quit()

    #             elif event.type == pygame.MOUSEBUTTONDOWN:

    #                 # Check if the "Submit" button was clicked
    #                 if button_rect.collidepoint(event.pos) and input_text != "":

    #                     # Collect response, Check if it is valid type and if it is correct, Add to txt file
    #                     try:

    #                         answer = input_text
    #                         correct = answer == self.answer

    #                         if correct:
    #                             correct_text = font.render("That is correct", True, pygame.Color('black'))
    #                             self.player_correct = True
    #                             correct_text_surface = correct_text.get_rect(
    #                                 center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 65))
    #                             window.blit(correct_text, correct_text_surface)

    #                         else:
    #                             correct_text = font.render("Sorry, that is wrong", True, pygame.Color('black'))
    #                             self.player_correct = False
    #                             correct_text_surface = correct_text.get_rect(
    #                                 center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 65))
    #                             window.blit(correct_text, correct_text_surface)

    #                         with open('report.txt', 'a+') as fp:
    #                             fp.write("------------------------------------------\n\n")
    #                             fp.write("Player: " + str(self.player) + "\n\n")
    #                             fp.write("Question number: " + str(counter) + "\n\n")
    #                             fp.write(str(q) + "\n\n")
    #                             fp.write("Correct answer: " + str(self.answer) + "\n")
    #                             fp.write("User answer: " + str(answer) + "\n\n")
    #                             fp.write("Correct: " + str(correct) + "\n\n")
    #                             counter += 1

    #                     except ValueError:
    #                         pass

    #                     question_answered = True

    #             # Handle input text
    #             elif event.type == pygame.KEYDOWN:
    #                 if input_active:
    #                     if event.key == pygame.K_RETURN:
    #                         input_active = False
    #                     elif event.key == pygame.K_BACKSPACE:
    #                         input_text = input_text[:-1]
    #                     else:
    #                         input_text += event.unicode

    #         # Update the display
    #         pygame.display.update()

class EulerTotient:
    
    def primechk(self, x):
        counter = 0
        for i in range (1, x):
            if x % i == 0:
                counter = counter + 1
        if counter == 2:
            return True
        else:
            return False

    def primeFactors(self, n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n / 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):

            while n % i == 0:
                factors.append(i)
                n = n / i
        if n > 2:
            factors.append(n)
        return factors


    def findtotient(self, divisor):
        primeval = self.primechk(divisor)
        if primeval == True:
            tot = divisor - 1
        else:
            factors = self.primeFactors(divisor)
            factors = list(dict.fromkeys(factors))
            print(factors)
            product = divisor
            for k in factors:
                product = product * (1 - (1/k))
            tot = product

        newtot = int(tot)
        return newtot

    def pow_mod(self, base, exp, divisor):
        if exp == 0:
            return 1
        elif exp == 1:
            return base % divisor
        else:
            divided = self.pow_mod(base, exp // 2, divisor)
            if exp % 2 == 0:
                return (divided * divided) % divisor
            else:
                return (divided * divided * base) % divisor

class EulerTotientQuestionGUI:

    def __init__(self, player):

        # Math-related variables
        self.player = player
        self.base = random.randint(2, 9)
        self.exp = random.randint(2, 1000)
        self.divisor = random.randint(2, 200)
        p = EulerTotient()
        self.totient = p.findtotient(self.divisor)
        self.modulus = p.pow_mod(self.base, self.exp, self.divisor)
        self.player_correct = False
        self.background_color = pygame.Color("#EFE7DA")
        self.foreground_color = pygame.Color("#210F04")

    def question(self, q_type):
        if q_type == 0:

            text = f"{self.player}, Find the euler totient of " + str(self.divisor)
            string = f"{self.divisor}"

            return [text, self.totient]

        elif q_type == 1:

            text = f"{self.player}, Find the value of " + str(self.base) + " ^ " + str(self.exp) + " mod " + str(self.divisor)

            return [text, self.modulus]

    def run(self):

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

        # Set up the entry field
        input_box = pygame.Rect(WIDTH / 2, 100, 200, 32)
        input_box.center = (WIDTH / 2, 1.1 * LENGTH / 2)
        input_text = ""

        # Set up the "Submit" button
        button_rect = pygame.Rect(WIDTH / 2, 180, 100, 50)
        button_rect.center = (WIDTH / 2, 3 * LENGTH / 4)
        button_text = 'Submit'
        button_color = pygame.Color('gray')
        button_active_color = self.foreground_color

        # Generate question
        q_type = random.randint(0, 1)

        q, a = self.question(q_type)[0], self.question(q_type)[1],
        print(a)

        counter = 0

        question_answered = False

        # Game loop
        while not question_answered:

            # Draw the window
            window.fill(self.background_color)

            # Add question
            question_text = font.render(q, True, self.foreground_color)
            question_text_surface = question_text.get_rect(center=(WIDTH / 2, LENGTH / 4))
            window.blit(question_text, question_text_surface)


            # Draw the input box
            pygame.draw.rect(window, self.foreground_color, input_box)
            input_surface = font.render(input_text, True, self.background_color)
            window.blit(input_surface, (input_box.x + 5, input_box.y + 5))

            # Draw the "Submit" button
            button_color = button_active_color if button_rect.collidepoint(pygame.mouse.get_pos()) else button_color
            pygame.draw.rect(window, button_color, button_rect)
            button_surface = font.render(button_text, True, self.background_color)
            button_rect_center = button_surface.get_rect(center=button_rect.center)
            window.blit(button_surface, button_rect_center)

            # Handle events
            for event in pygame.event.get():

                input_active = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Check if the "Submit" button was clicked
                    if button_rect.collidepoint(event.pos) and input_text != "":

                        # Collect response, Check if it is valid type and if it is correct, Add to txt file
                        try:

                            answer = int(input_text)
                            correct = answer == a

                            if correct:
                                correct_text = font.render("That is correct", True, pygame.Color('black'))
                                self.player_correct = True
                                correct_text_surface = correct_text.get_rect(
                                    center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 65))
                                window.blit(correct_text, correct_text_surface)

                            else:
                                correct_text = font.render("Sorry, that is wrong", True, pygame.Color('black'))
                                self.player_correct = False
                                correct_text_surface = correct_text.get_rect(
                                    center=(WIDTH / 2, LENGTH / 4 + LENGTH / 10 + 65))
                                window.blit(correct_text, correct_text_surface)

                            with open('report.txt', 'a+') as fp:
                                fp.write("------------------------------------------\n\n")
                                fp.write("Player: " + str(self.player) + "\n\n")
                                fp.write("Question number: " + str(counter) + "\n\n")
                                fp.write(str(q) + "\n\n")
                                fp.write("Correct answer: " + str(a) + "\n")
                                fp.write("User answer: " + str(answer) + "\n\n")
                                fp.write("Correct: " + str(correct) + "\n\n")
                                counter += 1

                        except ValueError:
                            pass

                        question_answered = True

                # Handle input text
                elif event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            # Update the display
            pygame.display.update()

if __name__ == "__main__":
    pq = PermutationQuestionGUI("Damon")
    pq.run()

