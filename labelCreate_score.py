#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:34:14 2019

@author: shailesh
"""

import chess
from chess import pgn
import chess.engine
import chess.svg

gameFile = open("Data/ficsgamesdb_201901_chess2000_nomovetimes_107218.pgn")
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")




#info = engine.analyse(board, chess.engine.Limit(depth=20))
#print("Score:", info["score"])

positions = []
scores = []
counter = 1
while(counter<100):
	print(counter)
	try: 
		game = pgn.read_game(gameFile)
		board = game.board()
	except:
		break
	for move in game.mainline_moves():
	#	predictedMove = engineMoveList[i]
#		print(counter,'\n')
		score = str(engine.analyse(board, chess.engine.Limit(depth="10"))["score"])
		if(score[0] in '+-0') :
			if score =='0':
				score = 0
				
			else:
				score = int(score[1:])
				
				if counter%2==0:
					score*=-1
		else:																			#When mate is seen
			sign = score[1]
			if sign == '-':
				score = -1000
			else:
				score = 1000
		
		positions.append(board.fen())
		scores.append(str(score))
		board.push(move)
	counter+=1

with open("Data/ScoreData/inputs.txt","w") as inputs:
	inputs.writelines(positions)
with open("Data/ScoreData/labels.txt","w") as labels:
	labels.writelines(scores)
	