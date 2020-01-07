#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:48:06 2020

@author: shailesh
"""

import chess
import numpy as np
from numpy import loadtxt
from keras.models import load_model
import helpers
import chess.svg

from keras.models import load_model
from keras.models import model_from_json
import json

with open('models/model_in_json.json','r') as f:
    model_json = json.load(f)

model = model_from_json(model_json)
model.load_weights('models/model_weights.h5')


def makeBestMove(board,colourToPlay,model):
	scores =[]
#	fen = board.board_fen()
#	posVec = helpers.fenToVec(fen)
	legalMoves = list(board.legal_moves)
	for move in legalMoves:
		board.push(move)
		posVec = np.array([helpers.fenToVec(board.board_fen())])
#		print(posVec)
		board.pop()
		scores.append(model.predict(posVec))
	if colourToPlay == 1:
		bestMove = legalMoves[np.argmax(scores)]
	if colourToPlay ==0:
		bestMove = legalMoves[np.argmin(scores)]
	board.push(bestMove)




board = chess.Board()
colourToPlay = 1
while(not board.is_game_over()):
	makeBestMove(board,colourToPlay,model)
	colourToPlay = not colourToPlay   #toggle colour to play
	print(board,'\n\n')
	chess.svg.board(board=board)
	
	