#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:18:09 2020

@author: shailesh
"""
import numpy as np
import chess

pieces = [chess.PAWN,chess.KNIGHT,chess.BISHOP,chess.ROOK,chess.QUEEN,chess.KING]
colours = [chess.WHITE,chess.BLACK]

def readInputData(path):
	with open(path) as f:
		fens = f.readlines()
	vectors = [fenToVec(fen) for fen in fens]			#X(inputs)
	
	return np.array(vectors)

def readLabels(path):
	with open(path) as f:
		Y = f.readlines()
	return np.array(Y)
def fenToVec(fen):
	posFen = fen.split()[0]
	board = chess.BaseBoard(posFen)
	l = []
	
	for colour in colours:
		for piece in pieces:
			v = np.zeros(64)
			for i in list(board.pieces(piece,colour)):
				v[i] = 1
			l.append(v)
	l = np.concatenate(l)
	return l

	
def vecToFen(vec):
	vecList = np.split(vec,12)
	whiteList = vecList[:6]
	blackList = vecList[6:]
	board = chess.BaseBoard()
	board.clear_board()
	for pieceType in range(len(whiteList)):
		pieceArr = whiteList[pieceType]
		for ind in range(len(pieceArr)):
			if pieceArr[ind]:
				board.set_piece_at(ind ,chess.Piece(pieces[pieceType],chess.WHITE))
				
	for pieceType in range(len(blackList)):
		pieceArr = blackList[pieceType]
		for ind in range(len(pieceArr)):
			if pieceArr[ind]:
				board.set_piece_at(ind ,chess.Piece(pieces[pieceType],chess.BLACK))
	
	return board.board_fen()

			
		
		

#pieces = [chess.PAWN,chess.KNIGHT,chess.BISHOP,chess.ROOK,chess.QUEEN,chess.KING]
#colours = [chess.WHITE,chess.BLACK]