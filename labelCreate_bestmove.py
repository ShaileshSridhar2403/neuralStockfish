#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:27:19 2019

@author: shailesh
"""

import chess
from chess import pgn
import chess.engine
import chess.svg

game = open("/home/shailesh/Projects/neuralStockfish/neuralStockfish/ficsgamesdb_455930641.pgn")
game = pgn.read_game(game)

engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

board = game.board()


#player.append(board.fen())
#result = engine.play(board, chess.engine.Limit(time=0.1))


#for move in game.mainline_moves():
#	playerMoveList.append(move)
#	result = engine.play(board, chess.engine.Limit(time=0.1))
#	board.push(move)
#	engineMoveList.append(result.move)

#playerMoveList = game.mainline_moves()

positions = []
predictedPositions = []

for move in game.mainline_moves():
#	predictedMove = engineMoveList[i]
	print(board,'\n')
	chess.svg.board(board)
	predictedMove = engine.play(board, chess.engine.Limit(time=0.1)).move
	board.push(predictedMove)
	print(board,'\n'*3)
	predictedPositions.append(board.fen())
	board.pop()
	positions.append(board.fen())
	board.push(move)
	


with open("inputs.txt","w") as inputs:
	inputs.writelines(positions)
with open("labels.txt","w") as labels:
	labels.writelines(predictedPositions)