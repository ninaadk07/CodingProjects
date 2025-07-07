import numpy as np
import pygame
import sys
import math
import questionsGUI_v2
import random


class Connect4GUI:

	def __init__(self, player1_name, player2_name):
		self.player1_name = player1_name
		self.player2_name = player2_name

		self.board_color = pygame.Color("#F0C808")
		self.background_color = pygame.Color("#1E2019")
		self.player1_color = pygame.Color("#DD1C1A")
		self.player2_color = pygame.Color("#07A0C3")
		self.rows = 6
		self.cols = 7
		self.square_size = 100

		self.width = self.cols * self.square_size
		self.height = (self.rows+1) * self.square_size
		
		self.size = (self.width, self.height)
		self.radius = int(self.square_size/2 - 5)

		self.screen = pygame.display.set_mode(self.size)

	def create_board(self):
		board = np.zeros((self.rows,self.cols))
		return board

	def drop_piece(self, board, row, col, piece):
		board[row][col] = piece

	def valid_position(self, board, col):
		return board[self.rows-1][col] == 0

	def next_free_spot(self, board, col):
		row = 0 
		while row < self.rows:
			if board[row][col] == 0:
				return row
			row += 1

		# for r in range(self.rows):
		# 	if board[r][col] == 0:
		# 		return r

	def print_board(self, board):
		print(np.flip(board, 0))

	def draw_board(self, board):
		for c in range(self.cols):
			for r in range(self.rows):
				pygame.draw.rect(self.screen, self.board_color, (c*self.square_size, r*self.square_size+self.square_size, self.square_size, self.square_size))
				pygame.draw.circle(self.screen, self.background_color, (int(c*self.square_size+self.square_size/2), int(r*self.square_size+self.square_size+self.square_size/2)), self.radius)
		
		for c in range(self.cols):
			for r in range(self.rows):		
				if board[r][c] == 1:
					pygame.draw.circle(self.screen, self.player1_color, (int(c*self.square_size+self.square_size/2), self.height-int(r*self.square_size+self.square_size/2)), self.radius)
				elif board[r][c] == 2: 
					pygame.draw.circle(self.screen, self.player2_color, (int(c*self.square_size+self.square_size/2), self.height-int(r*self.square_size+self.square_size/2)), self.radius)
		pygame.display.update()

	def win(self, board, piece):
		for c in range(self.cols-3):
			for r in range(self.rows):
				if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
					return True

		for c in range(self.cols):
			for r in range(self.rows-3):
				if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
					return True

		for c in range(self.cols-3):
			for r in range(self.rows-3):
				if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
					return True

		for c in range(self.cols-3):
			for r in range(3, self.rows):
				if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
					return True

	def run(self):
		
		open('report.txt', 'w').close()
		board = self.create_board()
		self.print_board(board)
		game_over = False
		turn = 0

		player1_made_move = False
		player2_made_move = False
		player1_answered_q = False
		player2_answered_q = False
		player1_correct = False
		player2_correct = False

		pygame.init()
		
		self.draw_board(board)
		pygame.display.update()

		myfont = pygame.font.SysFont("Fira Code", 75)

		while not game_over:

			if not player1_answered_q and turn == 0:
				question_number = random.randint(0,3)
				question = None
				if question_number == 0:
					question = questionsGUI_v2.PermutationQuestionGUI(self.player1_name)
				elif question_number == 1:
					question = questionsGUI_v2.MatricesGUI(self.player1_name)
				elif question_number == 2:
					question = questionsGUI_v2.EulerTotientQuestionGUI(self.player1_name)
				elif question_number == 3:
					question = questionsGUI_v2.VectorQuestionGUI(self.player1_name)
				question.run()
				# question = questionsGUI_v2.random_question(self.player1_name)
				# permutations_question = questionsGUI_v2.PermutationQuestionGUI(self.player1_name)
				# permutations_question.run()
				player1_answered_q = True
				player1_made_move = False
				player1_correct = question.player_correct
				pygame.time.wait(1500)
				if not player1_correct:
					turn += 1
					turn = turn % 2
					player2_answered_q = False
					continue
			
			if not player2_answered_q and turn == 1:
				question_number = random.randint(0,2)
				question = None
				if question_number == 0:
					question = questionsGUI_v2.PermutationQuestionGUI(self.player2_name)
				elif question_number == 1:
					question = questionsGUI_v2.MatricesGUI(self.player2_name)
				elif question_number == 2:
					question = questionsGUI_v2.EulerTotientQuestionGUI(self.player2_name)
				elif question_number == 3:
					question = questionsGUI_v2.VectorQuestionGUI(self.player2_name)
				question.run()
				# permutations_question = questionsGUI_v2.PermutationQuestionGUI(self.player2_name)
				# permutations_question.run()
				player2_answered_q = True
				player2_made_move = False
				player2_correct = question.player_correct
				pygame.time.wait(1500)
				if not player2_correct:
					turn += 1
					turn = turn % 2
					player1_answered_q = False
					continue

			for event in pygame.event.get():
					
				if player1_correct or player2_correct:
				
					self.draw_board(board)
					
					if event.type == pygame.QUIT:
						sys.exit()

					if event.type == pygame.MOUSEMOTION:
						pygame.draw.rect(self.screen, self.background_color, (0,0, self.width, self.square_size))
						posx = event.pos[0]
						if turn == 0:
							pygame.draw.circle(self.screen, self.player1_color, (posx, int(self.square_size/2)), self.radius)
						else: 
							pygame.draw.circle(self.screen, self.player2_color, (posx, int(self.square_size/2)), self.radius)
					pygame.display.update()

					if event.type == pygame.MOUSEBUTTONDOWN:
						pygame.draw.rect(self.screen, self.background_color, (0,0, self.width, self.square_size))			
						# Ask for Player 1 Input
					
						if turn == 0 and player1_correct:
							posx = event.pos[0]
							col = int(math.floor(posx/self.square_size))

							if self.valid_position(board, col):
								row = self.next_free_spot(board, col)
								self.drop_piece(board, row, col, 1)
								player1_made_move = True
								player2_answered_q = False
								player1_correct = False

								if self.win(board, 1):
									label = myfont.render(f"{self.player1_name} wins!!", 1, self.player1_color)
									self.screen.blit(label, (40,10))
									game_over = True

						# Ask for Player 2 Input
						elif turn == 1 and player2_correct:		
							posx = event.pos[0]
							col = int(math.floor(posx/self.square_size))

							if self.valid_position(board, col):
								row = self.next_free_spot(board, col)
								self.drop_piece(board, row, col, 2)
								player2_made_move = True
								player1_answered_q = False
								player2_correct = False

								if self.win(board, 2):
									label = myfont.render(f"{self.player2_name} wins!!", 1, self.player2_color)
									self.screen.blit(label, (40,10))
									game_over = True

						self.print_board(board)
						self.draw_board(board)

						turn += 1
						turn = turn % 2

						if game_over:
							pygame.time.wait(3000)

