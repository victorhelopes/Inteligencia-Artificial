#! /usr/bin/env python3
'''
PyMaze driver class. Makes use of the maze class to parse program arguments.
@author: Paul Miller (github.com/138paulmiller)
adapted by Dino Franklin
'''

import os, sys, random, time, threading
import maze_gbc063 as maze
import gbc063


# defalt ANSI settings from user
COLOR_DEFAULT = u'\u001b[0m'
# foreground colors (text)
COLOR_BLACK = u'\u001b[30m'
COLOR_RED =  u'\u001b[31m'
COLOR_GREEN = u'\u001b[32m'
COLOR_YELLOW = u'\u001b[33m'
COLOR_BLUE  =u'\u001b[34m'
COLOR_MAGENTA = u'\u001b[35m'
COLOR_CYAN = u'\u001b[36m'
COLOR_WHITE = u'\u001b[37m'
# background colors 
COLOR_BG_BLACK = u'\u001b[40m'
COLOR_BG_RED =	u'\u001b[41m'
COLOR_BG_GREEN =  u'\u001b[42m'
COLOR_BG_YELLOW = u'\u001b[43m'
COLOR_BG_BLUE = u'\u001b[44m'
COLOR_BG_MAGENTA =  u'\u001b[45m'
COLOR_BG_CYAN = u'\u001b[46m'
COLOR_BG_WHITE= u'\u001b[47m'

def play_maze(maze_obj, limit,tinkle):
	print("Possiveis buscas:")
	print("1-Busca em profundiade")
	print("2-Busca por aprofundamento iterativo")
	print("3-Busca por descida de encosta")
	print("4-Busca por tempera simulada")
	opcao = int(input("Digite uma opção:"))
	#clear the screen clear if linux, cls if windows
	os.system('clear' if os.name!='nt' else 'cls')	
	
	# mostra o labirinto
	print(maze_obj.to_str())	
	current = (0,0)
	# em (0,0) pergunta para o labirinto acoes possiveis
	info = maze_obj.move(current)
	current = info[1]
	options = info[2]
		
	move = 0

	visitado = []
	pilha = []
	# sai qdo atinge o max de passos ou chega no objetivo

	aprofundamento = 1# int(input("Nivel maximo de aprofundamento:"))
	if(opcao == 1):
		while not (move > limit) and not maze_obj.is_done():
			print("1")
			time.sleep(1)
			action = gbc063.algoritmo_profundidade(current, options,visitado) 
			info = maze_obj.move(action)
			current = info[1]
			options = info[2]
			move += 1

	if(opcao == 2):
		while not (move > limit) and not maze_obj.is_done():
			time.sleep(1)
			action = gbc063.algoritmo_aprofundamento_iterativo(current, options,pilha,visitado,aprofundamento)
			if(action == []):
				aprofundamento +=1
				visitado = []
				pilha = []
			else:
				info = maze_obj.move(action)
				current = info[1]
				options = info[2]
			move += 1

	if(opcao == 3):
		while not (move > limit) and not maze_obj.is_done():
			time.sleep(0.5)
			action = gbc063.subidaEncosta(current, options) 
			if(action == False):
				print("nao foi possivel achar melhor caminho")
				break
			info = maze_obj.move(action)
			current = info[1]
			options = info[2]
			move += 1
	if(opcao == 4):	
		temp = 100
		fator_diminuicao = 1
		while not (move > limit) and not maze_obj.is_done():
			time.sleep(1)
			action = gbc063.tempera(current, options,temp) 
			temp-= fator_diminuicao
			info = maze_obj.move(action)
			current = info[1]
			options = info[2]
			move += 1
	else:
		return 0

	# saindo
	if (move < limit):
		print('O objetivo foi atingido com ',move,' movimentos');
		print('Solucao (',len(maze_obj.path),' passos)')
		print(maze_obj.path)
	else:
		print('O objetivo nao foi atingido em ',move,' movimentos.');
		

def main():

	clock = 0.1
	seed = random.random()*10000		
	width = 10 	#20
	height = 10 	#12
	limite = 99
	is_block = True
	is_color = True
	block_symbol = u'\u2588'#unicode FullBlock
	block_symbols = {
		'start' : u'O',
		'end' : u'X',
		'wall_v' : block_symbol, 
		'wall_h' : block_symbol,
		'wall_c' : block_symbol,
		'visited' : block_symbol,
	}
	color_symbols = {
		'empty_color' : COLOR_DEFAULT,
		'visited_color' : COLOR_WHITE,   # incluido
		'wall_color' : COLOR_BLUE,
		'head_color' : COLOR_RED,
		'tail_color' : COLOR_CYAN,
		'start_bg_color' : COLOR_BG_YELLOW,
		'end_bg_color' : COLOR_BG_YELLOW,
		# if color, full block for player too
		'head' : block_symbol,
		'tail' : block_symbol,
		'visited' : block_symbol,   # incluido
	}
	#default symbols (not unicode or ANSI coloring)
	symbols = {
		# default symbols
		'start' : 'S',
		'end' : 'X',
		'wall_v'  : '|',
		'wall_h' : '-',
		'wall_c' : '+',
		'head' :  '#',
		'tail' : 'o',	
		'empty' : ' ',
		'visited' : 'v',
	}

	# se quiser desenho em blocos - necessario monospaced font
	# se  nao, comente com #
	symbols.update(block_symbols)
	symbols.update(color_symbols)
				
	# cria o labirinto
	maze_obj = maze.Maze(width, height, seed, symbols)

	# usa seu algoritmo (gbc063) para sair do labirinto
	play_maze(maze_obj,limite,clock)


# main
if __name__ == '__main__':
	main() 
	input()
